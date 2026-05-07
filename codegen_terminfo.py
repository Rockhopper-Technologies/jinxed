#!/usr/bin/env python3
"""
Generate 'jinxed.terminfo' terminfo files using ncurses terminfo.src using tic(1) and infocmp(1).

This script runs on modern Python (3.14 at time of writing) but the modules it generates are Python
2.7-safe -- they use only list, dict, bytes, and string literals, and do not use f-strings, type
annotations, or typing imports.
"""
import os
import re
import subprocess
import sys
import tarfile
import tempfile
from dataclasses import dataclass
from pathlib import Path
from urllib.request import urlretrieve

from jinxed.terminfo import BOOL_CAPS as BOOL_NAMES, NUM_CAPS as NUM_NAMES

BOOL_CAPS = frozenset(BOOL_NAMES)
NUM_CAPS = frozenset(NUM_NAMES)

# G0/G1 character set designation sequences: ESC ( X or ESC ) X
# where X is one of 0, A, B, U, K (DEC Special Graphics, UK, ASCII,
# Null, User).  Stripped because they are harmful on modern UTF-8
# terminals, where they corrupt output by switching away from UTF-8.
G0_G1_DESIGNATION = re.compile(b'\x1b[()][0ABUK]')

# After stripping G0/SO/SI bytes from
#   %?%p9%t<g0_seq>%e<g0_seq>%;
# the conditional reduces to a no-op husk  %?%p9%t%e%;
# with empty then/else branches.  Clean it up.
SGR_EMPTY_COND = re.compile(b'%\\?%p9%t%e%;')

# Delay tokens: $<N> (ms), $<N/M> (fractional seconds), $<N*> (proportional).
# Harmful on modern terminal emulators; stripped from all string capabilities.
DELAY_TOKEN = re.compile(b'\\$<[^>]+>')

# Capabilities that are inherently G0/G1 character-set operations.
# Set to empty bytes rather than dropped -- signals "unsupported" to callers.
EMPTY_CAPS = frozenset({'smacs', 'rmacs', 'enacs', 's0ds', 's1ds'})

URL = 'https://invisible-mirror.net/archives/ncurses/current/ncurses.tar.gz'
HERE_DIR = Path(__file__).resolve().parent
OUT_DIR = HERE_DIR / 'jinxed' / 'terminfo'

TERMINALS_TXT = HERE_DIR / 'terminals.txt'

_MODULE_RE = re.compile(r'[.-]')

def _module_name(term: str) -> str:
    """Convert a terminal name to a valid Python module name."""
    return _MODULE_RE.sub('_', term).lower()

# We track 'hand maintained' ones so that we can more clearly attribute their origin in the
# documentation we generate
HAND_MAINTAINED = {'syncterm', 'ansi-bbs', 'ansicon', 'vtwin10', 'ansi'}

# Aliases not present in the ncurses source but can be found on systems, in my case, the 'ghostty'
# installed from source uses TERM=xterm-ghostty, but this is only available with the installed local
# termcap $HOME/.terminfo/g/ghostty, so we provide this alias for code generation on other systems.
EXTRA_ALIASES = {'xterm-ghostty': 'ghostty', 'xterm-kitty': 'kitty'}

GITHUB_BASE = 'https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo'

# Fixups applied to capability data. These were discovered by comparing XTGETTCAP results form the
# ucs-detect project https://github.com/jquast/ucs-detect/ vs. ncurses entries.


