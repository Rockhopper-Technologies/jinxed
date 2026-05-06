"""
rio terminal info (derived from alacritty)

Revision: 1.1198 
Source: ncurses terminfo.src
        https://invisible-mirror.net/archives/ncurses/current/terminfo.src.gz

This file is derived from the ncurses terminfo database, which is
distributed under the MIT/X11 license.  See LICENSE.ncurses.
"""

from .alacritty import BOOL_CAPS, NUM_CAPS, STR_CAPS

BOOL_CAPS = BOOL_CAPS[:]
NUM_CAPS = NUM_CAPS.copy()
STR_CAPS = STR_CAPS.copy()
