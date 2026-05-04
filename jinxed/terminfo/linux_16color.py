"""
linux-16color terminal info

Generated: 2026-05-04T21:31:56.636866+00:00
Source: ncurses 6.4.20240113 (hash: c9aac1e1e58b)
"""

from .linux import BOOL_CAPS, NUM_CAPS, STR_CAPS

BOOL_CAPS = BOOL_CAPS[:]
NUM_CAPS = NUM_CAPS.copy()
STR_CAPS = STR_CAPS.copy()

# Modified/added nums
NUM_CAPS['colors'] = 16
NUM_CAPS['ncv'] = 42
NUM_CAPS['pairs'] = 256
# Modified strings
STR_CAPS['setab'] = b'\x1b[4%p1%{8}%m%d%?%p1%{7}%>%t;5%e;25%;m'
STR_CAPS['setaf'] = b'\x1b[3%p1%{8}%m%d%?%p1%{7}%>%t;1%e;22%;m'
