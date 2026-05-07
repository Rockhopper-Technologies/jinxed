"""
ansi terminal info

Derived from Revision: 1.1198
Source: https://invisible-mirror.net/archives/ncurses/current/terminfo.src.gz

jquast: added capabilities commonly available in 1980s-1990s terminal emulator programs (like
minicom, telix, etc), but absent from the ANSI X3.64 standard: sc (save_cursor), rc
(restore_cursor), civis (cursor_invisible), cnorm (cursor_normal).

This file is derived from the ncurses terminfo database, which is distributed under the MIT/X11
license.  See LICENSE.ncurses.
"""

# flake8: noqa: E501
# pylint: disable=line-too-long

BOOL_CAPS = [
    'am',      # (auto_right_margin) terminal has automatic margins
    'mc5i',    # (prtr_silent) printer will not echo on screen
    'mir',     # (move_insert_mode) safe to move while in insert mode
    'msgr',    # (move_standout_mode) safe to move while in standout mode
]

NUM_CAPS = {
    'colors': 8,    # (max_colors) maximum number of colors on screen
    'cols': 80,     # (columns) number of columns in a line
    'it': 8,        # (init_tabs) tabs initially every # spaces
    'lines': 24,    # (lines) number of lines on screen or page
    'ncv': 3,       # (no_color_video) video attributes that cannot be used with colors
    'pairs': 64,    # (max_pairs) maximum number of color-pairs on the screen
}

STR_CAPS = {
    'acsc': b'+\x10,\x11-\x18.\x190\xdb`\x04a\xb1f\xf8g\xf1h\xb0j\xd9k\xbfl\xdam\xc0n\xc5o~p\xc4q\xc4r\xc4s_t\xc3u\xb4v\xc1w\xc2x\xb3y\xf3z\xf2{\xe3|\xd8}\x9c~\xfe',
    'bel': b'\a',
    'blink': b'\x1b[5m',
    'bold': b'\x1b[1m',
    'cbt': b'\x1b[Z',
    'clear': b'\x1b[H\x1b[J',
    'civis': b'\x1b[?25l',
    'cnorm': b'\x1b[?25h',
    'cr': b'\r',
    'cub': b'\x1b[%p1%dD',
    'cub1': b'\x1b[D',
    'cud': b'\x1b[%p1%dB',
    'cud1': b'\x1b[B',
    'cuf': b'\x1b[%p1%dC',
    'cuf1': b'\x1b[C',
    'cup': b'\x1b[%i%p1%d;%p2%dH',
    'cuu': b'\x1b[%p1%dA',
    'cuu1': b'\x1b[A',
    'dch': b'\x1b[%p1%dP',
    'dch1': b'\x1b[P',
    'dl': b'\x1b[%p1%dM',
    'dl1': b'\x1b[M',
    'ech': b'\x1b[%p1%dX',
    'ed': b'\x1b[J',
    'el': b'\x1b[K',
    'el1': b'\x1b[1K',
    'enacs': b'',
    'home': b'\x1b[H',
    'hpa': b'\x1b[%i%p1%dG',
    'ht': b'\x1b[I',
    'hts': b'\x1bH',
    'ich': b'\x1b[%p1%d@',
    'il': b'\x1b[%p1%dL',
    'il1': b'\x1b[L',
    'ind': b'\n',
    'indn': b'\x1b[%p1%dS',
    'invis': b'\x1b[8m',
    'kbs': b'\b',
    'kcbt': b'\x1b[Z',
    'kcub1': b'\x1b[D',
    'kcud1': b'\x1b[B',
    'kcuf1': b'\x1b[C',
    'kcuu1': b'\x1b[A',
    'khome': b'\x1b[H',
    'kich1': b'\x1b[L',
    'mc4': b'\x1b[4i',
    'mc5': b'\x1b[5i',
    'nel': b'\r\x1b[S',
    'op': b'\x1b[39;49m',
    'rep': b'%p1%c\x1b[%p2%{1}%-%db',
    'rc': b'\x1b[u',
    'rev': b'\x1b[7m',
    'rin': b'\x1b[%p1%dT',
    'rmacs': b'',
    'rmpch': b'\x1b[10m',
    'rmso': b'\x1b[m',
    'rmul': b'\x1b[m',
    's0ds': b'',
    's1ds': b'',
    's2ds': b'\x1b*B',
    's3ds': b'\x1b+B',
    'setab': b'\x1b[4%p1%dm',
    'setaf': b'\x1b[3%p1%dm',
    'sgr': b'\x1b[0;10%?%p1%t;7%;%?%p2%t;4%;%?%p3%t;7%;%?%p4%t;5%;%?%p6%t;1%;%?%p7%t;8%;%?%p9%t;11%;m',
    'sgr0': b'\x1b[0;10m',
    'sc': b'\x1b[s',
    'smacs': b'',
    'smpch': b'\x1b[11m',
    'smso': b'\x1b[7m',
    'smul': b'\x1b[4m',
    'tbc': b'\x1b[3g',
    'u6': b'\x1b[%i%d;%dR',
    'u7': b'\x1b[6n',
    'u8': b'\x1b[?%[;0123456789]c',
    'u9': b'\x1b[c',
    'vpa': b'\x1b[%i%p1%dd',
}
