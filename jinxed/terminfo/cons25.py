"""
cons25 terminal info

Revision: 1.1256
Source: https://invisible-mirror.net/archives/ncurses/current/ncurses.tar.gz

This file is derived from the ncurses terminfo database, which is
distributed under the MIT/X11 license.  See LICENSE.ncurses.
"""

# flake8: noqa: E501
# pylint: disable=line-too-long

BOOL_CAPS = [
    'am',      # (auto_right_margin) terminal has automatic margins
    'bce',     # (back_color_erase) screen erased with background color
    'bw',      # (auto_left_margin) cub1 wraps from column 0 to last column
    'eo',      # (erase_overstrike) can erase overstrikes with a blank
    'msgr',    # (move_standout_mode) safe to move while in standout mode
    'npc',     # (no_pad_char) pad character does not exist
]

NUM_CAPS = {
    'colors': 8,    # (max_colors) maximum number of colors on screen
    'cols': 80,     # (columns) number of columns in a line
    'it': 8,        # (init_tabs) tabs initially every # spaces
    'lines': 25,    # (lines) number of lines on screen or page
    'ncv': 21,      # (no_color_video) video attributes that cannot be used with colors
    'pairs': 64,    # (max_pairs) maximum number of color-pairs on the screen
}

STR_CAPS = {
    'acsc': b'-\x18.\x190\xdb`\x04a\xb0f\xf8g\xf1h\xb1i\x15j\xd9k\xbfl\xdam\xc0n\xc5q\xc4t\xc3u\xb4v\xc1w\xc2x\xb3y\xf3z\xf2~\xf9',
    'bel': b'\a',
    'blink': b'\x1b[5m',
    'bold': b'\x1b[1m',
    'cbt': b'\x1b[Z',
    'clear': b'\x1b[H\x1b[J',
    'cnorm': b'\x1b[=0C',
    'cr': b'\r',
    'cub': b'\x1b[%p1%dD',
    'cub1': b'\b',
    'cud': b'\x1b[%p1%dB',
    'cud1': b'\x1b[B',
    'cuf': b'\x1b[%p1%dC',
    'cuf1': b'\x1b[C',
    'cup': b'\x1b[%i%p1%d;%p2%dH',
    'cuu': b'\x1b[%p1%dA',
    'cuu1': b'\x1b[A',
    'cvvis': b'\x1b[=1C',
    'dch': b'\x1b[%p1%dP',
    'dch1': b'\x1b[P',
    'dim': b'\x1b[30;1m',
    'dl': b'\x1b[%p1%dM',
    'dl1': b'\x1b[M',
    'ech': b'\x1b[%p1%dX',
    'ed': b'\x1b[J',
    'el': b'\x1b[K',
    'enacs': b'',
    'home': b'\x1b[H',
    'hpa': b'\x1b[%i%p1%d`',
    'ht': b'\t',
    'ich': b'\x1b[%p1%d@',
    'ich1': b'\x1b[@',
    'il': b'\x1b[%p1%dL',
    'il1': b'\x1b[L',
    'ind': b'\x1b[S',
    'indn': b'\x1b[%p1%dS',
    'kb2': b'\x1b[E',
    'kbs': b'\b',
    'kcbt': b'\x1b[Z',
    'kcub1': b'\x1b[D',
    'kcud1': b'\x1b[B',
    'kcuf1': b'\x1b[C',
    'kcuu1': b'\x1b[A',
    'kdch1': b'\x7f',
    'kend': b'\x1b[F',
    'kf1': b'\x1b[M',
    'kf10': b'\x1b[V',
    'kf11': b'\x1b[W',
    'kf12': b'\x1b[X',
    'kf13': b'\x1b[Y',
    'kf14': b'\x1b[Z',
    'kf15': b'\x1b[a',
    'kf16': b'\x1b[b',
    'kf17': b'\x1b[c',
    'kf18': b'\x1b[d',
    'kf19': b'\x1b[e',
    'kf2': b'\x1b[N',
    'kf20': b'\x1b[f',
    'kf21': b'\x1b[g',
    'kf22': b'\x1b[h',
    'kf23': b'\x1b[i',
    'kf24': b'\x1b[j',
    'kf25': b'\x1b[k',
    'kf26': b'\x1b[l',
    'kf27': b'\x1b[m',
    'kf28': b'\x1b[n',
    'kf29': b'\x1b[o',
    'kf3': b'\x1b[O',
    'kf30': b'\x1b[p',
    'kf31': b'\x1b[q',
    'kf32': b'\x1b[r',
    'kf33': b'\x1b[s',
    'kf34': b'\x1b[t',
    'kf35': b'\x1b[u',
    'kf36': b'\x1b[v',
    'kf37': b'\x1b[w',
    'kf38': b'\x1b[x',
    'kf39': b'\x1b[y',
    'kf4': b'\x1b[P',
    'kf40': b'\x1b[z',
    'kf41': b'\x1b[@',
    'kf42': b'\x1b[[',
    'kf43': b'\x1b[\x5c',
    'kf44': b'\x1b[]',
    'kf45': b'\x1b[^',
    'kf46': b'\x1b[_',
    'kf47': b'\x1b[`',
    'kf48': b'\x1b[{',
    'kf5': b'\x1b[Q',
    'kf6': b'\x1b[R',
    'kf7': b'\x1b[S',
    'kf8': b'\x1b[T',
    'kf9': b'\x1b[U',
    'khome': b'\x1b[H',
    'kich1': b'\x1b[L',
    'knp': b'\x1b[G',
    'kpp': b'\x1b[I',
    'nel': b'\x1b[E',
    'op': b'\x1b[x',
    'rc': b'\x1b8',
    'rev': b'\x1b[7m',
    'ri': b'\x1b[T',
    'rin': b'\x1b[%p1%dT',
    'rmacs': b'',
    'rmso': b'\x1b[m',
    'rs2': b'\x1b[x\x1b[m\x1bc',
    's0ds': b'',
    's1ds': b'',
    'sc': b'\x1b7',
    'setab': b'\x1b[4%p1%dm',
    'setaf': b'\x1b[3%p1%dm',
    'sgr': b'\x1b[0%?%p1%t;2;7%;%?%p3%t;7%;%?%p4%t;5%;%?%p5%t;30;1%;%?%p6%t;1%;m',
    'sgr0': b'\x1b[m',
    'smacs': b'',
    'smso': b'\x1b[7m',
    'vpa': b'\x1b[%i%p1%dd',
}
