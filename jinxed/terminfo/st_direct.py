"""
st-direct terminal info

Generated: 2026-05-04T21:31:56.636866+00:00
Source: ncurses 6.4.20240113 (hash: c9aac1e1e58b)
"""

from .st import BOOL_CAPS, NUM_CAPS, STR_CAPS

BOOL_CAPS = BOOL_CAPS[:]
NUM_CAPS = NUM_CAPS.copy()
STR_CAPS = STR_CAPS.copy()

# Modified/added nums
NUM_CAPS['colors'] = 16777216
NUM_CAPS['pairs'] = 65536
# Removed strings
del STR_CAPS['setb']
del STR_CAPS['setf']
# Modified strings
STR_CAPS['setab'] = b'\x1b[%?%p1%{8}%<%t4%p1%d%e48;2;%p1%{65536}%/%d;%p1%{256}%/%{255}%&%d;%p1%{255}%&%d%;m'
STR_CAPS['setaf'] = b'\x1b[%?%p1%{8}%<%t3%p1%d%e38;2;%p1%{65536}%/%d;%p1%{256}%/%{255}%&%d;%p1%{255}%&%d%;m'
