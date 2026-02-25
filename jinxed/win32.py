# -*- coding: utf-8 -*-
# Copyright 2019 - 2024 Avram Lubkin, All Rights Reserved

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# pylint: disable=too-few-public-methods
"""
Support functions and wrappers for calls to the Windows API
"""

import atexit
import codecs
from collections import namedtuple
import ctypes
from ctypes import wintypes
import io
import msvcrt  # pylint: disable=import-error
import os
import platform
import sys
import time

from jinxed._util import mock, IS_WINDOWS

# Workaround for auto-doc generation on Linux
if not IS_WINDOWS:
    ctypes = mock.Mock()  # noqa: F811

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

if IS_WINDOWS and tuple(int(num) for num in platform.version().split('.')) >= (10, 0, 10586):
    VTMODE_SUPPORTED = True
    CBREAK_MODE = ENABLE_PROCESSED_INPUT | ENABLE_VIRTUAL_TERMINAL_INPUT
    RAW_MODE = ENABLE_VIRTUAL_TERMINAL_INPUT
else:
    VTMODE_SUPPORTED = False
    CBREAK_MODE = ENABLE_PROCESSED_INPUT
    RAW_MODE = 0

GTS_SUPPORTED = hasattr(os, 'get_terminal_size')
TerminalSize = namedtuple('TerminalSize', ('columns', 'lines'))

