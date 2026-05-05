..
  Copyright 2019 Avram Lubkin, All Rights Reserved

  This Source Code Form is subject to the terms of the Mozilla Public
  License, v. 2.0. If a copy of the MPL was not distributed with this
  file, You can obtain one at http://mozilla.org/MPL/2.0/.

:github_url: https://github.com/Rockhopper-Technologies/jinxed

.. toctree::
   :hidden:

   self
   faq.rst
   api.rst


Overview
========

Jinxed is a pure-Python implementation of a subset of the Python :py:mod:`curses` library.

It provides :py:func:`~jinxed.tigetstr`, :py:func:`~jinxed.tparm`, and related terminfo
functions on all platforms with a simplified terminfo(5) database derived from ncurses.

Jinxed was created primarily to be a dependency to supply Windows support for the `blessed`_ 1.16
release through the win32 Console API.  It has since been extended to contain a subset of the
ncurses 6.6 `terminfo(5)`_ database, and, to allow dynamic injection `XTGETTCAP`_, demonstrated in
the first curses-free blessed_ 1.40 release.

.. _blessed: https://pypi.org/project/blessed
.. _`terminfo(5)`: https://invisible-island.net/ncurses/man/terminfo.5.html

Installation
------------

.. code-block:: console

    $ pip install jinxed


.. _Blessed: https://pypi.org/project/blessed

Source
------

Source is available on `GitHub <https://github.com/Rockhopper-Technologies/jinxed>`_

Issues
------

Please report issues `here <https://github.com/Rockhopper-Technologies/jinxed/issues>`_.
