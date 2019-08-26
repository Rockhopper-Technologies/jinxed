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

Jinxed is an implementation of a subset of the Python :py:mod:`curses` library for Windows

Jinxed is intended primarily for libraries that need to access terminfo functions
such as tigetstr() and tparm() and was written specifically to support Blessed_ on Windows.

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