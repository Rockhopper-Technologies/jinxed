# -*- coding: utf-8 -*-
# Copyright 2019 - 2024 Avram Lubkin, All Rights Reserved

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
Test module for jinxed.terminfo

Basic tests to make sure there are no syntax errors and all required attributes exist
"""

import importlib
import os
import pkgutil
import re

import jinxed.terminfo

from tests import TestCase

# Patterns that must NOT appear in any STR_CAPS value
_G0_G1 = re.compile(b'\x1b[()][0ABUK]')
_DELAY = re.compile(b'\\$<[^>]+>')

# Capabilities that must be present but empty (b'') in STR_CAPS
_EMPTY_CAPS = frozenset({'smacs', 'rmacs', 'enacs', 's0ds', 's1ds'})


class TestTermInfo(TestCase):
    """
    Validate terminfo
    """

    @classmethod
    def set_func(cls, term):
        """
        Create a test method checking for required attributes
        """

        name = 'test_%s' % term

        def func(self):

            module = importlib.import_module('jinxed.terminfo.%s' % term)

            self.assertIsInstance(module.BOOL_CAPS, list)
            self.assertIsInstance(module.NUM_CAPS, dict)
            self.assertIsInstance(module.STR_CAPS, dict)

            # Empty caps must be present and empty
            for cap_name in _EMPTY_CAPS:
                self.assertIn(cap_name, module.STR_CAPS,
                              '{}: missing empty cap {}'.format(term, cap_name))
                self.assertEqual(module.STR_CAPS[cap_name], b'',
                                 '{}.{}: expected b"", got {!r}'.format(
                                     term, cap_name, module.STR_CAPS[cap_name]))

            # No G0/G1 designation sequences or delay tokens in any STR_CAPS
            for cap_name, cap_value in module.STR_CAPS.items():
                self.assertIsNone(
                    _G0_G1.search(cap_value),
                    '{}.{}: contains G0/G1 designation'.format(term, cap_name),
                )
                self.assertIsNone(
                    _DELAY.search(cap_value),
                    '{}.{}: contains delay token'.format(term, cap_name),
                )

        func.__name__ = name
        if getattr(cls, name, None):
            raise RuntimeError('Duplicated test: %s' % name)

        setattr(cls, name, func)


for mod in pkgutil.iter_modules([os.path.dirname(jinxed.terminfo.__file__)]):
    if mod[1].startswith('_'):
        continue
    TestTermInfo.set_func(mod[1])
