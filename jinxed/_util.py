# -*- coding: utf-8 -*-
# Copyright 2019 Avram Lubkin, All Rights Reserved

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
Utility objects
"""

import os
import sys

if sys.version_info[0] < 3:  # pragma: no branch
    BASESTRING = basestring  # pragma: no cover  # noqa: F821 # pylint: disable=undefined-variable
else:
    BASESTRING = str


class error(Exception):  # pylint: disable=invalid-name
    """
    Generic class for Jinxed errors
    """


def get_term(*args, **kwargs):  # pylint: disable=unused-argument
    """
    A lightweight stand-in for win32.get_term() for non-Windows platforms
    Returns value of TERM environment variable or 'unknown'
    """

    return os.environ.get('TERM', 'unknown')
