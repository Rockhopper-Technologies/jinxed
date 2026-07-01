"""
rxvt-unicode-256color terminal info

Revision: 1.1256
Source: https://invisible-mirror.net/archives/ncurses/current/ncurses.tar.gz

This file is derived from the ncurses terminfo database, which is
distributed under the MIT/X11 license.  See LICENSE.ncurses.
"""

# flake8: noqa: E501
# pylint: disable=line-too-long

BOOL_CAPS = [
    'am',      # (auto_right_margin) terminal has automatic margins
    'bce',     # (back_color_erase) screen erased with background color
    'bw',      # (auto_left_margin) cub1 wraps from column 0 to last column
    'ccc',     # (can_change) terminal can re-define existing colors
    'eo',      # (erase_overstrike) can erase overstrikes with a blank
    'hs',      # (has_status_line) has extra status line
    'km',      # (has_meta_key) Has a meta key (i.e., sets 8th-bit)
    'mc5i',    # (prtr_silent) printer will not echo on screen
    'mir',     # (move_insert_mode) safe to move while in insert mode
    'msgr',    # (move_standout_mode) safe to move while in standout mode
    'npc',     # (no_pad_char) pad character does not exist
    'xenl',    # (eat_newline_glitch) newline ignored after 80 cols (concept)
    'xon',     # (xon_xoff) terminal uses xon/xoff handshaking
]

NUM_CAPS = {
    'btns': 5,         # (buttons) number of buttons on mouse
    'colors': 256,     # (max_colors) maximum number of colors on screen
    'cols': 80,        # (columns) number of columns in a line
    'it': 8,           # (init_tabs) tabs initially every # spaces
    'lines': 24,       # (lines) number of lines on screen or page
    'lm': 0,           # (lines_of_memory) lines of memory if > line. 0 means varies
    'ncv': 0,          # (no_color_video) video attributes that cannot be used with colors
    'pairs': 32767,    # (max_pairs) maximum number of color-pairs on the screen
}

