"""
sun terminal info

Revision: 1.1256
Source: https://invisible-mirror.net/archives/ncurses/current/ncurses.tar.gz

This file is derived from the ncurses terminfo database, which is
distributed under the MIT/X11 license.  See LICENSE.ncurses.
"""

# flake8: noqa: E501
# pylint: disable=line-too-long

BOOL_CAPS = [
    'am',      # (auto_right_margin) terminal has automatic margins
    'km',      # (has_meta_key) Has a meta key (i.e., sets 8th-bit)
    'msgr',    # (move_standout_mode) safe to move while in standout mode
]

NUM_CAPS = {
    'cols': 80,     # (columns) number of columns in a line
    'lines': 34,    # (lines) number of lines on screen or page
}

STR_CAPS = {
    'bel': b'\a',
    'clear': b'\f',
    'cr': b'\r',
    'cub1': b'\b',
    'cud1': b'\n',
    'cuf1': b'\x1b[C',
    'cup': b'\x1b[%i%p1%d;%p2%dH',
    'cuu1': b'\x1b[A',
    'dch': b'\x1b[%p1%dP',
    'dch1': b'\x1b[P',
    'dl': b'\x1b[%p1%dM',
    'dl1': b'\x1b[M',
    'ed': b'\x1b[J',
    'el': b'\x1b[K',
    'enacs': b'',
    'ht': b'\t',
    'ich': b'\x1b[%p1%d@',
    'ich1': b'\x1b[@',
    'il': b'\x1b[%p1%dL',
    'il1': b'\x1b[L',
    'ind': b'\n',
    'kb2': b'\x1b[218z',
    'kbs': b'\b',
    'kcub1': b'\x1b[D',
    'kcud1': b'\x1b[B',
    'kcuf1': b'\x1b[C',
    'kcuu1': b'\x1b[A',
    'kdch1': b'\x7f',
    'kend': b'\x1b[220z',
    'kf1': b'\x1b[224z',
    'kf10': b'\x1b[233z',
    'kf11': b'\x1b[234z',
    'kf12': b'\x1b[235z',
    'kf2': b'\x1b[225z',
    'kf3': b'\x1b[226z',
    'kf4': b'\x1b[227z',
    'kf5': b'\x1b[228z',
    'kf6': b'\x1b[229z',
    'kf7': b'\x1b[230z',
    'kf8': b'\x1b[231z',
    'kf9': b'\x1b[232z',
    'khome': b'\x1b[214z',
    'kich1': b'\x1b[247z',
    'knp': b'\x1b[222z',
    'kopt': b'\x1b[194z',
    'kpp': b'\x1b[216z',
    'kres': b'\x1b[193z',
    'kund': b'\x1b[195z',
    'rev': b'\x1b[7m',
    'rmacs': b'',
    'rmso': b'\x1b[m',
    'rs2': b'\x1b[s',
    's0ds': b'',
    's1ds': b'',
    'sgr': b'\x1b[0%?%p1%p3%|%t;7%;m',
    'sgr0': b'\x1b[m',
    'smacs': b'',
    'smso': b'\x1b[7m',
    'u8': b'\x1b[1t',
    'u9': b'\x1b[11t',
}
