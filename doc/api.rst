..
  Copyright 2019 Avram Lubkin, All Rights Reserved

  This Source Code Form is subject to the terms of the Mozilla Public
  License, v. 2.0. If a copy of the MPL was not distributed with this
  file, You can obtain one at http://mozilla.org/MPL/2.0/.

:github_url: https://github.com/Rockhopper-Technologies/jinxed

API Reference
=============

jinxed
------

.. py:module:: jinxed

.. py:function:: setupterm([termstr, fd])

  Reimplementation of :py:func:`curses.setupterm`

.. py:function:: tigetflag(capname)

  Reimplementation of :py:func:`curses.tigetflag`

.. py:function:: tigetnum(capname)

  Reimplementation of :py:func:`curses.tigetnum`

.. py:function:: tigetstr(capname)

  Reimplementation of :py:func:`curses.tigetstr`

.. py:function:: tparm(str[, ...])

  Reimplementation of :py:func:`curses.tparm`

.. py:class:: error

  Generic class for Jinxed errors

jinxed.win32
------------

.. role:: python(code)
   :language: python

.. note::
  Some functions require a file descriptor while others require a file handle.
  The windows library generally requires file handles, but some functions are intended
  to mimic existing functions that use file descriptors. An example of a obtaining a
  file descriptor is :python:`fd = sys.stdout.fileno()`. The file handle can then be
  obtained with :python:`msvcrt.get_osfhandle(fd)`.


.. py:module:: jinxed.win32


.. py:data:: VTMODE_SUPPORTED

  True when the WIndows version is 10.0.10586 or higher


.. py:function:: get_csbi(filehandle=None)

  Wrapper for GetConsoleScreenBufferInfo_

  If ``filehandle`` is :py:data:`None`, uses the filehandle of :py:data:`sys.__stdout__`.

  Returns a :py:class:`ConsoleScreenBufferInfo` object.


.. py:function:: get_console_mode(filehandle)

  Wrapper for GetConsoleMode_

  Returns an :py:class:`integer` representation of the current console mode


.. py:function:: set_console_mode(filehandle, mode)

  Wrapper for SetConsoleMode_

  ``mode`` is an :py:class:`integer` representation of the desired mode


.. py:function:: setcbreak(filehandle)

  Operating similarly to :py:func:`tty.setcbreak`, this function is
  a wrapper for SetConsoleMode_.

  All console input options are disabled except ``ENABLE_PROCESSED_INPUT``
  and, if supported, ``ENABLE_VIRTUAL_TERMINAL_INPUT``


.. py:function:: setraw(filehandle)

  Operating similarly to :py:func:`tty.setraw`, this function is
  a wrapper for SetConsoleMode_.

  All console input options are disabled except, if supported,
  ``ENABLE_VIRTUAL_TERMINAL_INPUT``


.. py:function:: get_terminal_size(fd)

  Convenience method for getting terminal size

  In Python 3.3 and above, this is a wrapper for :py:func:`os.get_terminal_size`.
  In older versions of Python, this function calls GetConsoleScreenBufferInfo_.

  In both cases, a :py:class:`~os.terminal_size` object is returned.


.. py:function:: get_term(fd, fallback=True)

  Attempts to determine and enable the current terminal type

  The current logic is:

    - If TERM is defined in the environment, the value is returned
    - Else, if ANSICON is defined in the environment, ``'ansicon'`` is returned
    - Else, if virtual terminal mode is natively supported, it is enabled and ``'vtwin10'`` is returned
    - Else, if ``fallback`` is ``True``, Ansicon is loaded, and ``'ansicon'`` is returned
    - If no other conditions are satisfied, ``'unknown'`` is returned

  This logic may change in the future as additional terminal types are added.

.. py:class:: ConsoleScreenBufferInfo

  Python representation of a ConsoleScreenBufferInfo_ object


.. _GetConsoleScreenBufferInfo: https://docs.microsoft.com/en-us/windows/console/getconsolescreenbufferinfo
.. _ConsoleScreenBufferInfo: https://docs.microsoft.com/en-us/windows/console/console-screen-buffer-info-str
.. _GetConsoleMode: https://docs.microsoft.com/en-us/windows/console/getconsolemode
.. _SetConsoleMode: https://docs.microsoft.com/en-us/windows/console/setconsolemode
