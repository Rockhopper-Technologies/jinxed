"""
tmux-256color terminal info

Generated: 2026-05-05T01:35:00.887727+00:00
Source: ncurses terminfo.src 1.1198
        https://invisible-mirror.net/archives/ncurses/current/terminfo.src.gz

This file is derived from the ncurses terminfo database, which is
distributed under the MIT/X11 license.  See LICENSE.ncurses.
"""

from .tmux import BOOL_CAPS, NUM_CAPS, STR_CAPS

BOOL_CAPS = BOOL_CAPS[:]
NUM_CAPS = NUM_CAPS.copy()
STR_CAPS = STR_CAPS.copy()

# Modified/added nums
NUM_CAPS['colors'] = 256
NUM_CAPS['pairs'] = 65536
# Modified strings
STR_CAPS['setab'] = b'\x1b[%?%p1%{8}%<%t4%p1%d%e%p1%{16}%<%t10%p1%{8}%-%d%e48;5;%p1%d%;m'
STR_CAPS['setaf'] = b'\x1b[%?%p1%{8}%<%t3%p1%d%e%p1%{16}%<%t9%p1%{8}%-%d%e38;5;%p1%d%;m'
