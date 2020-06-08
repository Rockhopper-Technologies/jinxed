  
# -*- coding: utf-8 -*-
# Copyright 2019 Avram Lubkin, All Rights Reserved

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# The PyInstaller compatibility module inside jinxed was originally authored by @Legorooj
import os


def get_hook_dirs():
    return [os.abspath(os.dirname(__file__))]
    

def get_test_dirs():
    return [os.abspath(os.dirname(__file__))]
