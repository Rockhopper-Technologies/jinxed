#!/usr/bin/env python
# Copyright 2019 Avram Lubkin, All Rights Reserved

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
Jinxed Terminal Library

Jinxed is an implementation of a subset of the Python curses library for Windows

Other libraries implement the full curses stack. Jinxed is intended primarily for libraries
that need to access terminfo functions such as tigetstr() and tparm().
"""

import os
import platform

from setuptools import setup

from setup_helpers import get_version, readme

INSTALL_REQUIRES = []
# Require ansicon for Windows versions older than 10.0.10586
if platform.system() == 'Windows' and \
   tuple(int(num) for num in platform.version().split('.')) < (10, 0, 10586):
    INSTALL_REQUIRES.append('ansicon')


setup(
    name='jinxed',
    version=get_version(os.path.join('jinxed', '__init__.py')),
    description="Jinxed Terminal Library",
    long_description=readme('README.rst'),
    author='Avram Lubkin',
    author_email='avylove@rockhopper.net',
    maintainer='Avram Lubkin',
    maintainer_email='avylove@rockhopper.net',
    url='https://github.com/Rockhopper-Technologies/ansicon',
    license='MPLv2.0',
    zip_safe=False,
    install_requires=INSTALL_REQUIRES,
    tests_require=[],
    packages=['jinxed'],
    test_suite='tests',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Utilities',
    ],
    keywords='terminal console blessed curses',
)
