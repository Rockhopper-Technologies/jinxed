..
  Copyright 2019 Avram Lubkin, All Rights Reserved

  This Source Code Form is subject to the terms of the Mozilla Public
  License, v. 2.0. If a copy of the MPL was not distributed with this
  file, You can obtain one at http://mozilla.org/MPL/2.0/.

:github_url: https://github.com/Rockhopper-Technologies/jinxed

Frequently Asked Questions
==========================

Why is Jinxed called Jinxed?
----------------------------------

Jinxed was written to support blessed_ on Windows. We originally wanted to call it Cursed,
to continue the theme, but the name was taken. Jinxed is a synonym for cursed.

Can you add support for a terminal?
-----------------------------------

A select few terminals from the `terminfo(5)`_ database were included to reduce packaging
size. Many historic and unlikely terminal types, like ``avatar``, were excluded.

If we are missing support for a terminal, please let us know its unique ``TERM`` name
and whether it is in the `terminfo(5)`_ database, or provide an equivalent reference. To submit,
`create an issue <https://github.com/Rockhopper-Technologies/jinxed/issues>`_
or `pull request <https://github.com/Rockhopper-Technologies/jinxed/pulls>`_.

We can also provide stubs for terminal capabilities, like what was done with the (now legacy) win32 
console. Not all terminals can be supported, there a few requirements:

1. The terminal must be detectable programmatically

   We need to be able to identify the terminal in some reasonable way
   and differentiate it from other terminals. This could be through
   environment variables (e.g. ``TERM``), the :py:mod:`platform` module, ``TTYPE`` telnet negotiation, or some other method.

2. Virtual terminal codes must be supported and documented

   While not all codes need to be supported, a majority of them should be

3. Terminal dimensions must be detectable

   The height and width of the terminal must be available to the running process.

4. The terminal should support modes similar to cbreak and raw

.. _blessed: https://pypi.org/project/blessed
.. _`terminfo(5)`: https://invisible-island.net/ncurses/man/terminfo.5.html
