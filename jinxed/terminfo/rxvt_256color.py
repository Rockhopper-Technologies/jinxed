"""
rxvt-256color terminal info

Generated: 2026-05-04T21:31:56.636866+00:00
Source: ncurses 6.4.20240113 (hash: c9aac1e1e58b)
"""

from .rxvt import BOOL_CAPS, NUM_CAPS, STR_CAPS

BOOL_CAPS = BOOL_CAPS[:]
NUM_CAPS = NUM_CAPS.copy()
STR_CAPS = STR_CAPS.copy()

# Added bools
BOOL_CAPS.append('ccc')
# Modified/added nums
NUM_CAPS['colors'] = 256
NUM_CAPS['pairs'] = 65536
# Added strings
STR_CAPS['initc'] = b'\x1b]4;%p1%d;rgb:%p2%{255}%*%{1000}%/%2.2X/%p3%{255}%*%{1000}%/%2.2X/%p4%{255}%*%{1000}%/%2.2X\x1b\x5c'
STR_CAPS['oc'] = b'\x1b]104\a'
# Modified strings
STR_CAPS['setab'] = b'\x1b[%?%p1%{8}%<%t4%p1%d%e%p1%{16}%<%t10%p1%{8}%-%d%e48;5;%p1%d%;m'
STR_CAPS['setaf'] = b'\x1b[%?%p1%{8}%<%t3%p1%d%e%p1%{16}%<%t9%p1%{8}%-%d%e38;5;%p1%d%;m'
