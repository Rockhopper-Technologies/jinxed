#!/usr/bin/env python3
"""
Generate 'jinxed.terminfo' terminfo files using ncurses terminfo.src using tic(1) and infocmp(1).

This script runs on modern Python (3.14 at time of writing) but the modules it generates are Python
2.7-safe -- they use only list, dict, bytes, and string literals, and do not use f-strings, type
annotations, or typing imports.
"""
import gzip
import os
import re
import subprocess
import sys
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

URL = 'https://invisible-mirror.net/archives/ncurses/current/terminfo.src.gz'
HERE_DIR = Path(__file__).resolve().parent
OUT_DIR = HERE_DIR / 'jinxed' / 'terminfo'

TERMINALS_TXT = HERE_DIR / 'terminals.txt'

# We track 'hand maintained' ones so that we can more clearly attribute their origin in the
# documentation we generate
HAND_MAINTAINED = {'syncterm', 'ansi-bbs', 'ansicon', 'vtwin10', 'ansi'}

# Aliases not present in the ncurses source but can be found on systems, in my case, the 'ghostty'
# installed from source uses TERM=xterm-ghostty, but this is only available with the installed local
# termcap $HOME/.terminfo/g/ghostty, so we provide this alias for code generation on other systems.
EXTRA_ALIASES = {'xterm-ghostty': 'ghostty', 'xterm-kitty': 'kitty'}

GITHUB_BASE = 'https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo'

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
            'add_b': [c for c in self.bools if c not in base.bools],
            'rm_b': [c for c in base.bools if c not in self.bools],
            'mod_n': {k: v for k, v in self.nums.items()
                      if k not in base.nums or base.nums.get(k) != v},
            'add_s': {k: v for k, v in self.strs.items() if k not in base.strs},
            'rm_s': [k for k in base.strs if k not in self.strs],
            'mod_s': {k: v for k, v in self.strs.items()
                      if k in base.strs and base.strs[k] != v},
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
        m = re.match(r"^\s*'(\w+)',\s*#\s*(.*)$", line)
        if m:
            target = bool_comments if current == 'bool' else num_comments
            target[m.group(1)] = m.group(2).rstrip()
    return bool_comments, num_comments


def decode(value: str) -> bytes:
    """Decode an infocmp -1 string value into bytes."""
    result = bytearray()
    i = 0
    while i < len(value):
        c = value[i]
        if c == '\\':
            i += 1
            if i >= len(value):
                break
            esc = value[i]
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
                    if i + 1 < len(value) and value[i + 1] in '01234567':
                        i += 1
                        octal += value[i]
                result.append(int(octal, 8))
            elif esc == 'x':
                i += 1
                if i >= len(value):
                    break
                h = value[i]
                if i + 1 < len(value) and value[i + 1] in '0123456789abcdefABCDEF':
                    i += 1
                    h += value[i]
                result.append(int(h, 16))
            else:
                result.append(ord(esc))
        elif c == '^':
            i += 1
            if i >= len(value):
                break
            ctrl = value[i]
            if 'A' <= ctrl <= '_':
                result.append(ord(ctrl) - ord('A') + 1)
            elif ctrl == '?':
                result.append(0x7f)
            else:
                result.append(ord(ctrl) & 0x1f)
        elif c == ',' and i == len(value) - 1:
            break
        else:
            result.append(ord(c))
        i += 1
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
        m = re.match(r'^(\w+)#(-?[\d]+|0[xX][\da-fA-F]+|0[0-7]+)$', line)
        if m:
            name, vs = m.group(1), m.group(2)
            if vs.startswith(('0x', '0X')):
                val = int(vs, 16)
            elif vs.startswith('0') and len(vs) > 1:
                val = int(vs, 8)
            else:
                val = int(vs)
            if name in NUM_CAPS:
                nums[name] = val
            continue
        m = re.match(r"^(\w+)=(.*)$", line)
        if m:
            name, raw = m.group(1), m.group(2)
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
    gz = cache / 'terminfo.src.gz'
    src = cache / 'terminfo.src'
    db = cache / 'terminfo.db'

    urlretrieve(URL, gz)

    src.write_bytes(gzip.decompress(gz.read_bytes()))

    version = 'unknown'
    header = src.read_text(errors='replace')[:4000]
    m = re.search(r'\$Revision: (\S+) \$', header)
    if m:
        version = m.group(1)

    db.mkdir(exist_ok=True)
    # Let tic write directly to the terminal so errors are visible
    subprocess.run(['tic', '-o', str(db), str(src)], check=True)

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
        fields = [f.strip() for f in header.split('|')]
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
        '# Auto-generated by codegen_terminfo.py',
        '# Maps alternative terminal names to the primary ncurses name.',
        '# Primary names are module names (with \'-\' replaced by \'_\').',
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
                for m in re.finditer(r'use=(\S+?),', line):
                    term_uses.setdefault(current_term, []).append(m.group(1))
            continue
        current_term = line.split('|')[0].strip()
        if current_term.endswith('+'):
            current_term = None

    result: dict[str, str | None] = {}
    for name in wanted:
        targets = term_uses.get(name, [])
        result[name] = next((t for t in targets if t in wanted), None)
    return result


def extract(kind: str, db: Path) -> TermData | None:
    """Extract compiled terminfo entry via infocmp."""
    env = {**os.environ, 'TERMINFO': str(db), 'TERMINFO_DIRS': str(db)}
    try:
        r = subprocess.check_output(['infocmp', '-1', kind],
                                    text=True, timeout=10, env=env)
        return parse(r)
    except (subprocess.SubprocessError, OSError):
        return None


