"""
vt100 terminal info

Revision: 1.1256
Source: https://invisible-mirror.net/archives/ncurses/current/ncurses.tar.gz

This file is derived from the ncurses terminfo database, which is
distributed under the MIT/X11 license.  See LICENSE.ncurses.
"""

# flake8: noqa: E501
# pylint: disable=line-too-long

BOOL_CAPS = [
    'am',      # (auto_right_margin) terminal has automatic margins
    'mc5i',    # (prtr_silent) printer will not echo on screen
    'msgr',    # (move_standout_mode) safe to move while in standout mode
    'xenl',    # (eat_newline_glitch) newline ignored after 80 cols (concept)
    'xon',     # (xon_xoff) terminal uses xon/xoff handshaking
]

NUM_CAPS = {
    'cols': 80,     # (columns) number of columns in a line
    'it': 8,        # (init_tabs) tabs initially every # spaces
    'lines': 24,    # (lines) number of lines on screen or page
    'vt': 3,        # (virtual_terminal) virtual terminal number (CB/unix)
}

STR_CAPS = {
    'acsc': b'``aaffggjjkkllmmnnooppqqrrssttuuvvwwxxyyzz{{||}}~~',
    'bel': b'\a',
    'blink': b'\x1b[5m',
    'bold': b'\x1b[1m',
    'clear': b'\x1b[H\x1b[J',
    'cr': b'\r',
    'csr': b'\x1b[%i%p1%d;%p2%dr',
    'cub': b'\x1b[%p1%dD',
    'cub1': b'\b',
    'cud': b'\x1b[%p1%dB',
    'cud1': b'\n',
    'cuf': b'\x1b[%p1%dC',
    'cuf1': b'\x1b[C',
    'cup': b'\x1b[%i%p1%d;%p2%dH',
    'cuu': b'\x1b[%p1%dA',
    'cuu1': b'\x1b[A',
    'ed': b'\x1b[J',
    'el': b'\x1b[K',
    'el1': b'\x1b[1K',
    'enacs': b'',
    'home': b'\x1b[H',
    'ht': b'\t',
    'hts': b'\x1bH',
    'ind': b'\n',
    'ka1': b'\x1bOq',
    'ka3': b'\x1bOs',
    'kb2': b'\x1bOr',
    'kbs': b'\b',
    'kc1': b'\x1bOp',
    'kc3': b'\x1bOn',
    'kcub1': b'\x1bOD',
    'kcud1': b'\x1bOB',
    'kcuf1': b'\x1bOC',
    'kcuu1': b'\x1bOA',
    'kent': b'\x1bOM',
    'kf0': b'\x1bOy',
    'kf1': b'\x1bOP',
    'kf10': b'\x1bOx',
    'kf2': b'\x1bOQ',
    'kf3': b'\x1bOR',
    'kf4': b'\x1bOS',
    'kf5': b'\x1bOt',
    'kf6': b'\x1bOu',
    'kf7': b'\x1bOv',
    'kf8': b'\x1bOl',
    'kf9': b'\x1bOw',
    'lf1': b'pf1',
    'lf2': b'pf2',
    'lf3': b'pf3',
    'lf4': b'pf4',
    'mc0': b'\x1b[0i',
    'mc4': b'\x1b[4i',
    'mc5': b'\x1b[5i',
    'rc': b'\x1b8',
    'rev': b'\x1b[7m',
    'ri': b'\x1bM',
    'rmacs': b'',
    'rmam': b'\x1b[?7l',
    'rmkx': b'\x1b[?1l\x1b>',
    'rmso': b'\x1b[m',
    'rmul': b'\x1b[m',
    'rs2': b'\x1b<\x1b>\x1b[?3;4;5l\x1b[?7;8h\x1b[r',
    's0ds': b'',
    's1ds': b'',
    'sc': b'\x1b7',
    'sgr': b'\x1b[0%?%p1%p6%|%t;1%;%?%p2%t;4%;%?%p1%p3%|%t;7%;%?%p4%t;5%;m',
    'sgr0': b'\x1b[m',
    'smacs': b'',
    'smam': b'\x1b[?7h',
    'smkx': b'\x1b[?1h\x1b=',
    'smso': b'\x1b[7m',
    'smul': b'\x1b[4m',
    'tbc': b'\x1b[3g',
    'u6': b'\x1b[%i%d;%dR',
    'u7': b'\x1b[6n',
    'u8': b'\x1b[?%[;0123456789]c',
    'u9': b'\x1bZ',
}