STR_CAPS = {
    'acsc': b'+C,D-A.B0E``aaffgghFiGjjkkllmmnnooppqqrrssttuuvvwwxxyyzz{{||}}~~',
    'bel': b'\a',
    'blink': b'\x1b[5m',
    'bold': b'\x1b[1m',
    'civis': b'\x1b[?25l',
    'clear': b'\x1b[H\x1b[2J',
    'cnorm': b'\x1b[?12l\x1b[?25h',
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
    'cvvis': b'\x1b[?12;25h',
    'dch': b'\x1b[%p1%dP',
    'dch1': b'\x1b[P',
    'dl': b'\x1b[%p1%dM',
    'dl1': b'\x1b[M',
    'dsl': b'\x1b]2;\a',
    'ech': b'\x1b[%p1%dX',
    'ed': b'\x1b[J',
    'el': b'\x1b[K',
    'el1': b'\x1b[1K',
    'enacs': b'',
    'flash': b'\x1b[?5h\x1b[?5l',
    'fsl': b'\a',
    'home': b'\x1b[H',
    'hpa': b'\x1b[%i%p1%dG',
    'ht': b'\t',
    'hts': b'\x1bH',
    'ich': b'\x1b[%p1%d@',
    'ich1': b'\x1b[@',
    'il': b'\x1b[%p1%dL',
    'il1': b'\x1b[L',
    'ind': b'\n',
    'indn': b'\x1b[%p1%dS',
    'initc': b'\x1b]4;%p1%d;rgb:%p2%{65535}%*%{1000}%/%4.4X/%p3%{65535}%*%{1000}%/%4.4X/%p4%{65535}%*%{1000}%/%4.4X\x1b\x5c',
    'is1': b'\x1b[!p',
    'is2': b'\x1b[r\x1b[m\x1b[2J\x1b[?7;25h\x1b[?1;3;4;5;6;9;66;1000;1001;1049l\x1b[4l',
    'kDC': b'\x1b[3$',
    'kDC5': b'\x1b[3^',
    'kDC6': b'\x1b[3@',
    'kDN': b'\x1b[b',
    'kDN5': b'\x1bOb',
    'kEND': b'\x1b[8$',
    'kEND5': b'\x1b[8^',
    'kEND6': b'\x1b[8@',
    'kFND': b'\x1b[1$',
    'kFND5': b'\x1b[1^',
    'kFND6': b'\x1b[1@',
    'kHOM': b'\x1b[7$',
    'kHOM5': b'\x1b[7^',
    'kHOM6': b'\x1b[7@',
    'kIC': b'\x1b[2$',
    'kIC5': b'\x1b[2^',
    'kIC6': b'\x1b[2@',
    'kLFT': b'\x1b[d',
    'kLFT5': b'\x1bOd',
    'kNXT': b'\x1b[6$',
    'kNXT5': b'\x1b[6^',
    'kNXT6': b'\x1b[6@',
    'kPRV': b'\x1b[5$',
    'kPRV5': b'\x1b[5^',
    'kPRV6': b'\x1b[5@',
    'kRIT': b'\x1b[c',
    'kRIT5': b'\x1bOc',
    'kUP': b'\x1b[a',
    'kUP5': b'\x1bOa',
    'ka1': b'\x1bOw',
    'ka3': b'\x1bOy',
    'kb2': b'\x1bOu',
    'kbs': b'\x7f',
    'kc1': b'\x1bOq',
    'kc3': b'\x1bOs',
    'kcbt': b'\x1b[Z',
    'kcub1': b'\x1b[D',
    'kcud1': b'\x1b[B',
    'kcuf1': b'\x1b[C',
    'kcuu1': b'\x1b[A',
    'kdch1': b'\x1b[3~',
    'kel': b'\x1b[8^',
    'kend': b'\x1b[8~',
    'kent': b'\x1bOM',
    'kf1': b'\x1b[11~',
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
    'kf2': b'\x1b[12~',
    'kf20': b'\x1b[34~',
    'kf3': b'\x1b[13~',
    'kf4': b'\x1b[14~',
    'kf5': b'\x1b[15~',
    'kf6': b'\x1b[17~',
    'kf7': b'\x1b[18~',
    'kf8': b'\x1b[19~',
    'kf9': b'\x1b[20~',
    'kfnd': b'\x1b[1~',
    'khome': b'\x1b[7~',
    'kich1': b'\x1b[2~',
    'kmous': b'\x1b[M',
    'knp': b'\x1b[6~',
    'kpp': b'\x1b[5~',
    'kslt': b'\x1b[4~',
    'mc0': b'\x1b[i',
    'mc4': b'\x1b[4i',
    'mc5': b'\x1b[5i',
    'op': b'\x1b[39;49m',
    'rc': b'\x1b8',
    'rev': b'\x1b[7m',
    'ri': b'\x1bM',
    'rin': b'\x1b[%p1%dT',
    'ritm': b'\x1b[23m',
    'rmacs': b'',
    'rmam': b'\x1b[?7l',
    'rmcup': b'\x1b[r\x1b[?1049l',
    'rmir': b'\x1b[4l',
    'rmkx': b'\x1b>',
    'rmso': b'\x1b[27m',
    'rmul': b'\x1b[24m',
    'rs1': b'\x1bc',
    'rs2': b'\x1b[r\x1b[m\x1b[?7;25h\x1b[?1;3;4;5;6;9;66;1000;1001;1049l\x1b[4l',
    's0ds': b'',
    's1ds': b'',
    's2ds': b'\x1b*B',
    's3ds': b'\x1b+B',
    'sc': b'\x1b7',
    'setab': b'\x1b[48;5;%p1%dm',
    'setaf': b'\x1b[38;5;%p1%dm',
    'setb': b'%?%p1%{7}%>%t\x1b[48;5;%p1%dm%e\x1b[4%?%p1%{1}%=%t4%e%p1%{3}%=%t6%e%p1%{4}%=%t1%e%p1%{6}%=%t3%e%p1%d%;m%;',
    'setf': b'%?%p1%{7}%>%t\x1b[38;5;%p1%dm%e\x1b[3%?%p1%{1}%=%t4%e%p1%{3}%=%t6%e%p1%{4}%=%t1%e%p1%{6}%=%t3%e%p1%d%;m%;',
    'sgr': b'\x1b[%?%p6%t;1%;%?%p2%t;4%;%?%p1%p3%|%t;7%;%?%p4%t;5%;%?%p7%t;8%;m',
    'sgr0': b'\x1b[m',
    'sitm': b'\x1b[3m',
    'smacs': b'',
    'smam': b'\x1b[?7h',
    'smcup': b'\x1b[?1049h',
    'smir': b'\x1b[4h',
    'smkx': b'\x1b=',
    'smso': b'\x1b[7m',
    'smul': b'\x1b[4m',
    'tbc': b'\x1b[3g',
    'tsl': b'\x1b]2;',
    'u6': b'\x1b[%i%d;%dR',
    'u7': b'\x1b[6n',
    'u8': b'\x1b[?1;2c',
    'u9': b'\x1b[c',
    'vpa': b'\x1b[%i%p1%dd',
}
