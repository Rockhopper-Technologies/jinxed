"""
putty-256color terminal info (derived from putty)

Revision: 1.1256
Source: https://invisible-mirror.net/archives/ncurses/current/ncurses.tar.gz

This file is derived from the ncurses terminfo database, which is
distributed under the MIT/X11 license.  See LICENSE.ncurses.
"""

# flake8: noqa: E501
# pylint: disable=line-too-long

from .putty import BOOL_CAPS, NUM_CAPS, STR_CAPS

BOOL_CAPS = BOOL_CAPS[:]
NUM_CAPS = NUM_CAPS.copy()
STR_CAPS = STR_CAPS.copy()
BOOL_CAPS.remove('ccc')  # noqa
NUM_CAPS['colors'] = 256
NUM_CAPS['pairs'] = 65536

# Removed strings
del STR_CAPS['initc']

# Modified strings
STR_CAPS['setab'] = b'\x1b[%?%p1%{8}%<%t4%p1%d%e%p1%{16}%<%t10%p1%{8}%-%d%e48;5;%p1%d%;m'
STR_CAPS['setaf'] = b'\x1b[%?%p1%{8}%<%t3%p1%d%e%p1%{16}%<%t9%p1%{8}%-%d%e38;5;%p1%d%;m'
