# -*- coding: utf-8 -*-
# Copyright 2019 Avram Lubkin, All Rights Reserved

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# The PyInstaller compatibility module inside jinxed was originally authored by @Legorooj


def test_jinxed(pyi_builder):
    pyi_builder.test_source('''import jinxed

jinxed.setupterm('xterm')
assert jinxed._terminal.TERM.terminfo is jinxed.terminfo.xterm''')
