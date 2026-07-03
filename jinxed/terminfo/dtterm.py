"""
dtterm terminal info

Revision: 1.1256
Source: https://invisible-mirror.net/archives/ncurses/current/ncurses.tar.gz

This file is derived from the ncurses terminfo database, which is
distributed under the MIT/X11 license.  See LICENSE.ncurses.
"""

# flake8: noqa: E501
# pylint: disable=line-too-long

BOOL_CAPS = [
    'am',      # (auto_right_margin) terminal has automatic margins
    'mir',     # (move_insert_mode) safe to move while in insert mode
    'msgr',    # (move_standout_mode) safe to move while in standout mode
    'xenl',    # (eat_newline_glitch) newline ignored after 80 cols (concept)
    'xon',     # (xon_xoff) terminal uses xon/xoff handshaking
    'AX',      # (ansi_x3.64_1979) terminal uses ECMA-48/ANSI X3.64 color sequences
]

NUM_CAPS = {
    'colors': 8,    # (max_colors) maximum number of colors on screen
    'cols': 80,     # (columns) number of columns in a line
    'it': 8,        # (init_tabs) tabs initially every # spaces
    'lines': 24,    # (lines) number of lines on screen or page
    'lm': 0,        # (lines_of_memory) lines of memory if > line. 0 means varies
    'pairs': 64,    # (max_pairs) maximum number of color-pairs on the screen
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
    'dim': b'\x1b[2m',
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
    'il': b'\x1b[%p1%dL',
    'il1': b'\x1b[L',
    'ind': b'\x1bD',
    'invis': b'\x1b[8m',
    'is2': b'\x1b F\x1b>\x1b[?1l\x1b[?7h\x1b[?45l',
    'kbs': b'\b',
    'kcub1': b'\x1b[D',
    'kcud1': b'\x1b[B',
    'kcuf1': b'\x1b[C',
    'kcuu1': b'\x1b[A',
    'kdch1': b'\x1b[3~',
    'kf1': b'\x1b[11~',
    'kf10': b'\x1b[21~',
    'kf11': b'\x1b[23~',
    'kf12': b'\x1b[24~',
    'kf13': b'\x1b[25~',
    'kf14': b'\x1b[26~',
    'kf15': b'\x1b[28~',
    'kf16': b'\x1b[29~',
    'kf17': b'\x1b[31~',
    'kf18': b'\x1b[32~',
    'kf19': b'\x1b[33~',
    'kf2': b'\x1b[12~',
    'kf20': b'\x1b[34~',
    'kf3': b'\x1b[13~',
    'kf4': b'\x1b[14~',
    'kf5': b'\x1b[15~',
    'kf6': b'\x1b[17~',
    'kf7': b'\x1b[18~',
    'kf8': b'\x1b[19~',
    'kf9': b'\x1b[20~',
    'kfnd': b'\x1b[1~',
    'khlp': b'\x1b[28~',
    'kich1': b'\x1b[2~',
    'knp': b'\x1b[6~',
    'kpp': b'\x1b[5~',
    'kslt': b'\x1b[4~',
    'nel': b'\x1bE',
    'op': b'\x1b[39;49m',
    'rc': b'\x1b8',
    'rev': b'\x1b[7m',
    'ri': b'\x1bM',
    'rmacs': b'',
    'rmam': b'\x1b[?7l',
    'rmir': b'\x1b[4l',
    'rmso': b'\x1b[22;27m',
    'rmul': b'\x1b[24m',
    's0ds': b'',
    's1ds': b'',
    'sc': b'\x1b7',
    'setab': b'\x1b[4%p1%dm',
    'setaf': b'\x1b[3%p1%dm',
    'sgr': b'\x1b[0%?%p1%t;2;7%;%?%p2%t;4%;%?%p3%t;7%;%?%p4%t;5%;%?%p5%t;2%;%?%p6%t;1%;%?%p7%t;8%;m',
    'sgr0': b'\x1b[m',
    'smacs': b'',
    'smam': b'\x1b[?7h',
    'smir': b'\x1b[4h',
    'smso': b'\x1b[2;7m',
    'smul': b'\x1b[4m',
    'tbc': b'\x1b[3g',
    'u6': b'\x1b[%i%d;%dR',
    'u7': b'\x1b[6n',
    'u8': b'\x1b[?%[;0123456789]c',
    'u9': b'\x1bZ',
}
