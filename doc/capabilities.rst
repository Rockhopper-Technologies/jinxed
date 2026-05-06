Capabilities
============

Jinxed provides a lightweight virtual `capabilities database` with its `terminfo(5)`_ family of
functions derived from the gnu ncurses file `terminfo.src`_ without the requirement of any system
libraries.

Singleton-free
--------------

Python's :func:`curses.setupterm` has something of an undocumented singleton:
:func:`curses.setupterm` allows only a single terminal type to be initialized for the lifetime of
the process, and may not be changed:

.. code-block:: python

    >>> import curses
    >>> curses.setupterm('xterm')
    >>> curses.tigetstr('sgr')
    b'%?%p9%t\x1b(0%e\x1b(B%;\x1b[0%?%p6%t;1%;%?%p5%t;2%;%?%p2%t;4%;%?%p1%p3%|%t;7%;%?%p4%t;5%;%?%p7%t;8%;m'
    >>> curses.setupterm('vt100')
    >>> curses.tigetstr('sgr')
    b'%?%p9%t\x1b(0%e\x1b(B%;\x1b[0%?%p6%t;1%;%?%p5%t;2%;%?%p2%t;4%;%?%p1%p3%|%t;7%;%?%p4%t;5%;%?%p7%t;8%;m'

This is especially a problem for writing telnet or ssh network services like MUDs or BBSs, where
thread-safe support for multiple terminal capabilities in a single process session is required.
Jinxed has no such limitation, offering a class-first variant of the global C functions, the
`jinxed.Terminal`_ class can be instantiated for many terminal types per process:

.. code-block:: python

    >>> import jinxed
    >>> jinxed.Terminal('xterm').tigetstr('sgr')
    b'\x1b[0%?%p6%t;1%;%?%p5%t;2%;%?%p2%t;4%;%?%p1%p3%|%t;7%;%?%p4%t;5%;%?%p7%t;8%;m'
    >>> jinxed.Terminal('vt100').tigetstr('sgr')
    b'\x1b[0%?%p1%p6%|%t;1%;%?%p2%t;4%;%?%p1%p3%|%t;7%;%?%p4%t;5%;m'

Database
---------

Jinxed ships a **virtual terminfo database** as python code distributed in its `terminfo/`_ folder,
and uses no system terminfo, termcap or ncurses C Library code.  This is important for some
distributions of Python like the standard Python Windows release, though containing the curses_
module, its capability database is empty. Many Python distributions may also be missing support for
curses_ entirely.

If you request an unsupported ``$TERM``, jinxed raises ``jinxed.error``.  Catch it and fall back to
a common terminal type, like ``xterm-256color``.

An example using the Singleton-free `jinxed.Terminal`_:

.. code-block:: python

    import jinxed, os

    try:
        term = jinxed.Terminal(os.environ.get('TERM', 'xterm-256color'))
    except jinxed.error:
        term = jinxed.Terminal('xterm-256color')
    print(term.tigetstr('sgr'))

Terminals
---------

To ensure a small packaging size, only a subset of the 1,000+ historically known termcap entries are
provided by Jinxed. The following are generated from the ncurses `terminfo.src`_ source file by the
script found in Jinxed source repository, `codegen_terminfo.py
<https://github.com/Rockhopper-Technologies/jinxed/blob/main/codegen_terminfo.py>`_.

