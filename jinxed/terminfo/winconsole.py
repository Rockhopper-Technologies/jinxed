"""
winconsole terminal info

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
    'it': 8,        # (init_tabs) tabs initially every # spaces
    'pairs': 64,    # (max_pairs) maximum number of color-pairs on the screen
}

STR_CAPS = {
    'acsc': b'++,,--..00``aaffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz~~',
    'bel': b'\a',
    'bold': b'\x1b[1m',
    'cbt': b'\x1b[Z',
    'civis': b'\x1b[?25l',
    'clear': b'\x1b[H\x1b[J',
    'cnorm': b'\x1b[?25h',
    'cr': b'\r',
    'csr': b'\x1b[%i%p1%d;%p2%dr',
    'cub': b'\x1b[%p1%dD',
    'cub1': b'\x1b[D',
    'cud': b'\x1b[%p1%dB',
    'cud1': b'\x1b[B',
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
    'el1': b'\x1b[0K',
    'enacs': b'',
    'home': b'\x1b[H',
    'ht': b'\t',
    'hts': b'\x1bH',
    'ich': b'\x1b[%p1%d@',
    'il': b'\x1b[%p1%dL',
    'il1': b'\x1b[L',
    'ind': b'\n',
    'indn': b'\x1b[%p1%dS',
    'is1': b'\x1b[!p',
    'kbs': b'\b',
    'kcub1': b'\x1b[D',
    'kcud1': b'\x1b[B',
    'kcuf1': b'\x1b[C',
    'kcuu1': b'\x1b[A',
    'kdch1': b'\x1b[3~',
    'kend': b'\x1b[4~',
    'kf1': b'\x1b[11~',
    'kf10': b'\x1b[21~',
    'kf11': b'\x1b[23~',
    'kf12': b'\x1b[24~',
    'kf13': b'\x1b[11;2~',
    'kf14': b'\x1b[12;2~',
    'kf15': b'\x1b[13;2~',
    'kf16': b'\x1b[14;2~',
    'kf17': b'\x1b[15;2~',
    'kf18': b'\x1b[17;2~',
    'kf19': b'\x1b[18;2~',
    'kf2': b'\x1b[12~',
    'kf20': b'\x1b[19;2~',
    'kf21': b'\x1b[20;2~',
    'kf22': b'\x1b[21;2~',
    'kf23': b'\x1b[24;2~',
    'kf24': b'\x1b[25;2~',
    'kf25': b'\x1b[11;3~',
    'kf26': b'\x1b[12;3~',
    'kf27': b'\x1b[13;3~',
    'kf28': b'\x1b[14;3~',
    'kf29': b'\x1b[15;3~',
    'kf3': b'\x1b[13~',
    'kf30': b'\x1b[17;3~',
    'kf31': b'\x1b[18;3~',
    'kf32': b'\x1b[19;3~',
    'kf33': b'\x1b[20;3~',
    'kf34': b'\x1b[21;3~',
    'kf35': b'\x1b[24;3~',
    'kf36': b'\x1b[25;3~',
    'kf37': b'\x1b[11;4~',
    'kf38': b'\x1b[12;4~',
    'kf39': b'\x1b[13;4~',
    'kf4': b'\x1b[14~',
    'kf40': b'\x1b[14;4~',
    'kf41': b'\x1b[15;4~',
    'kf42': b'\x1b[17;4~',
    'kf43': b'\x1b[18;4~',
    'kf44': b'\x1b[19;4~',
    'kf45': b'\x1b[20;4~',
    'kf46': b'\x1b[21;4~',
    'kf47': b'\x1b[24;4~',
    'kf48': b'\x1b[25;4~',
    'kf49': b'\x1b[11;7~',
    'kf5': b'\x1b[15~',
    'kf50': b'\x1b[12;7~',
    'kf51': b'\x1b[13;7~',
    'kf52': b'\x1b[14;7~',
    'kf53': b'\x1b[15;7~',
    'kf54': b'\x1b[17;7~',
    'kf55': b'\x1b[18;7~',
    'kf56': b'\x1b[19;7~',
    'kf57': b'\x1b[20;7~',
    'kf58': b'\x1b[21;7~',
    'kf59': b'\x1b[24;7~',
    'kf6': b'\x1b[17~',
    'kf60': b'\x1b[25;7~',
    'kf7': b'\x1b[18~',
    'kf8': b'\x1b[19~',
    'kf9': b'\x1b[20~',
    'khome': b'\x1b[1~',
    'kich1': b'\x1b[2~',
    'knp': b'\x1b[6~',
    'kpp': b'\x1b[5~',
    'nel': b'\r\n',
    'op': b'\x1b[39;49m',
    'rc': b'\x1b8',
    'rev': b'\x1b[7m',
    'ri': b'\x1b[T',
    'rin': b'\x1b[%p1%dT',
    'rmacs': b'',
    'rmso': b'\x1b[27m',
    'rmul': b'\x1b[24m',
    'rs1': b'\x1b[!p',
    's0ds': b'',
    's1ds': b'',
    'sc': b'\x1b7',
    'setab': b'\x1b[4%p1%dm',
    'setaf': b'\x1b[3%p1%dm',
    'sgr': b'\x1b[0%?%p1%p6%|%t;1%;%?%p2%t;4%;%?%p1%p3%|%t;7%;m',
    'sgr0': b'\x1b[0m',
    'smacs': b'',
    'smso': b'\x1b[7m',
    'smul': b'\x1b[4m',
    'tbc': b'\x1b[3g',
}
