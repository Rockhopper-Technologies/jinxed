# -*- coding: utf-8 -*-
# Copyright 2019 Avram Lubkin, All Rights Reserved

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
Test module for Jinxed
"""

import unittest


# Fix deprecated methods for Python 2
class TestCase(unittest.TestCase):
    """
    Subclass of unittest.TestCase for customization
    """


if not hasattr(TestCase, 'assertRegex'):
    TestCase.assertRegex = TestCase.assertRegexpMatches

if not hasattr(TestCase, 'assertNotRegex'):
    TestCase.assertNotRegex = TestCase.assertNotRegexpMatches

if not hasattr(TestCase, 'assertRaisesRegex'):
    TestCase.assertRaisesRegex = TestCase.assertRaisesRegexp
