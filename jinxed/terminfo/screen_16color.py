"""
screen-16color terminal info

Generated: 2026-05-04T21:31:56.636866+00:00
Source: ncurses 6.4.20240113 (hash: c9aac1e1e58b)
"""

from .screen import BOOL_CAPS, NUM_CAPS, STR_CAPS

BOOL_CAPS = BOOL_CAPS[:]
NUM_CAPS = NUM_CAPS.copy()
STR_CAPS = STR_CAPS.copy()

# Modified/added nums
NUM_CAPS['colors'] = 16
NUM_CAPS['pairs'] = 256
# Added strings
STR_CAPS['setb'] = b'%p1%{8}%/%{6}%*%{4}%+\x1b[%d%p1%{8}%m%Pa%?%ga%{1}%=%t4%e%ga%{3}%=%t6%e%ga%{4}%=%t1%e%ga%{6}%=%t3%e%ga%d%;m'
STR_CAPS['setf'] = b'%p1%{8}%/%{6}%*%{3}%+\x1b[%d%p1%{8}%m%Pa%?%ga%{1}%=%t4%e%ga%{3}%=%t6%e%ga%{4}%=%t1%e%ga%{6}%=%t3%e%ga%d%;m'
# Modified strings
STR_CAPS['setab'] = b'\x1b[%?%p1%{8}%<%t%p1%\x27(\x27%+%e%p1%{92}%+%;%dm'
STR_CAPS['setaf'] = b'\x1b[%?%p1%{8}%<%t%p1%{30}%+%e%p1%\x27R\x27%+%;%dm'
