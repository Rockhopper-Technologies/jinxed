"""
vt320 terminal info

Revision: 1.1256
Source: https://invisible-mirror.net/archives/ncurses/current/ncurses.tar.gz

This file is derived from the ncurses terminfo database, which is
distributed under the MIT/X11 license.  See LICENSE.ncurses.
"""

# flake8: noqa: E501
# pylint: disable=line-too-long

BOOL_CAPS = [
    'am',       # (auto_right_margin) terminal has automatic margins
    'eslok',    # (status_line_esc_ok) escape can be used on the status line
    'hs',       # (has_status_line) has extra status line
    'mir',      # (move_insert_mode) safe to move while in insert mode
    'msgr',     # (move_standout_mode) safe to move while in standout mode
    'xenl',     # (eat_newline_glitch) newline ignored after 80 cols (concept)
    'xon',      # (xon_xoff) terminal uses xon/xoff handshaking
]

NUM_CAPS = {
    'cols': 80,     # (columns) number of columns in a line
    'lines': 24,    # (lines) number of lines on screen or page
    'wsl': 80,      # (width_status_line) number of columns in status line
}

STR_CAPS = {
    'acsc': b'``aaffggjjkkllmmnnooppqqrrssttuuvvwwxxyyzz{{||}}~~',
    'bel': b'\a',
    'blink': b'\x1b[5m',
    'bold': b'\x1b[1m',
    'civis': b'\x1b[?25l',
    'clear': b'\x1b[H\x1b[2J',
    'cnorm': b'\x1b[?25h',
    'cr': b'\r',
    'csr': b'\x1b[%i%p1%d;%p2%dr',
    'cub': b'\x1b[%p1%dD',
    'cub1': b'\b',
    'cud': b'\x1b[%p1%dB',
    'cud1': b'\n',
    'cuf': b'\x1b[%p1%dC',
    'cuf1': b'\x1b[C',
    'cup': b'\x1b[%i%p1%d;%p2%dH',
    'cuu': b'\x1b[%p1%dA',
    'cuu1': b'\x1b[A',
    'dch': b'\x1b[%p1%dP',
    'dch1': b'\x1b[P',
    'dl': b'\x1b[%p1%dM',
    'dl1': b'\x1b[M',
    'dsl': b'\x1b[0$~',
    'ech': b'\x1b[%p1%dX',
    'ed': b'\x1b[J',
    'el': b'\x1b[K',
    'el1': b'\x1b[1K',
    'enacs': b'',
    'fsl': b'\x1b[0$}',
    'home': b'\x1b[H',
    'ht': b'\t',
    'hts': b'\x1bH',
    'ich': b'\x1b[%p1%d@',
    'il': b'\x1b[%p1%dL',
    'il1': b'\x1b[L',
    'ind': b'\x1bD',
    'is2': b'\x1b>\x1b[?3l\x1b[?4l\x1b[?5l\x1b[?7h\x1b[?8h\x1b[1;24r\x1b[24;1H',
    'ka1': b'\x1bOw',
    'ka2': b'\x1bOx',
    'ka3': b'\x1bOy',
    'kb1': b'\x1bOt',
    'kb2': b'\x1bOu',
    'kb3': b'\x1bOv',
    'kbs': b'\x7f',
    'kc1': b'\x1bOq',
    'kc2': b'\x1bOr',
    'kc3': b'\x1bOs',
    'kcub1': b'\x1bOD',
    'kcud1': b'\x1bOB',
    'kcuf1': b'\x1bOC',
    'kcuu1': b'\x1bOA',
    'kdch1': b'\x1b[3~',
    'kel': b'\x1b[4~',
    'kent': b'\x1bOM',
    'kf1': b'\x1bOP',
    'kf10': b'\x1b[21~',
    'kf11': b'\x1b[23~',
    'kf12': b'\x1b[24~',
    'kf13': b'\x1b[25~',
    'kf14': b'\x1b[26~',
    'kf15': b'\x1b[28~',
    'kf16': b'\x1b[29~',
    'kf17': b'\x1b[31~',
    'kf18': b'\x1b[32~',
    'kf19': b'\x1b[33~',
    'kf2': b'\x1bOQ',
    'kf20': b'\x1b[34~',
    'kf3': b'\x1bOR',
    'kf4': b'\x1bOS',
    'kf6': b'\x1b[17~',
    'kf7': b'\x1b[18~',
    'kf8': b'\x1b[19~',
    'kf9': b'\x1b[20~',
    'khome': b'\x1b[1~',
    'kich1': b'\x1b[2~',
    'knp': b'\x1b[6~',
    'knxt': b'\t',
    'kpp': b'\x1b[5~',
    'kprv': b'\x1b[Z',
    'kslt': b'\x1b[4~',
    'mc0': b'\x1b[i',
    'mc4': b'\x1b[?4i',
    'mc5': b'\x1b[?5i',
    'nel': b'\x1bE',
    'rc': b'\x1b8',
    'rev': b'\x1b[7m',
    'rf': b'/usr/share/tabset/vt300',
    'ri': b'\x1bM',
    'rmacs': b'',
    'rmam': b'\x1b[?7l',
    'rmir': b'\x1b[4l',
    'rmkx': b'\x1b[?1l\x1b>',
    'rmso': b'\x1b[m',
    'rmul': b'\x1b[m',
    'rs2': b'\x1b>\x1b[?3l\x1b[?4l\x1b[?5l\x1b[?7h\x1b[?8h\x1b[1;24r\x1b[24;1H',
    's0ds': b'',
    's1ds': b'',
    'sc': b'\x1b7',
    'sgr': b'\x1b[0%?%p6%t;1%;%?%p2%t;4%;%?%p4%t;5%;%?%p1%p3%|%t;7%;m',
    'sgr0': b'\x1b[m',
    'smacs': b'',
    'smam': b'\x1b[?7h',
    'smir': b'\x1b[4h',
    'smkx': b'\x1b[?1h\x1b=',
    'smso': b'\x1b[7m',
    'smul': b'\x1b[4m',
    'tbc': b'\x1b[3g',
    'tsl': b'\x1b[2$~\x1b[1$}\x1b[%i%p1%d`',
    'u6': b'\x1b[%i%d;%dR',
    'u7': b'\x1b[6n',
    'u8': b'\x1b[?%[;0123456789]c',
    'u9': b'\x1b[c',
}