def apply_fixups(data_map: dict[str, 'TermData']) -> None:
    """Patch known ncurses terminfo errors in-place."""
    for name, data in data_map.items():
        if name == 'kitty':
            # ncurses att610+cvis0: cnorm=\E[?12l               (blink off)
            # kitty kitty/terminfo.py:128: 'cnorm': r'\E[?12h'  (blink on)
            if data.strs.get('cnorm') == b'\x1b[?12l\x1b[?25h':
                data.strs['cnorm'] = b'\x1b[?12h\x1b[?25h'
        elif name == 'contour':
            # ncurses vt220+cvis: cnorm=\E[?25h                 (no mode 12)
            # contour Capabilities.cpp:104: "\033[?12l\033[?25h"
            if data.strs.get('cnorm') == b'\x1b[?25h':
                data.strs['cnorm'] = b'\x1b[?12l\x1b[?25h'
        elif name == 'wezterm':
            # ncurses ansi+erase:  clear=\E[H\E[J               (no ED param)
            # ncurses xterm+256color2: 48:5:                    (colon sep)
            # wezterm wezterm.terminfo:40,81-82:
            #   cnorm=\E[?12l\E[?25h, clear=\E[H\E[2J,
            #   setab/setaf use 48;5; / 38;5;
            if data.strs.get('cnorm') == b'\x1b[?25h':
                data.strs['cnorm'] = b'\x1b[?12l\x1b[?25h'
            if data.strs.get('clear') == b'\x1b[H\x1b[J':
                data.strs['clear'] = b'\x1b[H\x1b[2J'
            if data.strs.get('setab') == (
                b'\x1b[%?%p1%{8}%<%t4%p1%d'
                b'%e%p1%{16}%<%t10%p1%{8}%-%d'
                b'%e48:5:%p1%d%;m'
            ):
                data.strs['setab'] = (
                    b'\x1b[%?%p1%{8}%<%t4%p1%d'
                    b'%e%p1%{16}%<%t10%p1%{8}%-%d'
                    b'%e48;5;%p1%d%;m')
            if data.strs.get('setaf') == (
                b'\x1b[%?%p1%{8}%<%t3%p1%d'
                b'%e%p1%{16}%<%t9%p1%{8}%-%d'
                b'%e38:5:%p1%d%;m'
            ):
                data.strs['setaf'] = (
                    b'\x1b[%?%p1%{8}%<%t3%p1%d'
                    b'%e%p1%{16}%<%t9%p1%{8}%-%d'
                    b'%e38;5;%p1%d%;m')


# Lazy-initialised after parse_cap_comments() is called.
BOOL_COMMENTS: dict[str, str] = {}
NUM_COMMENTS: dict[str, str] = {}


@dataclass
class TermData:
    """Parsed terminfo capabilities with classification (diff) support."""

    bools: list[str]
    nums: dict[str, int]
    strs: dict[str, bytes]

    def diff(self, base: 'TermData') -> dict:
        """Return structured diff of this terminal against *base*."""
        return {
            'add_b': [cap for cap in self.bools if cap not in base.bools],
            'rm_b': [cap for cap in base.bools if cap not in self.bools],
            'mod_n': {key: val for key, val in self.nums.items()
                      if key not in base.nums or base.nums.get(key) != val},
            'add_s': {key: val for key, val in self.strs.items()
                      if key not in base.strs},
            'rm_s': [key for key in base.strs if key not in self.strs],
            'mod_s': {key: val for key, val in self.strs.items()
                      if key in base.strs and base.strs[key] != val},
        }


def strip_g0(value: bytes) -> bytes:
    """Strip G0 character set designation sequences, SO/SI, and delay tokens."""
    value = G0_G1_DESIGNATION.sub(b'', value)
    value = value.replace(b'\x0e', b'').replace(b'\x0f', b'')
    value = SGR_EMPTY_COND.sub(b'', value)
    value = DELAY_TOKEN.sub(b'', value)
    return value


def parse_cap_comments() -> tuple[dict[str, str], dict[str, str]]:
    """Parse inline comments from jinxed/terminfo/__init__.py.

    Returns (bool_comments, num_comments) dicts mapping cap name to comment text.
    """
    init_py = HERE_DIR / 'jinxed' / 'terminfo' / '__init__.py'
    source = init_py.read_text()

    bool_comments: dict[str, str] = {}
    num_comments: dict[str, str] = {}
    current: str | None = None
    for line in source.splitlines():
        stripped = line.strip()
        if stripped == 'BOOL_CAPS = [':
            current = 'bool'
            continue
        if stripped == 'NUM_CAPS = [':
            current = 'num'
            continue
        if stripped == ']':
            current = None
            continue
        if current is None:
            continue
        if (match := re.match(r"^\s*'(\w+)',\s*#\s*(.*)$", line)):
            target = bool_comments if current == 'bool' else num_comments
            target[match.group(1)] = match.group(2).rstrip()
    return bool_comments, num_comments


