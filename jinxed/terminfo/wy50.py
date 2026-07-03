"""
wy50 terminal info

Revision: 1.1256
Source: https://invisible-mirror.net/archives/ncurses/current/ncurses.tar.gz

This file is derived from the ncurses terminfo database, which is
distributed under the MIT/X11 license.  See LICENSE.ncurses.
"""

# flake8: noqa: E501
# pylint: disable=line-too-long

BOOL_CAPS = [
    'am',      # (auto_right_margin) terminal has automatic margins
    'bw',      # (auto_left_margin) cub1 wraps from column 0 to last column
    'hs',      # (has_status_line) has extra status line
    'mc5i',    # (prtr_silent) printer will not echo on screen
    'mir',     # (move_insert_mode) safe to move while in insert mode
    'msgr',    # (move_standout_mode) safe to move while in standout mode
    'xon',     # (xon_xoff) terminal uses xon/xoff handshaking
]

NUM_CAPS = {
    'cols': 80,     # (columns) number of columns in a line
    'lh': 1,        # (label_height) rows in each label
    'lines': 24,    # (lines) number of lines on screen or page
    'lw': 8,        # (label_width) columns in each label
    'ma': 1,        # (max_attributes) maximum combined attributes terminal can handle
    'nlab': 8,      # (num_labels) number of labels on screen
    'wsl': 45,      # (width_status_line) number of columns in status line
}

STR_CAPS = {
    'acsc': b'a;j5k3l2m1n8q:t4u9v=w0x6',
    'bel': b'\a',
    'cbt': b'\x1bI',
    'civis': b'\x1b`0',
    'clear': b'\x1b+',
    'cnorm': b'\x1b`1',
    'cr': b'\r',
    'cub1': b'\b',
    'cud1': b'\n',
    'cuf1': b'\f',
    'cup': b'\x1b=%p1%\x27 \x27%+%c%p2%\x27 \x27%+%c',
    'cuu1': b'\v',
    'dch1': b'\x1bW',
    'dim': b'\x1b`7\x1b)',
    'dl1': b'\x1bR',
    'dsl': b'\x1bF\r',
    'ed': b'\x1bY',
    'el': b'\x1bT',
    'enacs': b'',
    'flash': b'\x1b`8\x1b`9',
    'fsl': b'\r',
    'home': b'\x1e',
    'ht': b'\t',
    'hts': b'\x1b1',
    'il1': b'\x1bE',
    'ind': b'\n',
    'is1': b'\x1b`:\x1b`9',
    'is2': b'\x14\x1b\x27\x1b(',
    'kF1': b'\x01`\r',
    'kF10': b'\x01i\r',
    'kF11': b'\x01j\r',
    'kF12': b'\x01k\r',
    'kF13': b'\x01l\r',
    'kF14': b'\x01m\r',
    'kF15': b'\x01n\r',
    'kF16': b'\x01o\r',
    'kF2': b'\x01a\r',
    'kF3': b'\x01b\r',
    'kF4': b'\x01c\r',
    'kF5': b'\x01d\r',
    'kF6': b'\x01e\r',
    'kF7': b'\x01f\r',
    'kF8': b'\x01g\r',
    'kF9': b'\x01h\r',
    'kHOM': b'\x1b{',
    'kbs': b'\b',
    'kcbt': b'\x1bI',
    'kcub1': b'\b',
    'kcud1': b'\n',
    'kcuf1': b'\f',
    'kcuu1': b'\v',
    'kdch1': b'\x1bW',
    'kdl1': b'\x1bR',
    'ked': b'\x1bY',
    'kel': b'\x1bT',
    'kent': b'\x1b7',
    'kf1': b'\x01@\r',
    'kf10': b'\x01I\r',
    'kf11': b'\x01J\r',
    'kf12': b'\x01K\r',
    'kf13': b'\x01L\r',
    'kf14': b'\x01M\r',
    'kf15': b'\x01N\r',
    'kf16': b'\x01O\r',
    'kf2': b'\x01A\r',
    'kf3': b'\x01B\r',
    'kf4': b'\x01C\r',
    'kf5': b'\x01D\r',
    'kf6': b'\x01E\r',
    'kf7': b'\x01F\r',
    'kf8': b'\x01G\r',
    'kf9': b'\x01H\r',
    'khome': b'\x1e',
    'kich1': b'\x1bQ',
    'kil1': b'\x1bE',
    'knp': b'\x1bK',
    'kpp': b'\x1bJ',
    'kprt': b'\x1bP',
    'krpl': b'\x1br',
    'll': b'\x1e\v',
    'mc0': b'\x1bP',
    'mc4': b'\x14',
    'mc5': b'\x18',
    'nel': b'\r\n',
    'pfx': b'\x1bz%p1%\x27?\x27%+%c%p2%s\x7f',
    'pln': b'\x1bz%p1%\x27/\x27%+%c%p2%s\r',
    'prot': b'\x1b`7\x1b)',
    'rev': b'\x1b`6\x1b)',
    'ri': b'\x1bj',
    'rmacs': b'',
    'rmir': b'\x1br',
    'rmln': b'\x1bA11',
    'rmso': b'\x1b(',
    's0ds': b'',
    's1ds': b'',
    'sgr': b'%?%p1%p3%|%t\x1b`6\x1b)%e%p5%p8%|%t\x1b`7\x1b)%e\x1b(%;%?%p9%t\x1bH\x02%e\x1bH\x03%;',
    'sgr0': b'\x1b(\x1bH\x03',
    'smacs': b'',
    'smir': b'\x1bq',
    'smln': b'\x1bA10',
    'smso': b'\x1b`6\x1b)',
    'tbc': b'\x1b0',
    'tsl': b'\x1bF',
}
