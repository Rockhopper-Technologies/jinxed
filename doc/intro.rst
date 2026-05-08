..
  Copyright 2019 - 2026 Avram Lubkin, All Rights Reserved

  This Source Code Form is subject to the terms of the Mozilla Public
  License, v. 2.0. If a copy of the MPL was not distributed with this
  file, You can obtain one at http://mozilla.org/MPL/2.0/.

.. start-badges

| |docs| |gh_actions| |codecov|
| |pypi| |supported-versions| |supported-implementations|
| |linux| |windows| |mac| |bsd|

.. |docs| image:: https://img.shields.io/readthedocs/jinxed.svg?style=plastic&logo=read-the-docs
    :target: https://jinxed.readthedocs.org
    :alt: Documentation Status

.. |appveyor| image:: https://img.shields.io/appveyor/ci/Rockhopper-Technologies/jinxed.svg?style=plastic&logo=appveyor
    :target: https://ci.appveyor.com/project/Rockhopper-Technologies/jinxed
    :alt: Appveyor Build Status

.. |gh_actions| image:: https://img.shields.io/github/actions/workflow/status/Rockhopper-Technologies/jinxed/tests.yml?event=push&logo=github-actions&style=plastic
    :target: https://github.com/Rockhopper-Technologies/jinxed/actions/workflows/tests.yml
    :alt: GitHub Actions Status

.. |travis| image:: https://img.shields.io/travis/com/Rockhopper-Technologies/jinxed.svg?style=plastic&logo=travis
    :target: https://travis-ci.com/Rockhopper-Technologies/jinxed
    :alt: Travis-CI Build Status

.. |codecov| image:: https://img.shields.io/codecov/c/github/Rockhopper-Technologies/jinxed.svg?style=plastic&logo=codecov
    :target: https://codecov.io/gh/Rockhopper-Technologies/jinxed
    :alt: Coverage Status

.. |pypi| image:: https://img.shields.io/pypi/v/jinxed.svg?style=plastic&logo=pypi
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/jinxed

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/jinxed.svg?style=plastic&logo=pypi
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/jinxed

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/jinxed.svg?style=plastic&logo=pypi
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/jinxed

.. |linux| image:: https://img.shields.io/badge/Linux-yes-success?style=plastic&logo=linux
    :alt: Linux supported
    :target: https://pypi.python.org/pypi/jinxed

.. |windows| image:: https://img.shields.io/badge/Windows-yes-success?style=plastic&logo=windows
    :alt: Windows supported
    :target: https://pypi.python.org/pypi/jinxed

.. |mac| image:: https://img.shields.io/badge/MacOS-yes-success?style=plastic&logo=apple
    :alt: MacOS supported
    :target: https://pypi.python.org/pypi/jinxed

.. |bsd| image:: https://img.shields.io/badge/BSD-yes-success?style=plastic&logo=freebsd
    :alt: BSD supported
    :target: https://pypi.python.org/pypi/jinxed

.. end-badges

Introduction
============

Jinxed is a pure-Python implementation of a subset of the Python curses_ library.

It provides `jinxed.tigetstr()`_, `jinxed.tparm()`_, and related terminfo
functions on all platforms with a virtual `terminfo(5)`_ database.

Jinxed provides pure-python implementations of curses_ functions:

- `setupterm()`_ as `jinxed.setupterm()`_
- `tigetflag()`_ as `jinxed.tigetflag()`_
- `tigetnum()`_ as `jinxed.tigetnum()`_
- `tigetstr()`_ as `jinxed.tigetstr()`_
- `tparm()`_ as `jinxed.tparm()`_

Although Jinxed was created primarily to be a dependency to supply Windows support for the
`blessed`_ 1.16 release for lightweight sequences for the (now legacy) win32 Console API, it has
since been extended to contain a subset of the ncurses 6.6 `terminfo(5)`_ database and to allow
dynamic injection capabilities for `XTGETTCAP`_ support, demonstrated in blessed_ 1.40.

Further documentation can be found on `Read the Docs <https://jinxed.readthedocs.io/en/stable/>`_.

Installation
------------

.. code-block:: console

    $ pip install jinxed

Source
------

Source is available `on GitHub <https://github.com/Rockhopper-Technologies/jinxed>`_

Issues
------

Please report issues `on GitHub <https://github.com/Rockhopper-Technologies/jinxed/issues>`_

.. _curses: https://docs.python.org/library/curses.html
.. _blessed: https://pypi.org/project/blessed
.. _XTGETTCAP: https://codeberg.org/dnkl/foot#xtgettcap
.. _`jinxed.setupterm()`: https://jinxed.readthedocs.io/en/stable/api.html#jinxed.setupterm
.. _`jinxed.tigetflag()`: https://jinxed.readthedocs.io/en/stable/api.html#jinxed.tigetflag
.. _`jinxed.tigetnum()`: https://jinxed.readthedocs.io/en/stable/api.html#jinxed.tigetnum
.. _`jinxed.tigetstr()`: https://jinxed.readthedocs.io/en/stable/api.html#jinxed.tigetstr
.. _`jinxed.tparm()`: https://jinxed.readthedocs.io/en/stable/api.html#jinxed.tparm
.. _`setupterm()`: https://docs.python.org/library/curses.html#curses.setupterm
.. _`terminfo(5)`: https://man7.org/linux/man-pages/man5/terminfo.5.html
.. _`terminfo.src`: https://invisible-island.net/ncurses/terminfo.src.html
.. _`tigetflag()`: https://docs.python.org/library/curses.html#curses.tigetflag
.. _`tigetflag()`: https://docs.python.org/library/curses.html#curses.tigetflag
.. _`tigetnum()`: https://docs.python.org/library/curses.html#curses.tigetnum
.. _`tigetnum()`: https://docs.python.org/library/curses.html#curses.tigetnum
.. _`tigetstr()`: https://docs.python.org/library/curses.html#curses.tigetstr
.. _`tigetstr()`: https://docs.python.org/library/curses.html#curses.tigetstr
.. _`tparm()`: https://docs.python.org/library/curses.html#curses.tparm