.. BEGIN_TERMINAL_LIST
- `alacritty <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/alacritty.py>`_
- `ansi <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/ansi.py>`_
- `cons25 <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/cons25.py>`_, ansi80x25, ansis
- `contour <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/contour.py>`_, contour-latest
- `dtterm <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/dtterm.py>`_
- `foot <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/foot.py>`_
- `ghostty <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/ghostty.py>`_, xterm-ghostty
- `hpterm <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/hpterm.py>`_, X-hpterm
- `iris-ansi <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/iris_ansi.py>`_, iris-ansi-net
- `kitty <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/kitty.py>`_, xterm-kitty
- `linux <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/linux.py>`_
- `linux-16color <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/linux_16color.py>`_
- `putty <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/putty.py>`_
- `putty-256color <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/putty_256color.py>`_
- `rio <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/rio.py>`_
- `rxvt <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/rxvt.py>`_, rxvt-color
- `rxvt-256color <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/rxvt_256color.py>`_
- `rxvt-unicode <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/rxvt_unicode.py>`_
- `rxvt-unicode-256color <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/rxvt_unicode_256color.py>`_
- `screen <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/screen.py>`_
- `screen-256color <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/screen_256color.py>`_
- `st <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/st.py>`_, stterm
- `st-256color <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/st_256color.py>`_, stterm-256color
- `sun <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/sun.py>`_, sun1, sun2
- `tmux <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/tmux.py>`_
- `tmux-256color <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/tmux_256color.py>`_
- `vt100 <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/vt100.py>`_, vt100-am
- `vt102 <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/vt102.py>`_
- `vt220 <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/vt220.py>`_, vt200
- `vt320 <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/vt320.py>`_, vt300
- `wezterm <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/wezterm.py>`_
- `wy50 <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/wy50.py>`_, wyse50
- `xterm <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/xterm.py>`_
- `xterm-16color <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/xterm_16color.py>`_
- `xterm-256color <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/xterm_256color.py>`_
- `xterm-new <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/xterm_new.py>`_

Hand-maintained (not generated by codegen):

- `ansi-bbs <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/ansi_bbs.py>`_
- `ansicon <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/ansicon.py>`_
- `syncterm <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/syncterm.py>`_
- `vtwin10 <https://github.com/Rockhopper-Technologies/jinxed/blob/main/jinxed/terminfo/vtwin10.py>`_
.. END_TERMINAL_LIST

If you find any entry missing, please open report an issue `on GitHub
<https://github.com/Rockhopper-Technologies/jinxed/issues>`_ or create a pull request for
`jinxed/terminals.txt <https://github.com/Rockhopper-Technologies/jinxed/blob/main/terminals.txt>`_

.. _missing legacy codes:

Missing Legacy Codes
--------------------

Three kinds of Control Codes **are** removed from the virtual database:

- ``$<N>`` delay markers (e.g. ``$<50>`` meaning "pad 50ms") are removed, these are required for
  real hardware terminals with poor flow control that may need a bit of rest after some sequences.

  Jinxed provides no functions to interpret these codes and so they are removed.

- All ``\x1b(B``, ``\x1b(0``, ``\x1b(A``, ``\x1b(U``, ``\x1b(K`` G0/G1 Set Graphic Set designations
  and their related ``\x0e`` and ``\x0f`` Shift-Out and Shift-In control codes are removed.  These
  legacy sequences no longer apply to unicode/utf-8 terminals, and mainly only cause confusion.

  Historically, when a curses program used an sgr sequence the 9th parameter could be used to turn
  on line drawing mode, ``tparm(sgr, 0,0,0,0,0,0,0,0,1)``, and the sgr string was yielded with
  ``\x1b(0``, and calling with param 9=0 (default) yield with ``\x1b(B`` to switch back.

  Jinxed provides no functions to manage historic terminal character sets and so they are removed.

- The ``smacs``, ``rmacs``, ``enacs``, ``s0ds``, and ``s1ds`` capabilities are dropped entirely.

  These enter/exit alternate character set operations switch between ASCII and line-drawing mode
  via G0/G1 designation or Shift-Out/Shift-In.  Modern terminals use Unicode mapping (``acsc``)
  for line-drawing characters instead.

.. _blessed: https://pypi.org/project/blessed
.. _`capabilities database`: https://jinxed.readthedocs.io/en/stable/capabilities.html
.. _curses: https://docs.python.org/3/library/curses.html
.. _jinxed.terminal: https://jinxed.readthedocs.io/en/stable/api.html#jinxed.terminal
.. _`terminfo(5)`: https://invisible-island.net/ncurses/man/terminfo.5.html
.. _terminfo.src: https://invisible-island.net/ncurses/terminfo.src.html
.. _`terminfo/`: https://github.com/Rockhopper-Technologies/jinxed/tree/main/jinxed/terminfo
