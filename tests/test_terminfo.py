# -*- coding: utf-8 -*-
# Copyright 2019 Avram Lubkin, All Rights Reserved

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

import jinxed.terminfo

from tests import TestCase


class TestTermInfo(TestCase):
    """
    Validate terminfo
    """

    @ classmethod
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

        func.__name__ = name
        if getattr(cls, name, None):
            raise RuntimeError('Duplicated test: %s' % name)

        setattr(cls, name, func)


for mod in pkgutil.iter_modules([os.path.dirname(jinxed.terminfo.__file__)]):
    TestTermInfo.set_func(mod[1])
