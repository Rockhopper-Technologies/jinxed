"""
xterm-16color terminal info (derived from xterm-new)

Revision: 1.1256
Source: https://invisible-mirror.net/archives/ncurses/current/ncurses.tar.gz

This file is derived from the ncurses terminfo database, which is
distributed under the MIT/X11 license.  See LICENSE.ncurses.
"""

# flake8: noqa: E501
# pylint: disable=line-too-long

from .xterm_new import BOOL_CAPS, NUM_CAPS, STR_CAPS

BOOL_CAPS = BOOL_CAPS[:]
NUM_CAPS = NUM_CAPS.copy()
STR_CAPS = STR_CAPS.copy()
BOOL_CAPS.append('ccc')
NUM_CAPS['colors'] = 16
NUM_CAPS['pairs'] = 256

# Added strings
STR_CAPS['initc'] = b'\x1b]4;%p1%d;rgb:%p2%{255}%*%{1000}%/%2.2X/%p3%{255}%*%{1000}%/%2.2X/%p4%{255}%*%{1000}%/%2.2X\x1b\x5c'
STR_CAPS['oc'] = b'\x1b]104\a'

# Modified strings
STR_CAPS['rs1'] = b'\x1bc\x1b]104\a'
STR_CAPS['setab'] = b'\x1b[%?%p1%{8}%<%t%p1%\x27(\x27%+%e%p1%{92}%+%;%dm'
STR_CAPS['setaf'] = b'\x1b[%?%p1%{8}%<%t%p1%{30}%+%e%p1%\x27R\x27%+%;%dm'
STR_CAPS['setb'] = b'%p1%{8}%/%{6}%*%{4}%+\x1b[%d%p1%{8}%m%Pa%?%ga%{1}%=%t4%e%ga%{3}%=%t6%e%ga%{4}%=%t1%e%ga%{6}%=%t3%e%ga%d%;m'
STR_CAPS['setf'] = b'%p1%{8}%/%{6}%*%{3}%+\x1b[%d%p1%{8}%m%Pa%?%ga%{1}%=%t4%e%ga%{3}%=%t6%e%ga%{4}%=%t1%e%ga%{6}%=%t3%e%ga%d%;m'
