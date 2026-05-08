# -*- coding: utf-8 -*-
# Copyright 2019 - 2026 Avram Lubkin, All Rights Reserved

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
Provides a terminal class primarily for accessing functions that depend on
a terminal which has been previously setup as well as those functions
"""

import importlib
import io
import platform
import sys

from jinxed.terminfo import BOOL_CAPS, NUM_CAPS
from jinxed.terminfo._aliases import ALIASES
from jinxed._util import BASESTRING, error, raise_from_none

if platform.system() == 'Windows':  # pragma: no branch
    from jinxed.win32 import get_term  # pragma: no cover
else:
    from jinxed._util import get_term


TERM = None


class Terminal(object):
    """
    Persistent terminal object for functions that require a previously configured state
    """

    def __init__(self, term=None, fd=-1):  # pylint: disable=invalid-name

        # Type check for term
        if term is not None and not isinstance(term, BASESTRING):
            raise TypeError('term must be a string or None, not %s' % type(term).__name__)

        # Type check and default handling for fd
        if fd == -1:
            try:
                self.stream_fd = sys.stdout.fileno()
            except (AttributeError, TypeError, io.UnsupportedOperation):
                self.stream_fd = None
        elif not isinstance(fd, int):
            raise TypeError('fd must be an integer, not %s' % type(fd).__name__)
        else:
            self.stream_fd = fd

        # Try to dynamically determine terminal type
        if term is None:
            term = get_term(self.stream_fd)

        # Overlay capability caches (populated externally)
        self._overlay_str_caps = {}   # type: Dict[str, bytes]
        self._overlay_num_caps = {}   # type: Dict[str, int]
        self._overlay_bool_caps = set()  # type: Set[str]

        modname = ALIASES.get(term, term).replace('-', '_').replace('.', '_').lower()
        try:
            self.terminfo = importlib.import_module(
                'jinxed.terminfo.%s' % modname)
        except ImportError:
            raise_from_none(error('Could not find terminal %s' % term))

    def overlay_capabilities(self, str_caps=None, num_caps=None, bool_caps=None):
        # type: (Optional[Dict[str, Union[str, bytes]]], Optional[Dict[str, int]],
        #         Optional[Set[str]]) -> None
        """
        Overlay terminfo capabilities onto this terminal instance.

        Methods :meth:`tigetstr`, :meth:`tigetnum`, and :meth:`tigetflag` consult these given caches
        before falling back to the virtual terminfo database. This can be used to "patch" the
        capabilities database or with dynamic capability responses.

        :arg dict str_caps: Mapping of capability name to string value.  String values are encoded
            as ``latin-1``; ``bytes`` values are stored directly.  For non-ASCII text, prefer
            ``bytes`` to avoid ambiguities with ``latin-1`` encoding.
        :arg dict num_caps: Mapping of capability name to integer value.
        :arg set bool_caps: Set of boolean capability names that are present.
        """
        if str_caps:
            for key, val in str_caps.items():
                self._overlay_str_caps[key] = (
                        val if isinstance(val, bytes) else val.encode('latin-1')
                )
        if num_caps:
            self._overlay_num_caps.update(num_caps)
        if bool_caps:
            self._overlay_bool_caps.update(bool_caps)

    def tigetstr(self, capname):
        """
        Reimplementation of curses.tigetstr()
        """
        # Overlay cache takes priority (values are pre-encoded in overlay_capabilities)
        val = self._overlay_str_caps.get(capname)
        if val is not None:
            return val

        return self.terminfo.STR_CAPS.get(capname, None)

    def tigetnum(self, capname):
        """
        Reimplementation of curses.tigetnum()
        """

        # Overlay cache takes priority
        if capname in self._overlay_num_caps:
            return self._overlay_num_caps[capname]

        return self.terminfo.NUM_CAPS.get(capname, -1 if capname in NUM_CAPS else -2)

    def tigetflag(self, capname):
        """
        Reimplementation of curses.tigetflag()
        """

        # Overlay cache takes priority
        if capname in self._overlay_bool_caps:
            return 1

        if capname in self.terminfo.BOOL_CAPS:
            return 1
        return 0 if capname in BOOL_CAPS else -1


def setupterm(term=None, fd=-1):  # pylint: disable=invalid-name
    """
    Reimplementation of :py:func:`curses.setupterm`
    """

    global TERM  # pylint: disable=global-statement
    TERM = Terminal(term, fd)


def tigetflag(capname):
    """
    Reimplementation of :py:func:`curses.tigetflag`
    """

    if TERM is None:
        raise error('Must call setupterm() first')
    return TERM.tigetflag(capname)


def tigetnum(capname):
    """
    Reimplementation of :py:func:`curses.tigetnum`
    """

    if TERM is None:
        raise error('Must call setupterm() first')
    return TERM.tigetnum(capname)


def tigetstr(capname):
    """
    Reimplementation of :py:func:`curses.tigetstr`
    """

    if TERM is None:
        raise error('Must call setupterm() first')
    return TERM.tigetstr(capname)
