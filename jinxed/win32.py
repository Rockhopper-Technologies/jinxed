# -*- coding: utf-8 -*-
# Copyright 2019 Avram Lubkin, All Rights Reserved

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
Support functions and wrappers for calls to the Windows API
"""

import atexit
from collections import namedtuple
import ctypes
from ctypes import wintypes
import msvcrt  # pylint: disable=import-error
import os
import platform
import sys

LPDWORD = ctypes.POINTER(wintypes.DWORD)
COORD = wintypes._COORD  # pylint: disable=protected-access

# Console input modes
ENABLE_ECHO_INPUT = 0x0004
ENABLE_EXTENDED_FLAGS = 0x0080
ENABLE_INSERT_MODE = 0x0020
ENABLE_LINE_INPUT = 0x0002
ENABLE_MOUSE_INPUT = 0x0010
ENABLE_PROCESSED_INPUT = 0x0001
ENABLE_QUICK_EDIT_MODE = 0x0040
ENABLE_WINDOW_INPUT = 0x0008
ENABLE_VIRTUAL_TERMINAL_INPUT = 0x0200

# Console output modes
ENABLE_PROCESSED_OUTPUT = 0x0001
ENABLE_WRAP_AT_EOL_OUTPUT = 0x0002
ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
DISABLE_NEWLINE_AUTO_RETURN = 0x0008
ENABLE_LVB_GRID_WORLDWIDE = 0x0010

if tuple(int(num) for num in platform.version().split('.')) >= (10, 0, 10586):
    VTMODE_SUPPORTED = True
    CBREAK_MODE = ENABLE_PROCESSED_INPUT | ENABLE_VIRTUAL_TERMINAL_INPUT
    RAW_MODE = ENABLE_VIRTUAL_TERMINAL_INPUT
else:
    VTMODE_SUPPORTED = False
    CBREAK_MODE = ENABLE_PROCESSED_INPUT
    RAW_MODE = 0

GTS_SUPPORTED = hasattr(os, 'get_terminal_size')
TerminalSize = namedtuple('TerminalSize', ('columns', 'lines'))


class ConsoleScreenBufferInfo(ctypes.Structure):  # pylint: disable=too-few-public-methods
    """
    CONSOLE_SCREEN_BUFFER_INFO structure
    https://docs.microsoft.com/en-us/windows/console/console-screen-buffer-info-str
    """

    _fields_ = [('dwSize', COORD),
                ('dwCursorPosition', COORD),
                ('wAttributes', wintypes.WORD),
                ('srWindow', wintypes.SMALL_RECT),
                ('dwMaximumWindowSize', COORD)]


CSBIP = ctypes.POINTER(ConsoleScreenBufferInfo)


def _check_bool(result, func, args):  # pylint: disable=unused-argument
    """
    Used as an error handler for Windows calls
    Gets last error if call is not successful
    """

    if not result:
        raise ctypes.WinError(ctypes.get_last_error())
    return args


KERNEL32 = ctypes.WinDLL('kernel32', use_last_error=True)

KERNEL32.GetConsoleMode.errcheck = _check_bool
KERNEL32.GetConsoleMode.argtypes = (wintypes.HANDLE, LPDWORD)

KERNEL32.SetConsoleMode.errcheck = _check_bool
KERNEL32.SetConsoleMode.argtypes = (wintypes.HANDLE, wintypes.DWORD)

KERNEL32.GetConsoleScreenBufferInfo.errcheck = _check_bool
KERNEL32.GetConsoleScreenBufferInfo.argtypes = (wintypes.HANDLE, CSBIP)


def get_csbi(filehandle=None):
    """
    Returns a CONSOLE_SCREEN_BUFFER_INFO structure for the given console or stdout
    filehandle is a Windows filehandle object returned by msvcrt.get_osfhandle()
    """

    if filehandle is None:
        filehandle = msvcrt.get_osfhandle(sys.__stdout__.fileno())

    csbi = ConsoleScreenBufferInfo()
    KERNEL32.GetConsoleScreenBufferInfo(filehandle, ctypes.byref(csbi))
    return csbi


def get_console_mode(filehandle):
    """
    Convenience function for GetConsoleMode
    filehandle is a Windows filehandle object returned by msvcrt.get_osfhandle()
    """

    mode = wintypes.DWORD()
    KERNEL32.GetConsoleMode(filehandle, ctypes.byref(mode))
    return mode.value


def set_console_mode(filehandle, mode):
    """
    Convenience function for SetConsoleMode
    filehandle is a Windows filehandle object returned by msvcrt.get_osfhandle()
    """
    return bool(KERNEL32.SetConsoleMode(filehandle, mode))


def setcbreak(filehandle):
    """
    Convenience function to mimic tty.cbreak() behavior
    filehandle is a Windows filehandle object returned by msvcrt.get_osfhandle()
    """
    return set_console_mode(filehandle, CBREAK_MODE)


def setraw(filehandle):
    """
    Convenience function for mimic tty.raw() behavior
    filehandle is a Windows filehandle object returned by msvcrt.get_osfhandle()
    """
    return set_console_mode(filehandle, RAW_MODE)


def enable_vt_mode(filehandle=None):
    """
    Enables virtual terminal processing mode for the given console or stdout
    filehandle is a Windows filehandle object returned by msvcrt.get_osfhandle()
    """

    if filehandle is None:
        filehandle = msvcrt.get_osfhandle(sys.__stdout__.fileno())

    mode = get_console_mode(filehandle)
    mode |= ENABLE_VIRTUAL_TERMINAL_PROCESSING
    set_console_mode(filehandle, mode)


def get_terminal_size(fd):  # pylint:  disable=invalid-name
    """
    Convenience method for getting terminal size
    """

    # In Python 3.3+ we can let the standard library handle this
    if GTS_SUPPORTED:
        return os.get_terminal_size(fd)

    handle = msvcrt.get_osfhandle(fd)
    window = get_csbi(handle).srWindow
    return TerminalSize(window.Right - window.Left + 1, window.Bottom - window.Top + 1)


def get_term(fd, fallback=True):  # pylint:  disable=invalid-name
    """
    Attempt to determine and enable terminal
    If fallback is True, the fallback will be enabled when no other terminal can be determined
    """

    # First try TERM
    term = os.environ.get('TERM', None)

    if term is None:

        # See if ansicon is enabled
        if os.environ.get('ANSICON', None):
            term = 'ansicon'

        # See if the version of Windows supports VTMODE
        elif VTMODE_SUPPORTED:
            try:
                filehandle = msvcrt.get_osfhandle(fd)
                mode = get_console_mode(filehandle)
            except OSError:
                term = 'unknown'
            else:
                atexit.register(set_console_mode, filehandle, mode)
                set_console_mode(filehandle, mode | ENABLE_VIRTUAL_TERMINAL_PROCESSING)
                term = 'vtwin10'

        # Currently falling back to Ansicon for older versions of Windows
        elif fallback:
            import ansicon  # pylint: disable=import-error,import-outside-toplevel
            ansicon.load()

            try:
                filehandle = msvcrt.get_osfhandle(fd)
                mode = get_console_mode(filehandle)
            except OSError:
                term = 'unknown'
            else:
                atexit.register(set_console_mode, filehandle, mode)
                set_console_mode(filehandle, mode ^ ENABLE_WRAP_AT_EOL_OUTPUT)
                term = 'ansicon'

        else:
            term = 'unknown'

    return term