def decode(value: str) -> bytes:
    """Decode an infocmp -1 string value into bytes."""
    result = bytearray()
    idx = 0
    while idx < len(value):
        char = value[idx]
        if char == '\\':
            idx += 1
            if idx >= len(value):
                break
            esc = value[idx]
            if esc in ('E', 'e'):
                result.append(0x1b)
            elif esc == 'n':
                result.append(0x0a)
            elif esc == 't':
                result.append(0x09)
            elif esc == 'r':
                result.append(0x0d)
            elif esc == 'b':
                result.append(0x08)
            elif esc == 'f':
                result.append(0x0c)
            elif esc == 's':
                result.append(0x20)
            elif esc == 'l':
                result.append(0x0a)
            elif esc in ',:^\\':
                result.append(ord(esc))
            elif esc in '01234567':
                octal = esc
                for _ in range(2):
                    if idx + 1 < len(value) and value[idx + 1] in '01234567':
                        idx += 1
                        octal += value[idx]
                result.append(int(octal, 8))
            elif esc == 'x':
                idx += 1
                if idx >= len(value):
                    break
                hx = value[idx]
                if idx + 1 < len(value) and value[idx + 1] in '0123456789abcdefABCDEF':
                    idx += 1
                    hx += value[idx]
                result.append(int(hx, 16))
            else:
                result.append(ord(esc))
        elif char == '^':
            idx += 1
            if idx >= len(value):
                break
            ctrl = value[idx]
            if 'A' <= ctrl <= '_':
                result.append(ord(ctrl) - ord('A') + 1)
            elif ctrl == '?':
                result.append(0x7f)
            else:
                result.append(ord(ctrl) & 0x1f)
        elif char == ',' and idx == len(value) - 1:
            break
        else:
            result.append(ord(char))
        idx += 1
    return bytes(result)


def parse(output: str) -> TermData:
    """Parse infocmp -1 output into a TermData instance."""
    bools: list[str] = []
    nums: dict[str, int] = {}
    strs: dict[str, bytes] = {}
    for line in output.strip().splitlines():
        line = line.strip().rstrip(',')
        if not line or line.startswith('#'):
            continue
        if (match := re.match(r'^(\w+)#(-?[\d]+|0[xX][\da-fA-F]+|0[0-7]+)$', line)):
            name, vs = match.group(1), match.group(2)
            if vs.startswith(('0x', '0X')):
                val = int(vs, 16)
            elif vs.startswith('0') and len(vs) > 1:
                val = int(vs, 8)
            else:
                val = int(vs)
            if name in NUM_CAPS:
                nums[name] = val
            continue
        if (match := re.match(r"^(\w+)=(.*)$", line)):
            name, raw = match.group(1), match.group(2)
            if name in EMPTY_CAPS:
                strs[name] = b''
                continue
            val = decode(raw)
            if val:
                val = strip_g0(val)
            if val:
                strs[name] = val
            continue
        if re.match(r'^(\w+)$', line) and line in BOOL_CAPS:
            bools.append(line)
    for cap_name in EMPTY_CAPS:
        strs.setdefault(cap_name, b'')
    return TermData(bools, nums, strs)


def fetch() -> tuple[Path, str]:
    """Download and compile the ncurses terminfo source.

    Returns (db_path, version).
    """
    cache = Path(tempfile.mkdtemp(prefix='jinxed-terminfo-'))
    tarball = cache / 'ncurses.tar.gz'
    src = cache / 'terminfo.src'
    db = cache / 'terminfo.db'

    urlretrieve(URL, tarball)

    # Extract misc/terminfo.src from the ncurses tarball
    with tarfile.open(tarball) as tarf:
        for member in tarf.getmembers():
            if member.name.endswith('/misc/terminfo.src'):
                fobj = tarf.extractfile(member)
                if fobj:
                    src.write_bytes(fobj.read())
                break

    version = 'unknown'
    header = src.read_text(errors='replace')[:4000]
    if (match := re.search(r'\$Revision: (\S+) \$', header)):
        version = match.group(1)

    db.mkdir(exist_ok=True)
    # Let tic write directly to the terminal so errors are visible
    subprocess.run(['tic', '-x', '-o', str(db), str(src)], check=True)

    return db, version


