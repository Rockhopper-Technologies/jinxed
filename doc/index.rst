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
functions on all platforms, backed by a bundled virtual terminfo database.  It was written
initially to support `Blessed <https://pypi.org/project/blessed>`_ on Windows, and now
serves as its sole terminfo provider on all platforms.

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