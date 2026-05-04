"""
rxvt-unicode-256color terminal info

Generated: 2026-05-04T21:31:56.636866+00:00
Source: ncurses 6.4.20240113 (hash: c9aac1e1e58b)
"""

from .rxvt_unicode import BOOL_CAPS, NUM_CAPS, STR_CAPS

BOOL_CAPS = BOOL_CAPS[:]
NUM_CAPS = NUM_CAPS.copy()
STR_CAPS = STR_CAPS.copy()

# Modified/added nums
NUM_CAPS['colors'] = 256
NUM_CAPS['pairs'] = 32767
