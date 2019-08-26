.. start-badges

| |supported-platforms|
| |docs| |appveyor| |travis|
| |pypi| |supported-versions| |supported-implementations|

.. |docs| image:: https://img.shields.io/readthedocs/jinxed.svg?style=plastic
    :target: https://jinxed.readthedocs.org
    :alt: Documentation Status

.. |appveyor| image:: https://img.shields.io/appveyor/ci/Rockhopper-Technologies/jinxed.svg?style=plastic
    :target: https://ci.appveyor.com/project/Rockhopper-Technologies/jinxed
    :alt: Appveyor Build Status

.. |travis| image:: https://img.shields.io/travis/Rockhopper-Technologies/jinxed.svg?style=plastic
    :target: https://travis-ci.org/Rockhopper-Technologies/jinxed
    :alt: Travis-CI Build Status

.. |pypi| image:: https://img.shields.io/pypi/v/jinxed.svg?style=plastic
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/ansicon

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/jinxed.svg?style=plastic
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/ansicon

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/jinxed.svg?style=plastic
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/ansicon

.. |supported-platforms| image:: https://img.shields.io/badge/platforms-Windows-blue.svg?style=plastic
    :alt: Supported platforms

.. end-badges

Overview
========
Jinxed is an implementation of a subset of the Python curses library for Windows.

Jinxed is intended primarily for libraries that need to access terminfo functions
such as tigetstr() and tparm() and was written specifically to support Blessed_ on Windows.

Installation
============

.. code-block:: console

    $ pip install jinxed

Documentation
=============

Jinxed documentation can be found on `Read the Docs <https://jinxed.readthedocs.io/en/stable/>`_.

.. _Blessed: https://pypi.org/project/blessed
