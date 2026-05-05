"""
syncterm terminal info

Source: SyncTERM src/syncterm/conn_pty.c
  Function: pty_connect() -- assembles termcap at runtime via xp_asprintf
  URL:      https://gitlab.synchro.net/main/sbbs/-/raw/master/src/syncterm/conn_pty.c
  Caps:     256-color palette when CONIO_OPT_PALETTE_SETTING is set,
            8-color fallback otherwise (this module uses 256-color).

syncterm is SyncTERM's native terminal type, reported via TTYPE
negotiation over telnet.  It extends ANSI with BBS-oriented escape
sequences including DECSC/DECRC mouse tracking, SGR cursor styling,
and insert/delete line/char operations.  For local-mode connections,
see ansi-bbs.
"""

BOOL_CAPS = [
    'am',
    'bce',
    'ccc',
    'msgr',
]

NUM_CAPS = {
    'colors': 256,
    'cols': 80,
    'it': 8,
    'lines': 24,
    'pairs': 32767,
}

STR_CAPS = {
    'acsc': (
        b'\x7d\x9c|\x80{\x82+\x10,\x11l\x8am\x80k\xb7j\x99'
        b'u\x94t\x83v\x81w\x82q\x84x\x93n\x85`^Da\xb0f\xf8'
        b'g\xf1~\xf9.^Y-^Xh\xb1i^U0\x9by\xf3z\xf2'
    ),
    'bel': b'\a',
    'blink': b'\x1b[5m',
    'bold': b'\x1b[1m',
    'cbt': b'\x1b[Z',
    'civis': b'\x1b[?25l',
    'clear': b'\x1b[2J',
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
    'cvvis': b'\x1b[?25h',
    'dch': b'\x1b[%p1%dP',
    'dch1': b'\x1b[P',
    'dl': b'\x1b[%p1%dM',
    'dl1': b'\x1b[M',
    'ech': b'\x1b[%p1%dX',
    'ed': b'\x1b[J',
    'el': b'\x1b[K',
    'el1': b'\x1b[1K',
    'home': b'\x1b[H',
    'hpa': b'\x1b[%i%p1%dG',
    'ht': b'\t',
    'hts': b'\x1bH',
    'ich': b'\x1b[%p1%d@',
    'ich1': b'\x1b[@',
    'il': b'\x1b[%p1%dL',
    'il1': b'\x1b[L',
    'indn': b'\x1b[%p1%dS',
    'is1': b'\x1bc',
    'kbs': b'\x08',
    'kcbt': b'\x1b[Z',
    'kcub1': b'\x1b[D',
    'kcud1': b'\x1b[B',
    'kcuf1': b'\x1b[C',
    'kcuu1': b'\x1b[A',
    'kdch1': b'\x7f',
    'kend': b'\x1b[Y',
    'kf1': b'\x1b[11~',
    'kf2': b'\x1b[12~',
    'kf3': b'\x1b[13~',
    'kf4': b'\x1b[14~',
    'kf5': b'\x1b[15~',
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
    'op': b'\x1b[39;49m',
    'rc': b'\x1b[u',
    'rev': b'\x1b[0;1;7m',
    'rin': b'\x1b[%p1%dT',
    'rmam': b'\x1b[?7l',
    'rmcup': b'\x1b[?69h\x1b[s\x1b[?69l',
    'rs1': b'\x1bc',
    'sc': b'\x1b[s',
    'setab': b'\x1b[48;5;%p1%dm',
    'setaf': b'\x1b[38;5;%p1%dm',
    'sgr0': b'\x1b[m',
    'smam': b'\x1b[?7h',
    'smcup': b'\x1b[?69h\x1b[s\x1b[?69l',
    'smul': b'\x1b[4m',
    'tbc': b'\x1b[3g',
    'u6': b'\x1b[%i%p1%d;%p2%dR',
    'u7': b'\x1b[6n',
    'vpa': b'\x1b[%i%p1%dd',
}
