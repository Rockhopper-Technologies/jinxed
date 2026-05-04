"""
ansi-bbs terminal info

Source: SyncTERM install/termcap
  URL:  https://gitlab.synchro.net/main/sbbs/-/raw/master/install/termcap
  Caps: 8-color ANSI with BBS extensions (DECSC/DECRC, function keys)

ansi-bbs is SyncTERM's local-mode terminal type, an extended ANSI
variant used for direct BBS connections.  syncterm (q.v.) is the
equivalent type reported over telnet TTYPE negotiation.
"""

BOOL_CAPS = [
    'am',
    'eo',
    'msgr',
]

NUM_CAPS = {
    'colors': 8,
    'cols': 80,
    'lines': 24,
    'pairs': 64,
}

STR_CAPS = {
    'acsc': b'\x7d\x9c|\x80{\x82+\x10,\x11l\x8am\x80k\xb7j\x99u\x94t\x83v\x81w\x82q\x84x\x93n\x85`^Da\xb0f\xf8g\xf1~\xf9.^Y-^Xh\xb1i^U0\x9by\xf3z\xf2',
    'bel': b'\a',
    'blink': b'\x1b[5m',
    'bold': b'\x1b[1m',
    'clear': b'\x1b[2J\x1b[H',
    'cnorm': b'\x1b[?25h',
    'civis': b'\x1b[?25l',
    'cr': b'\r',
    'cub': b'\x1b[%p1%dD',
    'cub1': b'\b',
    'cud': b'\x1b[%p1%dB',
    'cud1': b'\x1b[B',
    'cuf': b'\x1b[%p1%dC',
    'cuf1': b'\x1b[C',
    'cup': b'\x1b[%i%p1%d;%p2%dH',
    'cuu': b'\x1b[%p1%dA',
    'cuu1': b'\x1b[A',
    'cvvis': b'\x1b[?25h',
    'dch1': b'\x1b[P',
    'dl1': b'\x1b[M',
    'ed': b'\x1b[J',
    'el': b'\x1b[K',
    'el1': b'\x1b[1K',
    'home': b'\x1b[H',
    'ht': b'\t',
    'il1': b'\x1b[L',
    'ich1': b'\x1b[@',
    'invis': b'\x1b[8m',
    'is1': b'\x1b[m\x1b[2J\x1b[H',
    'kbs': b'\x08',
    'kcub1': b'\x1b[D',
    'kcud1': b'\x1b[B',
    'kcuf1': b'\x1b[C',
    'kcuu1': b'\x1b[A',
    'kdch1': b'\x7f',
    'kel': b'\x1b[K',
    'kend': b'\x1b[Y',
    'kf1': b'\x1bOP',
    'kf2': b'\x1bOQ',
    'kf3': b'\x1bOR',
    'kf4': b'\x1bOS',
    'kf5': b'\x1bOt',
    'kf6': b'\x1b[17~',
    'kf7': b'\x1b[18~',
    'kf8': b'\x1b[19~',
    'kf9': b'\x1b[20~',
    'kf10': b'\x1b[21~',
    'kf11': b'\x1b[23~',
    'kf12': b'\x1b[24~',
    'khome': b'\x1b[H',
    'kich1': b'\x1b[@',
    'knp': b'\x1b[U',
    'kpp': b'\x1b[V',
    'op': b'\x1b[m',
    'rc': b'\x1b[u',
    'rev': b'\x1b[7m',
    'rmam': b'\x1b[?7l',
    'rmcup': b'\x1b[?69h\x1b[s\x1b[?69l',
    'rs1': b'\x1b[m\x1b[2J\x1b[H',
    'sc': b'\x1b[s',
    'setab': b'\x1b[4%p1%dm',
    'setaf': b'\x1b[3%p1%dm',
    'sgr0': b'\x1b[m',
    'smam': b'\x1b[?7h',
    'smcup': b'\x1b[?69h\x1b[s\x1b[?69l',
    'smul': b'\x1b[4m',
    'u6': b'\x1b[%i%p1%d;%p2%dR',
    'u7': b'\x1b[6n',
    'vpa': b'\x1b[%i%p1%dd',
}
