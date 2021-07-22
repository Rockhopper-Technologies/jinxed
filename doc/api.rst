..
  Copyright 2019 - 2021 Avram Lubkin, All Rights Reserved

  This Source Code Form is subject to the terms of the Mozilla Public
  License, v. 2.0. If a copy of the MPL was not distributed with this
  file, You can obtain one at http://mozilla.org/MPL/2.0/.

:github_url: https://github.com/Rockhopper-Technologies/jinxed

API Reference
=============

jinxed
------

.. py:module:: jinxed

Jinxed is an implementation of a subset of the Python curses library for Windows

.. autofunction:: setupterm
.. autofunction:: tigetflag
.. autofunction:: tigetnum
.. autofunction:: tigetstr
.. autofunction:: tparm(str[, ...])
.. autoexception:: error


jinxed.win32
------------

.. role:: python(code)
   :language: python

.. automodule:: jinxed.win32
  :members:
  :exclude-members: TerminalSize
  :member-order: bysource

  .. note::
    Some functions require a file descriptor while others require a file handle.
    The windows library generally requires file handles, but some functions are intended
    to mimic existing functions that use file descriptors. An example of a obtaining a
    file descriptor is :python:`fd = sys.stdout.fileno()`. The file handle can then be
    obtained with :python:`msvcrt.get_osfhandle(fd)`.

  .. py:data:: VTMODE_SUPPORTED

    True when the Windows version is 10.0.10586 or higher

  .. py:class:: ConsoleScreenBufferInfo

    Python representation of a CONSOLE_SCREEN_BUFFER_INFO_ object


.. _GetConsoleScreenBufferInfo: https://docs.microsoft.com/en-us/windows/console/getconsolescreenbufferinfo
.. _CONSOLE_SCREEN_BUFFER_INFO: https://docs.microsoft.com/en-us/windows/console/console-screen-buffer-info-str
.. _GetConsoleMode: https://docs.microsoft.com/en-us/windows/console/getconsolemode
.. _SetConsoleMode: https://docs.microsoft.com/en-us/windows/console/setconsolemode
