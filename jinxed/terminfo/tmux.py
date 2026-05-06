"""
tmux terminal info (derived from screen)

Revision: 1.1198 
Source: ncurses terminfo.src
        https://invisible-mirror.net/archives/ncurses/current/terminfo.src.gz

This file is derived from the ncurses terminfo database, which is
distributed under the MIT/X11 license.  See LICENSE.ncurses.
"""

from .screen import BOOL_CAPS, NUM_CAPS, STR_CAPS

BOOL_CAPS = BOOL_CAPS[:]
NUM_CAPS = NUM_CAPS.copy()
STR_CAPS = STR_CAPS.copy()
BOOL_CAPS.append('hs')

# Added strings
STR_CAPS['dsl'] = b'\x1b]0;\a'
STR_CAPS['fsl'] = b'\a'
STR_CAPS['invis'] = b'\x1b[8m'
STR_CAPS['kDC'] = b'\x1b[3;2~'
STR_CAPS['kEND'] = b'\x1b[1;2F'
STR_CAPS['kHOM'] = b'\x1b[1;2H'
STR_CAPS['kIC'] = b'\x1b[2;2~'
STR_CAPS['kLFT'] = b'\x1b[1;2D'
STR_CAPS['kNXT'] = b'\x1b[6;2~'
STR_CAPS['kPRV'] = b'\x1b[5;2~'
STR_CAPS['kRIT'] = b'\x1b[1;2C'
STR_CAPS['kf13'] = b'\x1b[1;2P'
STR_CAPS['kf14'] = b'\x1b[1;2Q'
STR_CAPS['kf15'] = b'\x1b[1;2R'
STR_CAPS['kf16'] = b'\x1b[1;2S'
STR_CAPS['kf17'] = b'\x1b[15;2~'
STR_CAPS['kf18'] = b'\x1b[17;2~'
STR_CAPS['kf19'] = b'\x1b[18;2~'
STR_CAPS['kf20'] = b'\x1b[19;2~'
STR_CAPS['kf21'] = b'\x1b[20;2~'
STR_CAPS['kf22'] = b'\x1b[21;2~'
STR_CAPS['kf23'] = b'\x1b[23;2~'
STR_CAPS['kf24'] = b'\x1b[24;2~'
STR_CAPS['kf25'] = b'\x1b[1;5P'
STR_CAPS['kf26'] = b'\x1b[1;5Q'
STR_CAPS['kf27'] = b'\x1b[1;5R'
STR_CAPS['kf28'] = b'\x1b[1;5S'
STR_CAPS['kf29'] = b'\x1b[15;5~'
STR_CAPS['kf30'] = b'\x1b[17;5~'
STR_CAPS['kf31'] = b'\x1b[18;5~'
STR_CAPS['kf32'] = b'\x1b[19;5~'
STR_CAPS['kf33'] = b'\x1b[20;5~'
STR_CAPS['kf34'] = b'\x1b[21;5~'
STR_CAPS['kf35'] = b'\x1b[23;5~'
STR_CAPS['kf36'] = b'\x1b[24;5~'
STR_CAPS['kf37'] = b'\x1b[1;6P'
STR_CAPS['kf38'] = b'\x1b[1;6Q'
STR_CAPS['kf39'] = b'\x1b[1;6R'
STR_CAPS['kf40'] = b'\x1b[1;6S'
STR_CAPS['kf41'] = b'\x1b[15;6~'
STR_CAPS['kf42'] = b'\x1b[17;6~'
STR_CAPS['kf43'] = b'\x1b[18;6~'
STR_CAPS['kf44'] = b'\x1b[19;6~'
STR_CAPS['kf45'] = b'\x1b[20;6~'
STR_CAPS['kf46'] = b'\x1b[21;6~'
STR_CAPS['kf47'] = b'\x1b[23;6~'
STR_CAPS['kf48'] = b'\x1b[24;6~'
STR_CAPS['kf49'] = b'\x1b[1;3P'
STR_CAPS['kf50'] = b'\x1b[1;3Q'
STR_CAPS['kf51'] = b'\x1b[1;3R'
STR_CAPS['kf52'] = b'\x1b[1;3S'
STR_CAPS['kf53'] = b'\x1b[15;3~'
STR_CAPS['kf54'] = b'\x1b[17;3~'
STR_CAPS['kf55'] = b'\x1b[18;3~'
STR_CAPS['kf56'] = b'\x1b[19;3~'
STR_CAPS['kf57'] = b'\x1b[20;3~'
STR_CAPS['kf58'] = b'\x1b[21;3~'
STR_CAPS['kf59'] = b'\x1b[23;3~'
STR_CAPS['kf60'] = b'\x1b[24;3~'
STR_CAPS['kf61'] = b'\x1b[1;4P'
STR_CAPS['kf62'] = b'\x1b[1;4Q'
STR_CAPS['kf63'] = b'\x1b[1;4R'
STR_CAPS['kind'] = b'\x1b[1;2B'
STR_CAPS['kri'] = b'\x1b[1;2A'
STR_CAPS['ritm'] = b'\x1b[23m'
STR_CAPS['sitm'] = b'\x1b[3m'
STR_CAPS['tsl'] = b'\x1b]0;'

# Modified strings
STR_CAPS['rmso'] = b'\x1b[27m'
STR_CAPS['sgr'] = b'\x1b[0%?%p6%t;1%;%?%p2%t;4%;%?%p1%p3%|%t;7%;%?%p4%t;5%;%?%p5%t;2%;%?%p7%t;8%;m'
STR_CAPS['smso'] = b'\x1b[7m'