def expand(db: Path) -> list[str]:
    """Return sorted list of terminal names to generate."""
    wanted = {line.split('#')[0].strip() for line in TERMINALS_TXT.read_text().splitlines()
              if line.split('#')[0].strip()}

    env = {**os.environ, 'TERMINFO': str(db), 'TERMINFO_DIRS': str(db)}
    try:
        r = subprocess.run(['toe', '-a'], capture_output=True, text=True, env=env,
                           check=True)
    except (subprocess.SubprocessError, OSError):
        print('WARNING: toe -a failed, no terminals available', file=sys.stderr)
        return []
    available = {line.split(None, 1)[0] for line in r.stdout.splitlines() if line.strip()}

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
    ]

    if base and base_data:
        base_mod = base.replace('-', '_')
        lines += [
            f'from .{base_mod} import BOOL_CAPS, NUM_CAPS, STR_CAPS',
            '',
            'BOOL_CAPS = BOOL_CAPS[:]',
            'NUM_CAPS = NUM_CAPS.copy()',
            'STR_CAPS = STR_CAPS.copy()',
        ]
        d = data.diff(base_data)
        for cap in d['add_b']:
            lines.append(f"BOOL_CAPS.append('{cap}')")
        for cap in d['rm_b']:
            lines.append(f"BOOL_CAPS.remove('{cap}')  # noqa")
        for k, v in sorted(d['mod_n'].items()):
            lines.append(f"NUM_CAPS['{k}'] = {v}")
        for label, items in (
            ('Added strings', d['add_s']),
            ('Removed strings', d['rm_s']),
            ('Modified strings', d['mod_s']),
        ):
            if items:
                lines.append('')
                lines.append(f'# {label}')
                if isinstance(items, dict):
                    for k, v in sorted(items.items()):
                        lines.append(f"STR_CAPS['{k}'] = {bytes_repr(v)}")
                else:
                    for k in items:
                        lines.append(f"del STR_CAPS['{k}']")
    else:
        lines.append('BOOL_CAPS = [')
        bool_entries: list[tuple[str, str | None]] = [
            (f"    '{cap_name}',", BOOL_COMMENTS.get(cap_name))
            for cap_name in data.bools
        ]
        max_bool = max((len(e) for e, _ in bool_entries), default=0)
        for entry, comment in bool_entries:
            lines.append(f"{entry:<{max_bool + 2}}  # {comment}" if comment else entry)
        lines.append(']')
        lines.append('')

        lines.append('NUM_CAPS = {')
        num_entries: list[tuple[str, str | None]] = [
            (f"    '{k}': {v},", NUM_COMMENTS.get(k))
            for k, v in sorted(data.nums.items())
        ]
        max_num = max((len(e) for e, _ in num_entries), default=0)
        for entry, comment in num_entries:
            lines.append(f"{entry:<{max_num + 2}}  # {comment}" if comment else entry)
        lines.append('}')
        lines.append('')

        lines.append('STR_CAPS = {')
        lines.extend(f"    '{k}': {bytes_repr(v)},"
                     for k, v in sorted(data.strs.items()))
        lines.append('}')
    lines.append('')
    return '\n'.join(lines)


def update_capabilities_rst(term_dir: Path,
                           aliases: dict[str, str] | None = None) -> None:
    """Regenerate the terminal list between BEGIN/END markers in capabilities.rst."""
    rst_path = HERE_DIR / 'doc' / 'capabilities.rst'
    if not rst_path.exists():
        return

    modules = sorted(p.stem for p in term_dir.glob('*.py')
                     if p.stem not in ('__init__', '_aliases'))

    lines_out: list[str] = []
    in_marker = False
    for line in rst_path.read_text().splitlines():
        stripped = line.strip()
        if stripped == '.. BEGIN_TERMINAL_LIST':
            in_marker = True
            lines_out.append(line)
            auto = [m for m in modules if m.replace('_', '-') not in HAND_MAINTAINED]
            hand = [m for m in modules if m.replace('_', '-') in HAND_MAINTAINED]
            for mod in auto:
                line = f'- `{mod.replace("_", "-")} <{GITHUB_BASE}/{mod}.py>`_'
                if aliases:
                    mod_aliases = sorted(a for a, p in aliases.items()
                                         if p == mod.replace('_', '-'))
                    if mod_aliases:
                        line += ', ' + ', '.join(mod_aliases)
                lines_out.append(line)
            if hand:
                lines_out.append('')
                lines_out.append('Hand-maintained (not generated by codegen):')
                lines_out.append('')
                for mod in hand:
                    lines_out.append(f'- `{mod.replace("_", "-")} <{GITHUB_BASE}/{mod}.py>`_')
            continue
        if stripped == '.. END_TERMINAL_LIST':
            in_marker = False
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
    for k in terms:
        d = extract(k, db)
        if d:
            data_map[k] = d
        else:
            print(f'SKIP: {k}', file=sys.stderr)

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
    for k, d in data_map.items():
        base: str | None = None
        base_data: TermData | None = None
        if mapping_use_base.get(k) and mapping_use_base[k] in data_map:
            base = mapping_use_base[k]
            base_data = data_map[base]
        fpath = OUT_DIR / f'{k.replace("-", "_")}.py'
        fpath.write_text(generate(k, d, version, base, base_data))

    print(f'{len(data_map)} modules -> {OUT_DIR}', file=sys.stderr)
    print(f'Source: ncurses terminfo.src {version}', file=sys.stderr)

    update_capabilities_rst(OUT_DIR, aliases)


if __name__ == '__main__':
    BOOL_COMMENTS, NUM_COMMENTS = parse_cap_comments()
    main()
