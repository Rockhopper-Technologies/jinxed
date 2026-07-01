"""
screen terminal info

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
    'mir',     # (move_insert_mode) safe to move while in insert mode
    'msgr',    # (move_standout_mode) safe to move while in standout mode
    'xenl',    # (eat_newline_glitch) newline ignored after 80 cols (concept)
    'AX',      # (ansi_x3.64_1979) terminal uses ECMA-48/ANSI X3.64 color sequences
]

NUM_CAPS = {
    'U8': 1,        # (utf8_terminal) ncurses uses Unicode values for line-drawing in UTF-8 locale
    'colors': 8,    # (max_colors) maximum number of colors on screen
    'cols': 80,     # (columns) number of columns in a line
    'it': 8,        # (init_tabs) tabs initially every # spaces
    'lines': 24,    # (lines) number of lines on screen or page
    'pairs': 64,    # (max_pairs) maximum number of color-pairs on the screen
}

STR_CAPS = {
    'BD': b'\x1b[?2004l',
    'BE': b'\x1b[?2004h',
    'PE': b'\x1b[201~',
    'PS': b'\x1b[200~',
    'S0': b'\x1b(%p1%c',
    'acsc': b'++,,--..00``aaffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz{{||}}~~',
    'bel': b'\a',
    'blink': b'\x1b[5m',
    'bold': b'\x1b[1m',
    'cbt': b'\x1b[Z',
    'civis': b'\x1b[?25l',
    'clear': b'\x1b[H\x1b[J',
    'cnorm': b'\x1b[34h\x1b[?25h',
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
    'cvvis': b'\x1b[34l',
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
    'flash': b'\x1bg',
    'home': b'\x1b[H',
    'hpa': b'\x1b[%i%p1%dG',
    'ht': b'\t',
    'hts': b'\x1bH',
    'ich': b'\x1b[%p1%d@',
    'il': b'\x1b[%p1%dL',
    'il1': b'\x1b[L',
    'ind': b'\n',
    'indn': b'\x1b[%p1%dS',
    'kbs': b'\x7f',
    'kcbt': b'\x1b[Z',
    'kcub1': b'\x1bOD',
    'kcud1': b'\x1bOB',
    'kcuf1': b'\x1bOC',
    'kcuu1': b'\x1bOA',
    'kdch1': b'\x1b[3~',
    'kend': b'\x1b[4~',
    'kf1': b'\x1bOP',
    'kf10': b'\x1b[21~',
    'kf11': b'\x1b[23~',
    'kf12': b'\x1b[24~',
    'kf2': b'\x1bOQ',
    'kf3': b'\x1bOR',
    'kf4': b'\x1bOS',
    'kf5': b'\x1b[15~',
    'kf6': b'\x1b[17~',
    'kf7': b'\x1b[18~',
    'kf8': b'\x1b[19~',
    'kf9': b'\x1b[20~',
    'khome': b'\x1b[1~',
    'kich1': b'\x1b[2~',
    'kmous': b'\x1b[M',
    'knp': b'\x1b[6~',
    'kpp': b'\x1b[5~',
    'nel': b'\x1bE',
    'op': b'\x1b[39;49m',
    'rc': b'\x1b8',
    'rev': b'\x1b[7m',
    'ri': b'\x1bM',
    'rin': b'\x1b[%p1%dT',
    'rmacs': b'',
    'rmcup': b'\x1b[?1049l',
    'rmir': b'\x1b[4l',
    'rmkx': b'\x1b[?1l\x1b>',
    'rmso': b'\x1b[23m',
    'rmul': b'\x1b[24m',
    'rs2': b'\x1bc\x1b[?1000l\x1b[?25h',
    's0ds': b'',
    's1ds': b'',
    'sc': b'\x1b7',
    'setab': b'\x1b[4%p1%dm',
    'setaf': b'\x1b[3%p1%dm',
    'sgr': b'\x1b[0%?%p6%t;1%;%?%p1%t;3%;%?%p2%t;4%;%?%p3%t;7%;%?%p4%t;5%;%?%p5%t;2%;m',
    'sgr0': b'\x1b[m',
    'smacs': b'',
    'smcup': b'\x1b[?1049h',
    'smir': b'\x1b[4h',
    'smkx': b'\x1b[?1h\x1b=',
    'smso': b'\x1b[3m',
    'smul': b'\x1b[4m',
    'tbc': b'\x1b[3g',
    'u6': b'\x1b[%i%d;%dR',
    'u7': b'\x1b[6n',
    'u8': b'\x1b[?1;2c',
    'u9': b'\x1b[c',
    'vpa': b'\x1b[%i%p1%dd',
}
