"""
vt102 terminal info (derived from vt100)

Revision: 1.1256
Source: https://invisible-mirror.net/archives/ncurses/current/ncurses.tar.gz

This file is derived from the ncurses terminfo database, which is
distributed under the MIT/X11 license.  See LICENSE.ncurses.
"""

# flake8: noqa: E501
# pylint: disable=line-too-long

from .vt100 import BOOL_CAPS, NUM_CAPS, STR_CAPS

BOOL_CAPS = BOOL_CAPS[:]
NUM_CAPS = NUM_CAPS.copy()
STR_CAPS = STR_CAPS.copy()

# Added strings
STR_CAPS['dch1'] = b'\x1b[P'
STR_CAPS['dl1'] = b'\x1b[M'
STR_CAPS['il1'] = b'\x1b[L'
STR_CAPS['rmir'] = b'\x1b[4l'
STR_CAPS['smir'] = b'\x1b[4h'