def parse_terminal_aliases(src: Path, wanted: set[str]) -> dict[str, str]:
    """Parse terminal name aliases from the ncurses source.

    Terminal entries have the form: primary|alias1|alias2|description,
    Returns a dict mapping each alias to its primary name.
    Only terminals in *wanted* are included.
    """
    text = src.read_text(errors='replace')
    aliases: dict[str, str] = {}
    for line in text.splitlines():
        if not line or line[0] in '#\t ':
            continue
        # Terminal header: fields separated by |, terminated by comma
        if '|' not in line:
            continue
        # Split on comma first, then on |
        header = line.split(',')[0]
        fields = [field.strip() for field in header.split('|')]
        if len(fields) < 2:
            continue
        primary = fields[0]
        if primary not in wanted:
            continue
        # Middle fields (between primary and description) are aliases.
        # The description (last field) typically has spaces/mixed case.
        # Accept aliases that look like valid terminal names:
        # no spaces, alphanumeric with hyphens/underscores.
        for alias in fields[1:-1]:
            if re.match(r'^[a-zA-Z0-9][-a-zA-Z0-9_]*$', alias) and alias != primary:
                aliases[alias] = primary
    return aliases


def generate_aliases(aliases: dict[str, str], outdir: Path) -> None:
    """Generate the jinxed/terminfo/_aliases.py module."""
    lines = [
        '"""Auto-generated terminal name aliases."""',
        '# Auto-generated by codegen_terminfo.py',
        '# Maps alternative terminal names to the primary ncurses name.',
        '# Primary names are module names (with \'-\' and \'.\' replaced by \'_\').',
        '',
        'ALIASES = {',
    ]
    for alias, primary in sorted(aliases.items()):
        lines.append(f"    '{alias}': '{primary}',")
    lines.append('}')
    lines.append('')

    fpath = outdir / '_aliases.py'
    fpath.write_text('\n'.join(lines))
    print(f'{len(aliases)} aliases -> {fpath}', file=sys.stderr)


def parse_use_chain(src: Path, wanted: set[str]) -> dict[str, str | None]:
    """Parse ``use=`` directives from terminfo.src for terminals in 'wanted'.

    Returns dict mapping terminal name to a 'base' terminal name,
    or None if the terminal has no ``use=`` target that is also in *wanted*.
    """
    text = src.read_text(errors='replace')
    term_uses: dict[str, list[str]] = {}
    current_term: str | None = None
    for line in text.splitlines():
        if not line or line[0] in '#\t ':
            if current_term and line.strip():
                for match in re.finditer(r'use=(\S+?),', line):
                    term_uses.setdefault(current_term, []).append(match.group(1))
            continue
        current_term = line.split('|')[0].strip()
        if current_term.endswith('+'):
            current_term = None

    result: dict[str, str | None] = {}
    for name in wanted:
        targets = term_uses.get(name, [])
        result[name] = next((trg for trg in targets if trg in wanted), None)
    return result


def extract(kind: str, db: Path) -> TermData | None:
    """Extract compiled terminfo entry via infocmp."""
    env = {**os.environ, 'TERMINFO': str(db), 'TERMINFO_DIRS': str(db)}
    try:
        output = subprocess.check_output(['infocmp', '-1', kind],
                                         text=True, timeout=10, env=env)
        return parse(output)
    except (subprocess.SubprocessError, OSError):
        return None


