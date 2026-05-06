"""
Windows 10 virtual terminal codes

Information sourced from:
    https://docs.microsoft.com/en-us/windows/console/console-virtual-terminal-sequences

A best effort has been made, but not all information was available
"""

from .xterm_256color import BOOL_CAPS, NUM_CAPS, STR_CAPS

BOOL_CAPS = BOOL_CAPS[:]
NUM_CAPS = NUM_CAPS.copy()
STR_CAPS = STR_CAPS.copy()
STR_CAPS['enacs'] = b''  # empty (G0/SO/SI stripped)
STR_CAPS['rmacs'] = b''  # empty (G0/SO/SI stripped)
STR_CAPS['s0ds'] = b''  # empty (G0/SO/SI stripped)
STR_CAPS['s1ds'] = b''  # empty (G0/SO/SI stripped)
STR_CAPS['smacs'] = b''  # empty (G0/SO/SI stripped)


# Added
STR_CAPS['cht'] = b'\x1b[%p1%dI'
STR_CAPS['cnl'] = b'\x1b[%p1%dE'
STR_CAPS['cpl'] = b'\x1b[%p1%dF'
STR_CAPS['hvp'] = b'\x1b[%i%p1%d;%p2%df'  # Same as cup
STR_CAPS['ka1'] = b'\x1bOH'   # upper left of keypad
STR_CAPS['ka3'] = b'\x1b[5~'   # upper right of keypad
STR_CAPS['setb'] = b'\x1b[48;5;%p1%dm'
STR_CAPS['setf'] = b'\x1b[38;5;%p1%dm'

# Removed - These do not appear to be supported
for _drop in ('blink', 'dim', 'flash', 'invis', 'kmous', 'meml', 'memu',
              'ritm', 'rmam', 'rmir', 'rmm', 'sitm', 'smam', 'smir', 'smm'):
    STR_CAPS.pop(_drop, None)

# Modified
NUM_CAPS['colors'] = 256
NUM_CAPS['cols'] = 120
NUM_CAPS['lines'] = 30
NUM_CAPS['pairs'] = 65536
STR_CAPS['cbt'] = b'\x1b[%p1%dZ'
STR_CAPS['csr'] = b'\x1b[%p1%{1}%+%d;%?%p2%t%p2%{1}%+%dr'
STR_CAPS['cub1'] = b'\x1b[D'
STR_CAPS['cud1'] = b'\x1b[B'
STR_CAPS['cvvis'] = b'\x1b[?25h'
STR_CAPS['initc'] = b'\x1b]4;%p1%d;rgb] =%p2%d/%p3%d/%p4%d\x1b'
STR_CAPS['is2'] = b'\x1b[!p\x1b>'
STR_CAPS['kbs'] = b'\x7f'
STR_CAPS['kc1'] = b'\x1bOF'   # lower left of keypad
STR_CAPS['kc3'] = b'\x1b[6~'   # lower right of keypad
STR_CAPS['kent'] = b'\r'
STR_CAPS['rmcup'] = b'\x1b[?1049l'
STR_CAPS['rs2'] = b'\x1b[!p\x1b>'  # DECSTR
STR_CAPS['sgr'] = b'\x1b[%p1%d%?%p2%t;%p2%d%;%?%p3%t;%p3%d%;%?%p4%t;%p4%d%;%?%p5%t;%p5%d%;' \
                  b'%?%p6%t;%p6%d%;%?%p7%t;%p7%d%;%?%p8%t;%p8%d%;%?%p9%t;%p9%d%;m'
STR_CAPS['smcup'] = b'\x1b[?1049h'
STR_CAPS['u9'] = b'\x1b[0c'
