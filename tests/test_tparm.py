# -*- coding: utf-8 -*-
# Copyright 2019 Avram Lubkin, All Rights Reserved

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
Test module for jinxed.tparm

There are two main sets of test
The first checks our tparm() implementation against a known result
The second only runs if curses can be imported and compares the output of our implementation
of tparm() with the curses implementation
"""

from unittest import skipUnless

from jinxed._tparm import tparm

from tests import TestCase


try:
    import curses
    CURSES = True
    curses.setupterm()
except ImportError:
    CURSES = False


TESTS = (('literal_percent', (b'%%',), b'%'),
         ('pop_c_1', (b'%p1%c', 84), b'T'),
         ('pop_c_3', (b'%c',), b'\x80'),
         ('increment_one_two', (b'%i%p1%c%p2%c', 84, 85), b'UV'),
         ('increment_one_two_1', (b'%i%p1%c', 84), b'U'),
         ('increment_one_two_2', (b'%i%p2%c', 0, 84), b'U'),
         ('binary_op_add', (b'%p1%p2%+%d', 1, 2), b'3'),
         ('binary_op_sub', (b'%p1%p2%-%d', 1, 2), b'-1'),
         ('binary_op_mul', (b'%p1%p2%*%d', 1, 2), b'2'),
         ('binary_op_div', (b'%p1%p2%/%d', 5, 2), b'2'),
         ('binary_op_mod', (b'%p1%p2%m%d', 5, 2), b'1'),
         ('binary_op_and', (b'%p1%p2%&%d', 3, 2), b'2'),
         ('binary_op_or', (b'%p1%p2%|%d', 3, 2), b'3'),
         ('binary_op_nor', (b'%p1%p2%^%d', 3, 2), b'1'),
         ('binary_op_eq_2', (b'%p1%p2%=%d', 2, 2), b'1'),
         ('binary_op_eq_1', (b'%p1%p2%=%d', 3, 2), b'0'),
         ('binary_op_gt_1', (b'%p1%p2%>%d', 3, 2), b'1'),
         ('binary_op_gt_2', (b'%p1%p2%>%d', 3, 3), b'0'),
         ('binary_op_lt_1', (b'%p1%p2%<%d', 2, 3), b'1'),
         ('binary_op_lt_2', (b'%p1%p2%<%d', 3, 2), b'0'),
         ('binary_op_log_and_1', (b'%p1%p2%A%d', 0, 0), b'0'),
         ('binary_op_log_and_2', (b'%p1%p2%A%d', 1, 0), b'0'),
         ('binary_op_log_and_3', (b'%p1%p2%A%d', 1, 1), b'1'),
         ('binary_op_log_or_1', (b'%p1%p2%O%d', 0, 0), b'0'),
         ('binary_op_log_or_2', (b'%p1%p2%O%d', 1, 0), b'1'),
         ('binary_op_log_or_3', (b'%p1%p2%O%d', 1, 1), b'1'),
         ('unary_op_inv', (b'%p1%~%d', 3), b'-4'),
         ('unary_op_not_1', (b'%p1%!%d', 1), b'0'),
         ('unary_op_not_2', (b'%p1%!%d', 0), b'1'),
         ('unary_op_not_3', (b'%p1%!%d', 3), b'0'),
         ('unary_op_not_4', (b'%p1%!%d',), b'1'),
         ('dynamic_set_get', (b'%p1%Pv%gv%d', 1), b'1'),
         ('dynamic_unset_get', (b'%gz%d',), b'0'),
         ('static_set_get', (b'%p1%PV%gV%d', 1), b'1'),
         ('static_unset_get', (b'%gZ%d',), b'0'),
         ('int_constant', (b'%{5}%d',), b'5'),
         ('char_constant', (b"%'c'%c",), b'c'),
         ('char_constant_2', (b"%'2'%'3'%+%c",), b'e'),

         # Check this


         ('cond_if_1', (b'%?%p1%tTrue%;', 1), b'True'),
         ('cond_if_2', (b'%?%p1%tTrue%;', 0), b''),
         ('cond_else_1', (b'%?%p1%tTrue%eFalse%;', 0), b'False'),
         ('cond_else_2', (b'%?%p1%tTrue%eFalse%;', 1), b'True'),
         ('cond_compound_1', (b'%?%p1%tOne%e%?%p2%tTwo%eNeither%;', 1, 0), b'One'),
         ('cond_compound_2', (b'%?%p1%tOne%e%?%p2%tTwo%eNeither%;', 0, 1), b'Two'),
         ('cond_compound_3', (b'%?%p1%tOne%e%?%p2%tTwo%eNeither%;', 0, 0), b'Neither'),
         ('cond_nested_1', (b'%?%p1%tOne%e%p2%tTwo%eNeither%;', 1, 0), b'One'),
         ('cond_nested_2', (b'%?%p1%tOne%e%p2%tTwo%eNeither%;', 0, 1), b'Two'),
         ('cond_nested_3', (b'%?%p1%tOne%e%p2%tTwo%eNeither%;', 0, 0), b'Neither'),
         ('cond_complex_1', (b'%?%p1%t%p1%e%p2%;%d', 0, 2), b'2'),

         ('printf_d1', (b'%p1%d', 1), b'1'),
         ('printf_d2', (b'%p1%:+03d', 1), b'+01'),
         ('printf_d3', (b'%p1%:-3d', 1), b'1  '),
         ('printf_d4', (b'%d',), b'0'),
         ('printf_s1', (b'%p1%s',), b''),
         ('printf_s2', (b'%p1%s', b'hi'), b'hi'),
         ('printf_s3', (b'%p1%:-3s', b'hi'), b'hi '),
         ('printf_s4', (b'%s',), b''),
         ('push_len', (b'%p1%l%d', b'hi'), b'2'),

         ('printf_f1', (b'%p1%x', 31), b'1f'),
         ('printf_x1', (b'%p1%x', 31), b'1f'),
         ('printf_x2', (b'%p1%X', 31), b'1F'),
         ('printf_o1', (b'%p1%o', 8), b'10'),
         ('unmatched_1', (b'%z',), b''),
         ('unmatched_2', (b'%w1',), b'1'),
         ('literal', (b'hi',), b'hi'))

KNOWN_FAILURES = ('printf_d2',  # Seems to be a bug in curses printf implementation
                  # Most tparm implementations only accept integers
                  'printf_s2',
                  'printf_s3',
                  'push_len',
                  )


class TestTParmExamples(TestCase):
    """
    Test tparm() against an expected result
    """

    def test_arguments(self):
        """
        Basic tests for invalid arguments
        """

        with self.assertRaisesRegex(TypeError, 'A bytes-like object is required'):
            tparm(u'Not a byte string')

        with self.assertRaisesRegex(TypeError, 'Parameters must be integers'):
            tparm(b'', u'Not an int')

    def test_dynamic_persistance(self):
        """
        Ensure dynamic variables persist between calls
        """
        tparm(b'%p1%Px', 4)
        self.assertEqual(tparm(b'%gx%d'), b'4')

    def test_static_persistance(self):
        """
        Ensure static variables persist between calls
        """
        tparm(b'%p1%PX', 4)
        self.assertEqual(tparm(b'%gX%d'), b'4')

    @ classmethod
    def set_func(cls, desc, args, result):
        """
        Create a test method comparing the result of tparm() and an expected result
        """

        name = 'test_%s' % desc

        def func(self):
            self.assertEqual(tparm(*args), result)

        func.__name__ = name
        if getattr(cls, name, None):
            raise RuntimeError('Duplicated test: %s' % name)

        setattr(cls, name, func)


# Add test to compare curses, only if available
@skipUnless(CURSES, 'Compare to curses on supported platforms')
class TestTParmCurses(TestCase):
    """
    Compare tparm() result to curses.tparm()
    """

    def test_dynamic_persistance(self):
        """
        Ensure dynamic variables persist between calls and compare to curses.tparm()
        """
        tparm(b'%p1%Px', 4)
        curses.tparm(b'%p1%Px', 4)
        self.assertEqual(tparm(b'%gx%d'), curses.tparm(b'%gx%d'))

    def test_static_persistance(self):
        """
        Ensure static variables persist between calls and compare to curses.tparm()
        """
        tparm(b'%p1%PX', 4)
        curses.tparm(b'%p1%PX', 4)
        self.assertEqual(tparm(b'%gX%d'), curses.tparm(b'%gX%d'))

    @classmethod
    def set_func(cls, desc, args, result):  # pylint: disable=unused-argument
        """
        Create a test method comparing the result of tparm() and curses.tparm()
        when both are called with the same arguments
        """

        name = 'test_%s' % desc

        def func(self):
            result = curses.tparm(*args)
            self.assertEqual(tparm(*args), result)

        func.__name__ = name
        if getattr(cls, name, None):
            raise RuntimeError('Duplicated test: %s' % name)

        setattr(cls, name, func)


for test in TESTS:
    TestTParmExamples.set_func(*test)
    if test[0] not in KNOWN_FAILURES:
        TestTParmCurses.set_func(*test)