class ConsoleScreenBufferInfo(ctypes.Structure):
    """
    Python representation of CONSOLE_SCREEN_BUFFER_INFO structure
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

KERNEL32.GetConsoleCP.errcheck = _check_bool
KERNEL32.GetConsoleCP.argtypes = ()

KERNEL32.GetConsoleMode.errcheck = _check_bool
KERNEL32.GetConsoleMode.argtypes = (wintypes.HANDLE, LPDWORD)

KERNEL32.SetConsoleMode.errcheck = _check_bool
KERNEL32.SetConsoleMode.argtypes = (wintypes.HANDLE, wintypes.DWORD)

KERNEL32.GetConsoleScreenBufferInfo.errcheck = _check_bool
KERNEL32.GetConsoleScreenBufferInfo.argtypes = (wintypes.HANDLE, CSBIP)

KERNEL32.WaitForSingleObject.argtypes = (wintypes.HANDLE, wintypes.DWORD)
KERNEL32.WaitForSingleObject.restype = wintypes.DWORD

# Console input record structures for PeekConsoleInputW/ReadConsoleInputW.
# Only KEY_EVENT_RECORD is needed -- all other event types (mouse, focus,
# resize, menu) are drained and discarded by kbhit() for now.


class _KEY_EVENT_RECORD(ctypes.Structure):
    """KEY_EVENT_RECORD -- 16 bytes, the largest INPUT_RECORD union member."""

    _fields_ = [
        ('bKeyDown', wintypes.BOOL),
        ('wRepeatCount', wintypes.WORD),
        ('wVirtualKeyCode', wintypes.WORD),
        ('wVirtualScanCode', wintypes.WORD),
        ('uChar', wintypes.WCHAR),
        ('dwControlKeyState', wintypes.DWORD),
    ]


class _EVENT_UNION(ctypes.Union):
    """INPUT_RECORD Event union (only KeyEvent is accessed)."""

    _fields_ = [('KeyEvent', _KEY_EVENT_RECORD)]


class _INPUT_RECORD(ctypes.Structure):
    """INPUT_RECORD structure."""

    _fields_ = [
        ('EventType', wintypes.WORD),
        ('Event', _EVENT_UNION),
    ]


_PINPUT_RECORD = ctypes.POINTER(_INPUT_RECORD)

KERNEL32.PeekConsoleInputW.argtypes = (
    wintypes.HANDLE, _PINPUT_RECORD, wintypes.DWORD, LPDWORD)
KERNEL32.PeekConsoleInputW.restype = wintypes.BOOL

KERNEL32.ReadConsoleInputW.argtypes = (
    wintypes.HANDLE, _PINPUT_RECORD, wintypes.DWORD, LPDWORD)
KERNEL32.ReadConsoleInputW.restype = wintypes.BOOL


def get_csbi(filehandle=None):
    """
    Args:
        filehandle(int): Windows filehandle object as returned by :py:func:`msvcrt.get_osfhandle`

    Returns:
        :py:class:`ConsoleScreenBufferInfo`: CONSOLE_SCREEN_BUFFER_INFO_ structure

    Wrapper for GetConsoleScreenBufferInfo_

    If ``filehandle`` is :py:data:`None`, uses the filehandle of :py:data:`sys.__stdout__`.

    """

    if filehandle is None:
        filehandle = msvcrt.get_osfhandle(sys.__stdout__.fileno())

    csbi = ConsoleScreenBufferInfo()
    KERNEL32.GetConsoleScreenBufferInfo(filehandle, ctypes.byref(csbi))
    return csbi


def get_console_input_encoding():
    """
    Returns:
        int: Current console mode

    Query for the console input code page and provide an encoding

    If the code page can not be resolved to a Python encoding, :py:data:`None` is returned.
    """

    try:
        encoding = 'cp%d' % KERNEL32.GetConsoleCP()
    except OSError:
        return None

    try:
        codecs.lookup(encoding)
    except LookupError:
        return None

    return encoding


def get_console_mode(filehandle):
    """
    Args:
        filehandle(int): Windows filehandle object as returned by :py:func:`msvcrt.get_osfhandle`

    Returns:
        int: Current console mode

    Raises:
        OSError: Error calling Windows API

    Wrapper for GetConsoleMode_
    """

    mode = wintypes.DWORD()
    KERNEL32.GetConsoleMode(filehandle, ctypes.byref(mode))
    return mode.value


def set_console_mode(filehandle, mode):
    """
    Args:
        filehandle(int): Windows filehandle object as returned by :py:func:`msvcrt.get_osfhandle`
        mode(int): Desired console mode

    Raises:
        OSError: Error calling Windows API

    Wrapper for SetConsoleMode_
    """

    return bool(KERNEL32.SetConsoleMode(filehandle, mode))


def setcbreak(filehandle):
    """
    Args:
        filehandle(int): Windows filehandle object as returned by :py:func:`msvcrt.get_osfhandle`

    Raises:
        OSError: Error calling Windows API

    Convenience function which mimics :py:func:`tty.setcbreak` behavior

    All console input options are disabled except ``ENABLE_PROCESSED_INPUT``
    and, if supported, ``ENABLE_VIRTUAL_TERMINAL_INPUT``
    """

    set_console_mode(filehandle, CBREAK_MODE)


def setraw(filehandle):
    """
    Args:
        filehandle(int): Windows filehandle object as returned by :py:func:`msvcrt.get_osfhandle`

    Raises:
        OSError: Error calling Windows API

    Convenience function which mimics :py:func:`tty.setraw` behavior

    All console input options are disabled except, if supported, ``ENABLE_VIRTUAL_TERMINAL_INPUT``
    """

    set_console_mode(filehandle, RAW_MODE)


def enable_vt_mode(filehandle=None):
    """
    Args:
        filehandle(int): Windows filehandle object as returned by :py:func:`msvcrt.get_osfhandle`

    Raises:
        OSError: Error calling Windows API

    Enables virtual terminal processing mode for the given console

    If ``filehandle`` is :py:data:`None`, uses the filehandle of :py:data:`sys.__stdout__`.
    """

    if filehandle is None:
        filehandle = msvcrt.get_osfhandle(sys.__stdout__.fileno())

    mode = get_console_mode(filehandle)
    mode |= ENABLE_VIRTUAL_TERMINAL_PROCESSING
    set_console_mode(filehandle, mode)


def get_terminal_size(fd):  # pylint:  disable=invalid-name
    """
    Args:
        fd(int): Python file descriptor

    Returns:
        :py:class:`os.terminal_size`: Named tuple representing terminal size

    Convenience function for getting terminal size

    In Python 3.3 and above, this is a wrapper for :py:func:`os.get_terminal_size`.
    In older versions of Python, this function calls GetConsoleScreenBufferInfo_.
    """

    # In Python 3.3+ we can let the standard library handle this
    if GTS_SUPPORTED:
        return os.get_terminal_size(fd)

    handle = msvcrt.get_osfhandle(fd)
    window = get_csbi(handle).srWindow
    return TerminalSize(window.Right - window.Left + 1, window.Bottom - window.Top + 1)


def flush_and_set_console(fd, mode=None):  # pylint:  disable=invalid-name
    """
    Args:
        filehandle(int): Windows filehandle object as returned by :py:func:`msvcrt.get_osfhandle`
        mode(int): Desired console mode. If None, mode is not changed

    Attempts to set console to specified mode, but will not raise on failure

    If the file descriptor is STDOUT or STDERR, attempts to flush first
    """

    try:
        if fd in (sys.__stdout__.fileno(), sys.__stderr__.fileno()):
            sys.__stdout__.flush()
            sys.__stderr__.flush()
    except (AttributeError, TypeError, io.UnsupportedOperation):
        pass

    if mode is not None:

        try:
            filehandle = msvcrt.get_osfhandle(fd)
            set_console_mode(filehandle, mode)
        except OSError:
            pass


def get_term(fd, fallback=True):  # pylint:  disable=invalid-name
    """
    Args:
        fd(int): Python file descriptor
        fallback(bool): Use fallback terminal type if type can not be determined
    Returns:
        str: Terminal type

    Attempts to determine and enable the current terminal type

    The current logic is:

        - If TERM is defined in the environment, the value is returned
        - Else, if ANSICON is defined in the environment, ``'ansicon'`` is returned
        - Else, if virtual terminal mode is natively supported,
          it is enabled and ``'vtwin10'`` is returned
        - Else, if ``fallback`` is ``True``, Ansicon is loaded, and ``'ansicon'`` is returned
        - If no other conditions are satisfied, ``'unknown'`` is returned

    This logic may change in the future as additional terminal types are added.
    """

    # First try TERM
    term = os.environ.get('TERM', None)

    if term is None:

        # See if ansicon is enabled
        if os.environ.get('ANSICON', None):
            term = 'ansicon'

        # See if Windows Terminal is being used
        elif os.environ.get('WT_SESSION', None):
            term = 'vtwin10'

        # See if the version of Windows supports VTMODE
        elif VTMODE_SUPPORTED:
            try:
                filehandle = msvcrt.get_osfhandle(fd)
                mode = get_console_mode(filehandle)
            except OSError:
                term = 'unknown'
            else:
                # Proceed if VT mode is already enabled
                if mode & ENABLE_VIRTUAL_TERMINAL_PROCESSING:
                    atexit.register(flush_and_set_console, fd, None)

                # Otherwise, enable VT mode
                else:
                    atexit.register(flush_and_set_console, fd, mode)
                    # pylint: disable=unsupported-binary-operation
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
                atexit.register(flush_and_set_console, fd, mode)
                set_console_mode(filehandle, mode ^ ENABLE_WRAP_AT_EOL_OUTPUT)
                term = 'ansicon'

        else:
            term = 'unknown'

    return term


def _drain_nonkey_events(handle):
    """
    Discard non-key-down events from the console input buffer.

    :arg int handle: Windows console handle.
    :returns: True if a key-down event is at the front of the buffer.
    :rtype: bool
    """
    record = _INPUT_RECORD()
    count = wintypes.DWORD()
    while True:
        if not KERNEL32.PeekConsoleInputW(
                handle, ctypes.byref(record), 1, ctypes.byref(count)):
            return False
        if count.value == 0:
            return False
        if record.EventType == 0x0001 and record.Event.KeyEvent.bKeyDown:
            return True  # KEY_EVENT with bKeyDown
        # discard non-key-down event (key-up, focus, mouse, resize, menu)
        if not KERNEL32.ReadConsoleInputW(
                handle, ctypes.byref(record), 1, ctypes.byref(count)):
            return False


def kbhit(fd=None, timeout=None):
    """
    Args:
        fd(int): Python file descriptor for keyboard input (e.g., sys.stdin.fileno()).
            If None, uses the file descriptor of :py:data:`sys.__stdin__`.
        timeout(float): Timeout in seconds. None for blocking indefinitely,
            0 for non-blocking, positive for seconds to wait.

    Returns:
        bool: True if a keypress is available to be read, False otherwise.

    Raises:
        OSError: If WaitForSingleObject fails

    Efficient keyboard hit detection using WaitForSingleObject_.

    After the wait signals, non-keyboard events (key-up releases, focus,
    resize) are drained from the input buffer so that only actual key-down
    events cause a True return.

    .. _WaitForSingleObject:
        https://docs.microsoft.com/en-us/windows/win32/api/synchapi/nf-synchapi-waitforsingleobject
    """
    if fd is None:
        fd = sys.__stdin__.fileno()

    handle = msvcrt.get_osfhandle(fd)
    deadline = None if timeout is None else time.monotonic() + max(0, timeout)

    while True:
        # Drain stale non-key events, return immediately if key-down ready.
        if _drain_nonkey_events(handle):
            return True

        # Calculate remaining wait.
        if deadline is not None:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                return False
            wait_ms = int(1000 * remaining)
        else:
            wait_ms = 0xFFFFFFFF  # INFINITE

        result = KERNEL32.WaitForSingleObject(handle, wait_ms)

        if result == 0xFFFFFFFF:  # WAIT_FAILED
            raise ctypes.WinError(ctypes.get_last_error())

        if result != 0x00000000:  # WAIT_TIMEOUT
            return False
