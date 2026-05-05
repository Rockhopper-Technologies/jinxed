"""
Pure-Python compiled terminfo file parser.

Reads binary terminfo files (e.g. /usr/share/terminfo/x/xterm) using
jinxed's capability name lists for ordering.  No external dependencies
beyond jinxed's own terminfo data.
"""

import os
import struct
from collections import OrderedDict
from typing import Dict, List, Optional, Tuple

from jinxed.terminfo import BOOL_CAPS as _BOOL_NAMES
from jinxed.terminfo import NUM_CAPS as _NUM_NAMES
# String capability names in ncurses order, derived from xterm module.
from jinxed.terminfo.xterm import STR_CAPS as _XTERM_STR_CAPS
_STR_NAMES: Tuple[str, ...] = tuple(_XTERM_STR_CAPS.keys())


def find_terminfo_path(kind: str) -> Optional[str]:
    """Find the compiled terminfo file for a terminal kind."""
    if not kind or kind in ('dumb', 'unknown'):
        return None

    first_char = kind[0]
    search_dirs = [
        os.path.expanduser('~/.terminfo'),
        '/etc/terminfo',
        '/usr/share/terminfo',
        '/usr/local/share/terminfo',
        '/lib/terminfo',
        '/usr/share/lib/terminfo',
    ]
    hex_dir = f'{ord(first_char):02x}'

    for base in search_dirs:
        for subdir in (first_char, hex_dir):
            path = os.path.join(base, subdir, kind)
            if os.path.isfile(path):
                return path
    return None


def parse_terminfo(
    path: str,
) -> Tuple[List[str], Dict[str, int], Dict[str, bytes]]:
    """Parse a compiled terminfo binary file.

    Returns (bool_caps, num_caps, str_caps) for a jinxed terminfo module.
    """
    with open(path, 'rb') as termfile:
        data = termfile.read()

    if len(data) < 12:
        raise ValueError(f'File too short: {len(data)} bytes')

    magic = struct.unpack_from('<H', data, 0)[0]
    if magic in (0o432, 0x1A):
        endian = '<'
    elif magic in (0o436, 0x1E):
        endian = '>'
    else:
        raise ValueError(f'Bad magic: 0x{magic:04x}')

    _, name_size, bool_count, num_count, str_count, str_table_size = \
        struct.unpack_from(f'{endian}6H', data, 0)

    offset = 12 + name_size

    bool_caps: List[str] = []
    for idx in range(min(bool_count, len(_BOOL_NAMES))):
        if offset < len(data) and data[offset] == 1:
            bool_caps.append(_BOOL_NAMES[idx])
        offset += 1
    # Skip any extra boolean entries beyond our known list
    if bool_count > len(_BOOL_NAMES):
        offset += bool_count - len(_BOOL_NAMES)

    num_caps: Dict[str, int] = OrderedDict()
    for idx in range(min(num_count, len(_NUM_NAMES))):
        if offset + 2 <= len(data):
            value = struct.unpack_from(f'{endian}h', data, offset)[0]
            if value >= 0:
                num_caps[_NUM_NAMES[idx]] = value
            offset += 2
    if num_count > len(_NUM_NAMES):
        offset += 2 * (num_count - len(_NUM_NAMES))

    str_offsets: List[int] = []
    for _ in range(str_count):
        if offset + 2 <= len(data):
            value = struct.unpack_from(f'{endian}h', data, offset)[0]
            str_offsets.append(value)
            offset += 2

    str_table_start = offset

    str_caps: Dict[str, bytes] = OrderedDict()
    for idx, str_offset in enumerate(str_offsets):
        if str_offset < 0:
            continue
        if idx >= len(_STR_NAMES):
            break
        null_pos = data.find(b'\x00', str_table_start + str_offset)
        if null_pos == -1:
            null_pos = len(data)
        value = data[str_table_start + str_offset:null_pos]
        if value:
            str_caps[_STR_NAMES[idx]] = value

    return bool_caps, num_caps, str_caps
