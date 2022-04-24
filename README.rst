
Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-rtttl/badge/?version=latest
    :target: https://docs.circuitpython.org/projects/rtttl/en/latest/
    :alt: Documentation Status

.. image:: https://raw.githubusercontent.com/adafruit/Adafruit_CircuitPython_Bundle/main/badges/adafruit_discord.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_RTTTL/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_RTTTL/actions/
    :alt: Build Status

This plays `RTTTL <https://en.wikipedia.org/wiki/Ring_Tone_Transfer_Language>`_ melodies.

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Adafruit CircuitPython Waveform <https://github.com/tannewt/Adafruit_CircuitPython_Waveform>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Installing from PyPI
====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-rtttl/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-rtttl

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-rtttl

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-rtttl

Usage Example
=============

This plays Frosty the Snowman:

.. code-block:: python

    import board
    import adafruit_rtttl

    adafruit_rtttl.play(board.A0, "Snowman:d=8,o=5,b=200:2g,4e.,f,4g,2c6,b,c6,4d6,4c6,4b,a,2g.,b,c6,4d6,4c6,4b,a,a,g,4c6,4e.,g,a,4g,4f,4e,4d,2c.,4c,4a,4a,4c6,4c6,4b,4a,4g,4e,4f,4a,4g,4f,2e.,4e,4d,4d,4g,4g,4b,4b,4d6,d6,b,4d6,4c6,4b,4a,4g,4p,2g")

CPX Usage Example
=================

This plays Frosty the Snowman on a Circuit Playground Express (we must enable onboard speaker):

.. code-block:: python

    import board
    from digitalio import DigitalInOut, Direction
    import adafruit_rtttl
    spkrenable = DigitalInOut(board.SPEAKER_ENABLE)
    spkrenable.direction = Direction.OUTPUT
    spkrenable.value = True

    adafruit_rtttl.play(board.A0, "Snowman:d=8,o=5,b=200:2g,4e.,f,4g,2c6,b,c6,4d6,4c6,4b,a,2g.,b,c6,4d6,4c6,4b,a,a,g,4c6,4e.,g,a,4g,4f,4e,4d,2c.,4c,4a,4a,4c6,4c6,4b,4a,4g,4e,4f,4a,4g,4f,2e.,4e,4d,4d,4g,4g,4b,4b,4d6,d6,b,4d6,4c6,4b,4a,4g,4p,2g")

Documentation
=============

API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/rtttl/en/latest/>`_.

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_rtttl/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
