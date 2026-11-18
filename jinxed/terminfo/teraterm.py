"""
teraterm terminal info

Revision: 1.1283
Source: https://invisible-mirror.net/archives/ncurses/current/ncurses.tar.gz

This file is derived from the ncurses terminfo database, which is
distributed under the MIT/X11 license.  See LICENSE.ncurses.
"""

# flake8: noqa: E501
# pylint: disable=line-too-long

BOOL_CAPS = [
    'am',       # (auto_right_margin) terminal has automatic margins
    'bce',      # (back_color_erase) screen erased with background color
    'eslok',    # (status_line_esc_ok) escape can be used on the status line
    'hs',       # (has_status_line) has extra status line
    'km',       # (has_meta_key) Has a meta key (i.e., sets 8th-bit)
    'mc5i',     # (prtr_silent) printer will not echo on screen
    'msgr',     # (move_standout_mode) safe to move while in standout mode
    'npc',      # (no_pad_char) pad character does not exist
    'xenl',     # (eat_newline_glitch) newline ignored after 80 cols (concept)
    'xon',      # (xon_xoff) terminal uses xon/xoff handshaking
    'AX',       # (ansi_x3.64_1979) terminal uses ECMA-48/ANSI X3.64 color sequences
]

NUM_CAPS = {
    'colors': 8,    # (max_colors) maximum number of colors on screen
    'cols': 80,     # (columns) number of columns in a line
    'it': 8,        # (init_tabs) tabs initially every # spaces
    'lines': 24,    # (lines) number of lines on screen or page
    'ncv': 3,       # (no_color_video) video attributes that cannot be used with colors
    'pairs': 64,    # (max_pairs) maximum number of color-pairs on the screen
}

STR_CAPS = {
    'BD': b'\x1b[?2004l',
    'BE': b'\x1b[?2004h',
    'PE': b'\x1b[201~',
    'PS': b'\x1b[200~',
    'RV': b'\x1b[>c',
    'XM': b'\x1b[?1006;1000%?%p1%{1}%=%th%el%;',
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
    'dsl': b'\x1b[0$~',
    'ech': b'\x1b[%p1%dX',
    'ed': b'\x1b[J',
    'el': b'\x1b[K',
    'el1': b'\x1b[1K',
    'enacs': b'',
    'flash': b'\x1b[?5h\x1b[?5l',
    'fsl': b'\x1b[0$}',
    'home': b'\x1b[H',
    'hpa': b'\x1b[%i%p1%dG',
    'ht': b'\t',
    'hts': b'\x1bH',
    'ich': b'\x1b[%p1%d@',
    'ich1': b'\x1b[@',
    'il': b'\x1b[%p1%dL',
    'il1': b'\x1b[L',
    'ind': b'\n',
    'ka1': b'\x1bOw',
    'ka2': b'\x1bOx',
    'ka3': b'\x1bOy',
    'kb1': b'\x1bOt',
    'kb2': b'\x1bOu',
    'kb3': b'\x1bOv',
    'kbeg': b'\x1bOE',
    'kbs': b'\b',
    'kc1': b'\x1bOq',
    'kc2': b'\x1bOr',
    'kc3': b'\x1bOs',
    'kcub1': b'\x1bOD',
    'kcud1': b'\x1bOB',
    'kcuf1': b'\x1bOC',
    'kcuu1': b'\x1bOA',
    'kdch1': b'\x7f',
    'kent': b'\x1bOM',
    'kf1': b'\x1bOP',
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
    'kf2': b'\x1bOQ',
    'kf20': b'\x1b[34~',
    'kf3': b'\x1bOR',
    'kf4': b'\x1bOS',
    'kf5': b'\x1b[15~',
    'kf6': b'\x1b[17~',
    'kf7': b'\x1b[18~',
    'kf8': b'\x1b[19~',
    'kf9': b'\x1b[20~',
    'kfnd': b'\x1b[1~',
    'kich1': b'\x1b[2~',
    'kmous': b'\x1b[<',
    'knp': b'\x1b[6~',
    'kp5': b'\x1bOE',
    'kpADD': b'\x1bOk',
    'kpCMA': b'\x1bOl',
    'kpDIV': b'\x1bOo',
    'kpDOT': b'\x1bOn',
    'kpMUL': b'\x1bOj',
    'kpSUB': b'\x1bOm',
    'kpZRO': b'\x1bOp',
    'kpp': b'\x1b[5~',
    'kslt': b'\x1b[4~',
    'lf1': b'pf1',
    'lf2': b'pf2',
    'lf3': b'pf3',
    'lf4': b'pf4',
    'mc0': b'\x1b[0i',
    'mc4': b'\x1b[4i',
    'mc5': b'\x1b[5i',
    'op': b'\x1b[39;49m',
    'rc': b'\x1b8',
    'rev': b'\x1b[7m',
    'ri': b'\x1bM',
    'rmacs': b'',
    'rmam': b'\x1b[?7l',
    'rmkx': b'\x1b[?1l\x1b>',
    'rmso': b'\x1b[27m',
    'rmul': b'\x1b[24m',
    'rs2': b'\x1b<\x1b>\x1b[?3;4;5l\x1b[?7;8h\x1b[r',
    'rv': b'\x1b\x5c[>32;331;0c',
    's0ds': b'',
    's1ds': b'',
    'sc': b'\x1b7',
    'setab': b'\x1b[4%p1%dm',
    'setaf': b'\x1b[3%p1%dm',
    'sgr': b'\x1b[0%?%p1%p6%|%t;1%;%?%p2%t;4%;%?%p1%p3%|%t;7%;%?%p4%t;5%;m',
    'sgr0': b'\x1b[0m',
    'smacs': b'',
    'smam': b'\x1b[?7h',
    'smkx': b'\x1b[?1h\x1b=',
    'smso': b'\x1b[7m',
    'smul': b'\x1b[4m',
    'tbc': b'\x1b[3g',
    'tsl': b'\x1b[2$~\x1b[1$}\x1b[%i%p1%d`',
    'u6': b'\x1b[%i%d;%dR',
    'u7': b'\x1b[6n',
    'u8': b'\x1b[?1;2c',
    'u9': b'\x1b[c',
    'vpa': b'\x1b[%i%p1%dd',
    'xm': b'\x1b[<%i%p3%d;%p1%d;%p2%d;%?%p4%tM%em%;',
}
