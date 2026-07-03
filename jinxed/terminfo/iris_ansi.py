"""
iris-ansi terminal info

Revision: 1.1256
Source: https://invisible-mirror.net/archives/ncurses/current/ncurses.tar.gz

This file is derived from the ncurses terminfo database, which is
distributed under the MIT/X11 license.  See LICENSE.ncurses.
"""

# flake8: noqa: E501
# pylint: disable=line-too-long

BOOL_CAPS = [
    'am',    # (auto_right_margin) terminal has automatic margins
]

NUM_CAPS = {
    'cols': 80,     # (columns) number of columns in a line
    'it': 8,        # (init_tabs) tabs initially every # spaces
    'lines': 40,    # (lines) number of lines on screen or page
}

STR_CAPS = {
    'bel': b'\a',
    'bold': b'\x1b[1m',
    'clear': b'\x1b[H\x1b[2J',
    'cnorm': b'\x1b[9/y\x1b[12/y\x1b[=6l',
    'cr': b'\r',
    'cub': b'\x1b[%p1%dD',
    'cub1': b'\x1b[D',
    'cud': b'\x1b[%p1%dB',
    'cud1': b'\n',
    'cuf': b'\x1b[%p1%dC',
    'cuf1': b'\x1b[C',
    'cup': b'\x1b[%i%p1%d;%p2%dH',
    'cuu': b'\x1b[%p1%dA',
    'cuu1': b'\x1b[A',
    'cvvis': b'\x1b[10/y\x1b[=1h\x1b[=2l\x1b[=6h',
    'dl': b'\x1b[%p1%dM',
    'dl1': b'\x1b[M',
    'ed': b'\x1b[J',
    'el': b'\x1b[K',
    'el1': b'\x1b[1K',
    'enacs': b'',
    'home': b'\x1b[H',
    'ht': b'\t',
    'hts': b'\x1bH',
    'il': b'\x1b[%p1%dL',
    'il1': b'\x1b[L',
    'ind': b'\x1bD',
    'is2': b'\x1b[?1l\x1b>\x1b[?7h\x1b[100g\x1b[0m\x1b7\x1b[r\x1b8',
    'kDC': b'\x1b[P',
    'kEND': b'\x1b[147q',
    'kHOM': b'\x1b[143q',
    'kLFT': b'\x1b[158q',
    'kPRT': b'\x1b[210q',
    'kRIT': b'\x1b[167q',
    'kSPD': b'\x1b[218q',
    'kbs': b'\b',
    'kcbt': b'\x1b[Z',
    'kcub1': b'\x1b[D',
    'kcud1': b'\x1b[B',
    'kcuf1': b'\x1b[C',
    'kcuu1': b'\x1b[A',
    'kdch1': b'\x7f',
    'kend': b'\x1b[146q',
    'kent': b'\r',
    'kf1': b'\x1b[001q',
    'kf10': b'\x1b[010q',
    'kf11': b'\x1b[011q',
    'kf12': b'\x1b[012q',
    'kf2': b'\x1b[002q',
    'kf3': b'\x1b[003q',
    'kf4': b'\x1b[004q',
    'kf5': b'\x1b[005q',
    'kf6': b'\x1b[006q',
    'kf7': b'\x1b[007q',
    'kf8': b'\x1b[008q',
    'kf9': b'\x1b[009q',
    'khome': b'\x1b[H',
    'kich1': b'\x1b[139q',
    'knp': b'\x1b[154q',
    'kpp': b'\x1b[150q',
    'kprt': b'\x1b[209q',
    'krmir': b'\x1b[146q',
    'kspd': b'\x1b[217q',
    'nel': b'\x1bE',
    'pfkey': b'\x1bP101;%p1%d.y%p2%s\x1b\x5c',
    'rc': b'\x1b8',
    'rev': b'\x1b[7m',
    'ri': b'\x1bM',
    'rmacs': b'',
    'rmam': b'\x1b[?7l',
    'rmso': b'\x1b[m',
    'rmul': b'\x1b[m',
    's0ds': b'',
    's1ds': b'',
    'sc': b'\x1b7',
    'sgr0': b'\x1b[m',
    'smacs': b'',
    'smam': b'\x1b[?7h',
    'smso': b'\x1b[1;7m',
    'smul': b'\x1b[4m',
    'tbc': b'\x1b[3g',
}
