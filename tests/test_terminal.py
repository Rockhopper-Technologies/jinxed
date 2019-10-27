# -*- coding: utf-8 -*-
# Copyright 2019 Avram Lubkin, All Rights Reserved

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
Test module for jinxed._terminal
"""

import io
import os
import sys

import jinxed
import jinxed.has_key
import jinxed._terminal
import jinxed.terminfo.xterm

from tests import TestCase

if sys.version_info[:2] < (3, 3):
    import mock
else:
    from unittest import mock  # noqa: F401  # pylint: disable=no-name-in-module

# pylint: disable=protected-access


class TestSetuperm(TestCase):
    """
    Tests for jinxed.setupterm()
    """

    def test_bad_term_type(self):
        """
        Raise error if term is not a string
        """
        with self.assertRaisesRegex(TypeError, 'term must be a string or None'):
            jinxed.setupterm(100)

    def test_bad_fd_type(self):
        """
        Raise error if fd is not an integer
        """
        with self.assertRaisesRegex(TypeError, 'fd must be an integer'):
            jinxed.setupterm('xterm', fd='banana')

    def test_unsupported_term(self):
        """
        Raise error if no terminfo for terminal
        """
        with self.assertRaisesRegex(jinxed.error, 'Could not find terminal foobar'):
            jinxed.setupterm('foobar')

    def test_term_none(self):
        """
        If term is none, determine dynamically
        """
        term = os.environ.get('TERM', None)
        jinxed._terminal.TERM = None

        try:
            os.environ['TERM'] = 'xterm'
            jinxed.setupterm()
            self.assertIs(jinxed._terminal.TERM.terminfo, jinxed.terminfo.xterm)

        finally:
            if term is None:
                del os.environ['TERM']
            else:
                os.environ['TERM'] = term

    def test_fd_explicit(self):
        """
        Use fd is given explicitly
        """
        jinxed.setupterm('xterm', fd=sys.stderr.fileno())
        self.assertEqual(jinxed._terminal.TERM.stream_fd, sys.stderr.fileno())

    def test_fd_error(self):
        """
        Set fd to None if known error is encountered
        """

        with mock.patch.object(sys, 'stdout', wraps=sys.stdout) as mockstdout:

            for error in (AttributeError, TypeError, io.UnsupportedOperation):
                mockstdout.fileno.side_effect = error()
                jinxed.setupterm('xterm')
                self.assertIs(jinxed._terminal.TERM.stream_fd, None)


class TestTigetflag(TestCase):
    """
    Tests for jinxed.tigetflag()
    """

    def test_no_term(self):
        """
        Raise exception if tigetflag() is called before setupterm()
        """
        jinxed._terminal.TERM = None
        with self.assertRaises(jinxed.error, msg='Must call setupterm() first'):
            jinxed.tigetflag('am')

    def test_cap_present(self):
        """
        Return 1 if capability is present for terminal
        """
        jinxed.setupterm('xterm')
        self.assertEqual(jinxed.tigetflag('am'), 1)

    def test_cap_missing(self):
        """
        Return 0 if capability is missing for terminal
        """
        jinxed.setupterm('xterm')
        self.assertEqual(jinxed.tigetflag('hz'), 0)

    def test_cap_unknown(self):
        """
        Return -1 if capability is unknown
        """
        jinxed.setupterm('xterm')
        self.assertEqual(jinxed.tigetflag('howmuchwoodawoodchuckwillchuck'), -1)


class TestTigetnum(TestCase):
    """
    Tests for jinxed.tigetnum()
    """

    def test_no_term(self):
        """
        Raise exception if tigetnum() is called before setupterm()
        """
        jinxed._terminal.TERM = None
        with self.assertRaises(jinxed.error, msg='Must call setupterm() first'):
            jinxed.tigetnum('colors')

    def test_cap_present(self):
        """
        Return 1 if capability is present for terminal
        """
        jinxed.setupterm('xterm')
        self.assertEqual(jinxed.tigetnum('colors'), 8)

    def test_cap_missing(self):
        """
        Return 0 if capability is missing for terminal
        """
        jinxed.setupterm('xterm')
        self.assertEqual(jinxed.tigetnum('bitwin'), -1)

    def test_cap_unknown(self):
        """
        Return -1 if capability is unknown
        """
        jinxed.setupterm('xterm')
        self.assertEqual(jinxed.tigetnum('howmuchwoodawoodchuckwillchuck'), -2)


class TestTigetstr(TestCase):
    """
    Tests for jinxed.tigetstr()
    """

    def test_no_term(self):
        """
        Raise exception if tigetstr() is called before setupterm()
        """
        jinxed._terminal.TERM = None
        with self.assertRaises(jinxed.error, msg='Must call setupterm() first'):
            jinxed.tigetstr('bold')

    def test_cap_present(self):
        """
        Return capability if present for terminal
        """
        jinxed.setupterm('xterm')
        self.assertEqual(jinxed.tigetstr('bold'), b'\x1b[1m')

    def test_cap_missing(self):
        """
        Return None if capability is missing for terminal
        """
        jinxed.setupterm('xterm')
        self.assertEqual(jinxed.tigetstr('howmuchwoodawoodchuckwillchuck'), None)