def expand(db: Path) -> list[str]:
    """Return sorted list of terminal names to generate."""
    wanted = {line.split('#')[0].strip() for line in TERMINALS_TXT.read_text().splitlines()
              if line.split('#')[0].strip()}

    env = {**os.environ, 'TERMINFO': str(db), 'TERMINFO_DIRS': str(db)}
    try:
        result = subprocess.run(['toe', '-a'], capture_output=True, text=True, env=env,
                                check=True)
    except (subprocess.SubprocessError, OSError):
        print('WARNING: toe -a failed, no terminals available', file=sys.stderr)
        return []
    available = {line.split(None, 1)[0] for line in result.stdout.splitlines()
                 if line.strip()}

    return sorted(wanted & available - HAND_MAINTAINED)


def bytes_repr(value: bytes) -> str:
    """Format bytes value as a Python bytes literal."""
    named = {0x07: '\\a', 0x08: '\\b', 0x09: '\\t', 0x0a: '\\n',
             0x0d: '\\r', 0x0c: '\\f', 0x0b: '\\v', 0x1b: '\\x1b'}
    parts: list[str] = []
    for byte in value:
        if byte in named:
            parts.append(named[byte])
        elif 0x20 <= byte <= 0x7e and byte not in (0x27, 0x5c):
            parts.append(chr(byte))
        else:
            parts.append(f'\\x{byte:02x}')
    return "b'" + ''.join(parts) + "'"


def generate(kind: str, data: TermData, version: str, base: str | None = None,
             base_data: TermData | None = None) -> str:
    """Generate a jinxed terminfo module for *kind*.

    When *base* and *base_data* are given, generates a derived (inheriting)
    module that only records differences from the base terminal.
    """
    lines = [
        '"""',
        f'{kind} terminal info' + (f' (derived from {base})' if base else ''),
        '',
        f'Revision: {version}',
        f'Source: {URL}',
        '',
        'This file is derived from the ncurses terminfo database, which is',
        'distributed under the MIT/X11 license.  See LICENSE.ncurses.',
        '"""',
        '',
        '# flake8: noqa: E501',
        '# pylint: disable=line-too-long',
        '',
    ]

    if base and base_data:
        base_mod = _module_name(base)
        lines += [
            f'from .{base_mod} import BOOL_CAPS, NUM_CAPS, STR_CAPS',
            '',
            'BOOL_CAPS = BOOL_CAPS[:]',
            'NUM_CAPS = NUM_CAPS.copy()',
            'STR_CAPS = STR_CAPS.copy()',
        ]
        diff = data.diff(base_data)
        for cap in diff['add_b']:
            lines.append(f"BOOL_CAPS.append('{cap}')")
        for cap in diff['rm_b']:
            lines.append(f"BOOL_CAPS.remove('{cap}')  # noqa")
        for key, val in sorted(diff['mod_n'].items()):
            lines.append(f"NUM_CAPS['{key}'] = {val}")
        for label, items in (
            ('Added strings', diff['add_s']),
            ('Removed strings', diff['rm_s']),
            ('Modified strings', diff['mod_s']),
        ):
            if items:
                lines.append('')
                lines.append(f'# {label}')
                if isinstance(items, dict):
                    for key, val in sorted(items.items()):
                        lines.append(f"STR_CAPS['{key}'] = {bytes_repr(val)}")
                else:
                    for key in items:
                        lines.append(f"del STR_CAPS['{key}']")
    else:
        lines.append('BOOL_CAPS = [')
        bool_entries: list[tuple[str, str | None]] = [
            (f"    '{cap_name}',", BOOL_COMMENTS.get(cap_name))
            for cap_name in data.bools
        ]
        max_bool = max((len(ent) for ent, _ in bool_entries), default=0)
        for entry, comment in bool_entries:
            lines.append(f"{entry:<{max_bool + 2}}  # {comment}" if comment else entry)
        lines.append(']')
        lines.append('')

        lines.append('NUM_CAPS = {')
        num_entries: list[tuple[str, str | None]] = [
            (f"    '{key}': {val},", NUM_COMMENTS.get(key))
            for key, val in sorted(data.nums.items())
        ]
        max_num = max((len(ent) for ent, _ in num_entries), default=0)
        for entry, comment in num_entries:
            lines.append(f"{entry:<{max_num + 2}}  # {comment}" if comment else entry)
        lines.append('}')
        lines.append('')

        lines.append('STR_CAPS = {')
        lines.extend(f"    '{key}': {bytes_repr(val)},"
                     for key, val in sorted(data.strs.items()))
        lines.append('}')
    lines.append('')
    return '\n'.join(lines)


