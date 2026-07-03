"""
vt220 terminal info

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
    'mir',     # (move_insert_mode) safe to move while in insert mode
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
    'civis': b'\x1b[?25l',
    'clear': b'\x1b[H\x1b[J',
    'cnorm': b'\x1b[?25h',
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
    'dch': b'\x1b[%p1%dP',
    'dch1': b'\x1b[P',
    'dl': b'\x1b[%p1%dM',
    'dl1': b'\x1b[M',
    'ech': b'\x1b[%p1%dX',
    'ed': b'\x1b[J',
    'el': b'\x1b[K',
    'el1': b'\x1b[1K',
    'enacs': b'',
    'flash': b'\x1b[?5h\x1b[?5l',
    'home': b'\x1b[H',
    'ht': b'\t',
    'hts': b'\x1bH',
    'ich': b'\x1b[%p1%d@',
    'if': b'/usr/share/tabset/vt100',
    'il': b'\x1b[%p1%dL',
    'il1': b'\x1b[L',
    'ind': b'\x1bD',
    'is2': b'\x1b[?7h\x1b>\x1b[?1l\x1b F\x1b[?4l',
    'kbs': b'\b',
    'kcub1': b'\x1b[D',
    'kcud1': b'\x1b[B',
    'kcuf1': b'\x1b[C',
    'kcuu1': b'\x1b[A',
    'kdch1': b'\x1b[3~',
    'kf1': b'\x1bOP',
    'kf10': b'\x1b[21~',
    'kf11': b'\x1b[23~',
    'kf12': b'\x1b[24~',
    'kf13': b'\x1b[25~',
    'kf14': b'\x1b[26~',
    'kf17': b'\x1b[31~',
    'kf18': b'\x1b[32~',
    'kf19': b'\x1b[33~',
    'kf2': b'\x1bOQ',
    'kf20': b'\x1b[34~',
    'kf3': b'\x1bOR',
    'kf4': b'\x1bOS',
    'kf6': b'\x1b[17~',
    'kf7': b'\x1b[18~',
    'kf8': b'\x1b[19~',
    'kf9': b'\x1b[20~',
    'kfnd': b'\x1b[1~',
    'khlp': b'\x1b[28~',
    'kich1': b'\x1b[2~',
    'knp': b'\x1b[6~',
    'kpp': b'\x1b[5~',
    'krdo': b'\x1b[29~',
    'kslt': b'\x1b[4~',
    'lf1': b'pf1',
    'lf2': b'pf2',
    'lf3': b'pf3',
    'lf4': b'pf4',
    'mc0': b'\x1b[i',
    'mc4': b'\x1b[4i',
    'mc5': b'\x1b[5i',
    'nel': b'\x1bE',
    'rc': b'\x1b8',
    'rev': b'\x1b[7m',
    'ri': b'\x1bM',
    'rmacs': b'',
    'rmam': b'\x1b[?7l',
    'rmir': b'\x1b[4l',
    'rmso': b'\x1b[27m',
    'rmul': b'\x1b[24m',
    'rs1': b'\x1b[?3l',
    's0ds': b'',
    's1ds': b'',
    'sc': b'\x1b7',
    'sgr': b'\x1b[0%?%p6%t;1%;%?%p2%t;4%;%?%p4%t;5%;%?%p1%p3%|%t;7%;m',
    'sgr0': b'\x1b[m',
    'smacs': b'',
    'smam': b'\x1b[?7h',
    'smir': b'\x1b[4h',
    'smso': b'\x1b[7m',
    'smul': b'\x1b[4m',
    'tbc': b'\x1b[3g',
    'u6': b'\x1b[%i%d;%dR',
    'u7': b'\x1b[6n',
    'u8': b'\x1b[?%[;0123456789]c',
    'u9': b'\x1b[c',
}
