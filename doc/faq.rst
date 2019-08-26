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

Jinxed was written to support Blessed_ on Windows. We originally want to call it Cursed,
to continue the theme, but the name was taken. Jinxed is a synonym for cursed.


Can you add support for _______ terminal?
---------------------------------------------------

We are happy to add support for as many terminals as we can.
However, not all terminals can be supported. There a few requirements.

  1. The terminal must be detectable programmatically

      We need to be able to identify the terminal in some reasonable way
      and differentiate it from other terminals. This could be through environment variables,
      the :py:mod:`platform` module, or some other method.

  2. Virtual terminal codes must be supported and documented

      While not all codes need to be supported, a majority of them should be

  3. Terminal dimensions must be detectable

      The height and width of the terminal must be available to the running process.

  4. The terminal should support modes similar to cbreak and raw


.. _Blessed: https://pypi.org/project/blessed