def update_capabilities_rst(term_dir: Path,
                            aliases: dict[str, str] | None = None) -> None:
    """Regenerate the terminal list between BEGIN/END markers in capabilities.rst."""
    rst_path = HERE_DIR / 'doc' / 'capabilities.rst'
    if not rst_path.exists():
        return

    modules = sorted(path.stem for path in term_dir.glob('*.py')
                     if path.stem not in ('__init__', '_aliases'))

    lines_out: list[str] = []
    in_marker = False
    for line in rst_path.read_text().splitlines():
        stripped = line.strip()
        if stripped == '.. BEGIN_TERMINAL_LIST':
            in_marker = True
            lines_out.append(line)
            lines_out.append('')
            auto = [mod for mod in modules
                    if mod.replace('_', '-') not in HAND_MAINTAINED]
            hand = [mod for mod in modules
                    if mod.replace('_', '-') in HAND_MAINTAINED]
            for mod in auto:
                line = f'- `{mod.replace("_", "-")} <{GITHUB_BASE}/{mod}.py>`_'
                if aliases:
                    mod_aliases = sorted(als for als, pri in aliases.items()
                                         if _module_name(pri) == mod)
                    if mod_aliases:
                        line += ', ' + ', '.join(mod_aliases)
                lines_out.append(line)
            if hand:
                lines_out.append('')
                lines_out.append('Hand-maintained (not generated by codegen):')
                lines_out.append('')
                for mod in hand:
                    lines_out.append(
                        f'- `{mod.replace("_", "-")} <{GITHUB_BASE}/{mod}.py>`_')
            continue
        if stripped == '.. END_TERMINAL_LIST':
            in_marker = False
            lines_out.append('')
            lines_out.append(line)
            continue
        if not in_marker:
            lines_out.append(line)

    rst_path.write_text('\n'.join(lines_out) + '\n')
    print(f'Updated {rst_path} ({len(modules)} terminals)', file=sys.stderr)


def main() -> None:
    db, version = fetch()
    terms = expand(db)

    data_map: dict[str, TermData] = {}
    for kind in terms:
        data = extract(kind, db)
        if data:
            data_map[kind] = data
        else:
            print(f'SKIP: {kind}', file=sys.stderr)

    apply_fixups(data_map)

    # Parse use= directives from the ncurses source to find explicit
    # derivation chains (e.g. rio -> alacritty).
    src = db.parent / 'terminfo.src'

    # Generate terminal name aliases
    wanted_terms = set(data_map)
    aliases = parse_terminal_aliases(src, wanted_terms)
    for alias, primary in EXTRA_ALIASES.items():
        if primary in wanted_terms and alias not in aliases:
            aliases[alias] = primary
    generate_aliases(aliases, OUT_DIR)
    mapping_use_base = parse_use_chain(src, wanted_terms)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for kind, data in data_map.items():
        base: str | None = None
        base_data: TermData | None = None
        if mapping_use_base.get(kind) and mapping_use_base[kind] in data_map:
            base = mapping_use_base[kind]
            base_data = data_map[base]
        fpath = OUT_DIR / f'{_module_name(kind)}.py'
        fpath.write_text(generate(kind, data, version, base, base_data))

    print(f'{len(data_map)} modules -> {OUT_DIR}', file=sys.stderr)
    print(f'Source: ncurses terminfo.src {version}', file=sys.stderr)

    update_capabilities_rst(OUT_DIR, aliases)


if __name__ == '__main__':
    BOOL_COMMENTS, NUM_COMMENTS = parse_cap_comments()
    main()
