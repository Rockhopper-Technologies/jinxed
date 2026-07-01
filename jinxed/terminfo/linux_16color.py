"""
linux-16color terminal info (derived from linux)

Revision: 1.1256
Source: https://invisible-mirror.net/archives/ncurses/current/ncurses.tar.gz

This file is derived from the ncurses terminfo database, which is
distributed under the MIT/X11 license.  See LICENSE.ncurses.
"""

# flake8: noqa: E501
# pylint: disable=line-too-long

from .linux import BOOL_CAPS, NUM_CAPS, STR_CAPS

BOOL_CAPS = BOOL_CAPS[:]
NUM_CAPS = NUM_CAPS.copy()
STR_CAPS = STR_CAPS.copy()
NUM_CAPS['colors'] = 16
NUM_CAPS['ncv'] = 42
NUM_CAPS['pairs'] = 256

# Modified strings
STR_CAPS['setab'] = b'\x1b[4%p1%{8}%m%d%?%p1%{7}%>%t;5%e;25%;m'
STR_CAPS['setaf'] = b'\x1b[3%p1%{8}%m%d%?%p1%{7}%>%t;1%e;22%;m'
