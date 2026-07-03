"""
hpterm terminal info

Revision: 1.1256
Source: https://invisible-mirror.net/archives/ncurses/current/ncurses.tar.gz

This file is derived from the ncurses terminfo database, which is
distributed under the MIT/X11 license.  See LICENSE.ncurses.
"""

# flake8: noqa: E501
# pylint: disable=line-too-long

BOOL_CAPS = [
    'am',     # (auto_right_margin) terminal has automatic margins
    'da',     # (memory_above) display may be retained above the screen
    'db',     # (memory_below) display may be retained below the screen
    'mir',    # (move_insert_mode) safe to move while in insert mode
    'xhp',    # (ceol_standout_glitch) standout not erased by overwriting (hp)
    'xon',    # (xon_xoff) terminal uses xon/xoff handshaking
]

NUM_CAPS = {
    'cols': 80,     # (columns) number of columns in a line
    'lh': 2,        # (label_height) rows in each label
    'lines': 24,    # (lines) number of lines on screen or page
    'lm': 0,        # (lines_of_memory) lines of memory if > line. 0 means varies
    'lw': 8,        # (label_width) columns in each label
    'nlab': 8,      # (num_labels) number of labels on screen
    'pb': 9600,     # (padding_baud_rate) lowest baud rate where padding needed
    'xmc': 0,       # (magic_cookie_glitch) number of blank characters left by smso or rmso
}

STR_CAPS = {
    'bel': b'\a',
    'bold': b'\x1b&dB',
    'cbt': b'\x1bi',
    'clear': b'\x1b&a0y0C\x1bJ',
    'cr': b'\r',
    'cub1': b'\b',
    'cud1': b'\x1bB',
    'cuf1': b'\x1bC',
    'cup': b'\x1b&a%p1%dy%p2%dC',
    'cuu1': b'\x1bA',
    'dch1': b'\x1bP',
    'dim': b'\x1b&dH',
    'dl1': b'\x1bM',
    'ed': b'\x1bJ',
    'el': b'\x1bK',
    'enacs': b'',
    'hpa': b'\x1b&a%p1%dC',
    'ht': b'\t',
    'hts': b'\x1b1',
    'il1': b'\x1bL',
    'ind': b'\n',
    'kbs': b'\b',
    'kclr': b'\x1bJ',
    'kctab': b'\x1b2',
    'kcub1': b'\x1bD',
    'kcud1': b'\x1bB',
    'kcuf1': b'\x1bC',
    'kcuu1': b'\x1bA',
    'kdch1': b'\x1bP',
    'kdl1': b'\x1bM',
    'ked': b'\x1bJ',
    'kel': b'\x1bK',
    'kf1': b'\x1bp',
    'kf2': b'\x1bq',
    'kf3': b'\x1br',
    'kf4': b'\x1bs',
    'kf5': b'\x1bt',
    'kf6': b'\x1bu',
    'kf7': b'\x1bv',
    'kf8': b'\x1bw',
    'khome': b'\x1bh',
    'khts': b'\x1b1',
    'kich1': b'\x1bQ',
    'kil1': b'\x1bL',
    'kind': b'\x1bS',
    'kll': b'\x1bF',
    'knp': b'\x1bU',
    'kpp': b'\x1bV',
    'kri': b'\x1bT',
    'krmir': b'\x1bR',
    'ktbc': b'\x1b3',
    'meml': b'\x1bl',
    'memu': b'\x1bm',
    'pfkey': b'\x1b&f%p1%dk%p2%l%dL%p2%s',
    'pfloc': b'\x1b&f1a%p1%dk%p2%l%dL%p2%s',
    'pfx': b'\x1b&f2a%p1%dk%p2%l%dL%p2%s',
    'pln': b'\x1b&f%p1%dk%p2%l%dd0L%p2%s',
    'rev': b'\x1b&dB',
    'ri': b'\x1bT',
    'rmacs': b'',
    'rmir': b'\x1bR',
    'rmkx': b'\x1b&s0A',
    'rmln': b'\x1b&j@',
    'rmso': b'\x1b&d@',
    'rmul': b'\x1b&d@',
    's0ds': b'',
    's1ds': b'',
    'sgr': b'\x1b&d%?%p7%t%\x27s\x27%c%;%p1%p3%|%p6%|%{2}%*%p2%{4}%*%+%p4%+%p5%{8}%*%+%\x27@\x27%+%c%?%p9%t%\x27\x27%c%e%\x27\x27%c%;',
    'sgr0': b'\x1b&d@',
    'smacs': b'',
    'smir': b'\x1bQ',
    'smkx': b'\x1b&s1A',
    'smln': b'\x1b&jB',
    'smso': b'\x1b&dJ',
    'smul': b'\x1b&dD',
    'tbc': b'\x1b3',
    'vpa': b'\x1b&a%p1%dY',
}
