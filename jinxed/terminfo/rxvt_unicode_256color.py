"""
rxvt-unicode-256color terminal info

Generated: 2026-05-05T00:03:18.503158+00:00
Source: ncurses terminfo.src 1.1198
        https://invisible-mirror.net/archives/ncurses/current/terminfo.src.gz

This file is derived from the ncurses terminfo database, which is
distributed under the MIT/X11 license.  See LICENSE.ncurses.
"""

from .rxvt_unicode import BOOL_CAPS, NUM_CAPS, STR_CAPS

BOOL_CAPS = BOOL_CAPS[:]
NUM_CAPS = NUM_CAPS.copy()
STR_CAPS = STR_CAPS.copy()

# Modified/added nums
NUM_CAPS['colors'] = 256
NUM_CAPS['pairs'] = 32767
