"""
iTerm2.app terminal info

Revision: 1.1247
Source: https://invisible-mirror.net/archives/ncurses/current/ncurses.tar.gz

This file is derived from the ncurses terminfo database, which is
distributed under the MIT/X11 license.  See LICENSE.ncurses.
"""

# flake8: noqa: E501
# pylint: disable=line-too-long

BOOL_CAPS = [
    'am',      # (auto_right_margin) terminal has automatic margins
    'bce',     # (back_color_erase) screen erased with background color
    'hs',      # (has_status_line) has extra status line
    'mir',     # (move_insert_mode) safe to move while in insert mode
    'msgr',    # (move_standout_mode) safe to move while in standout mode
    'npc',     # (no_pad_char) pad character does not exist
    'xenl',    # (eat_newline_glitch) newline ignored after 80 cols (concept)
    'xon',     # (xon_xoff) terminal uses xon/xoff handshaking
]

NUM_CAPS = {
    'colors': 256,     # (max_colors) maximum number of colors on screen
    'cols': 80,        # (columns) number of columns in a line
    'it': 8,           # (init_tabs) tabs initially every # spaces
    'lines': 24,       # (lines) number of lines on screen or page
    'pairs': 65536,    # (max_pairs) maximum number of color-pairs on the screen
    'wsl': 50,         # (width_status_line) number of columns in status line
}

STR_CAPS = {
    'acsc': b'``aaffggjjkkllmmnnooppqqrrssttuuvvwwxxyyzz{{||}}~~',
    'bel': b'\a',
    'blink': b'\x1b[5m',
    'bold': b'\x1b[1m',
    'cbt': b'\x1b[Z',
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
    'dsl': b'\x1b]2;\a',
    'ed': b'\x1b[J',
    'el': b'\x1b[K',
    'el1': b'\x1b[1K',
    'enacs': b'',
    'flash': b'\x1b[?5h\x1b[?5l',
    'fsl': b'\a',
    'home': b'\x1b[H',
    'hpa': b'\x1b[%i%p1%dG',
    'ht': b'\t',
    'hts': b'\x1bH',
    'ich': b'\x1b[%p1%d@',
    'ich1': b'\x1b[@',
    'il': b'\x1b[%p1%dL',
    'il1': b'\x1b[L',
    'ind': b'\n',
    'indn': b'\x1b[%p1%dS',
    'kEND': b'\x1b[1;2F',
    'kHOM': b'\x1b[1;2H',
    'kLFT': b'\x1b[1;2D',
    'kRIT': b'\x1b[1;2C',
    'kbs': b'\x7f',
    'kcbt': b'\x1b[Z',
    'kcub1': b'\x1bOD',
    'kcud1': b'\x1bOB',
    'kcuf1': b'\x1bOC',
    'kcuu1': b'\x1bOA',
    'kdch1': b'\x1b[3~',
    'kend': b'\x1bOF',
    'kf1': b'\x1bOP',
    'kf10': b'\x1b[21~',
    'kf11': b'\x1b[23~',
    'kf12': b'\x1b[24~',
    'kf13': b'\x1b[1;2P',
    'kf14': b'\x1b[1;2Q',
    'kf15': b'\x1b[1;2R',
    'kf16': b'\x1b[1;2S',
    'kf17': b'\x1b[15;2~',
    'kf18': b'\x1b[17;2~',
    'kf19': b'\x1b[18;2~',
    'kf2': b'\x1bOQ',
    'kf20': b'\x1b[19;2~',
    'kf21': b'\x1b[20;2~',
    'kf22': b'\x1b[21;2~',
    'kf23': b'\x1b[23;2~',
    'kf24': b'\x1b[24;2~',
    'kf3': b'\x1bOR',
    'kf4': b'\x1bOS',
    'kf5': b'\x1b[15~',
    'kf6': b'\x1b[17~',
    'kf7': b'\x1b[18~',
    'kf8': b'\x1b[19~',
    'kf9': b'\x1b[20~',
    'khome': b'\x1bOH',
    'kind': b'\x1b[1;2B',
    'kmous': b'\x1b[M',
    'knp': b'\x1b[6~',
    'kpp': b'\x1b[5~',
    'kri': b'\x1b[1;2A',
    'nel': b'\x1bE',
    'op': b'\x1b[39;49m',
    'rc': b'\x1b8',
    'rev': b'\x1b[7m',
    'ri': b'\x1bM',
    'rin': b'\x1b[%p1%dT',
    'ritm': b'\x1b[23m',
    'rmacs': b'',
    'rmam': b'\x1b[?7l',
    'rmcup': b'\x1b[?1049l\x1b[23;0;0t',
    'rmir': b'\x1b[4l',
    'rmkx': b'\x1b[?1l\x1b>',
    'rmso': b'\x1b[27m',
    'rmul': b'\x1b[24m',
    'rs2': b'\x1b[!p\x1b[?3;4l\x1b[4l\x1b>\x1b[?1000l',
    's0ds': b'',
    's1ds': b'',
    'sc': b'\x1b7',
    'setab': b'\x1b[%?%p1%{8}%<%t4%p1%d%e%p1%{16}%<%t10%p1%{8}%-%d%e48;5;%p1%d%;m',
    'setaf': b'\x1b[%?%p1%{8}%<%t3%p1%d%e%p1%{16}%<%t9%p1%{8}%-%d%e38;5;%p1%d%;m',
    'sgr': b'\x1b[0%?%p6%t;1%;%?%p2%t;4%;%?%p1%p3%|%t;7%;%?%p4%t;5%;%?%p5%t;2%;m',
    'sgr0': b'\x1b[m',
    'sitm': b'\x1b[3m',
    'smacs': b'',
    'smam': b'\x1b[?7h',
    'smcup': b'\x1b[?1049h\x1b[22;0;0t',
    'smir': b'\x1b[4h',
    'smkx': b'\x1b[?1h\x1b=',
    'smso': b'\x1b[7m',
    'smul': b'\x1b[4m',
    'tbc': b'\x1b[3g',
    'tsl': b'\x1b]2;',
    'u6': b'\x1b[%i%d;%dR',
    'u7': b'\x1b[6n',
    'u8': b'\x1b[?%[;0123456789]c',
    'u9': b'\x1b[c',
    'vpa': b'\x1b[%i%p1%dd',
}
