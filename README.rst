
Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-rtttl/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/rtttl/en/latest/
    :alt: Documentation Status

.. image :: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

.. image:: https://travis-ci.com/adafruit/Adafruit_CircuitPython_RTTTL.svg?branch=master
    :target: https://travis-ci.com/adafruit/Adafruit_CircuitPython_RTTTL
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

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_rtttl/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Building locally
================

To build this library locally you'll need to install the
`circuitpython-build-tools <https://github.com/adafruit/circuitpython-build-tools>`_ package.

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install circuitpython-build-tools

Once installed, make sure you are in the virtual environment:

.. code-block:: shell

    source .env/bin/activate

Then run the build:

.. code-block:: shell

    circuitpython-build-bundles --filename_prefix adafruit-circuitpython-rtttl --library_location .

Sphinx documentation
-----------------------

Sphinx is used to build the documentation based on rST files and comments in the code. First,
install dependencies (feel free to reuse the virtual environment from above):

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install Sphinx sphinx-rtd-theme

Now, once you have the virtual environment activated:

.. code-block:: shell

    cd docs
    sphinx-build -E -W -b html . _build/html

This will output the documentation to ``docs/_build/html``. Open the index.html in your browser to
view them. It will also (due to -W) error out on any warning like Travis will. This is a good way to
locally verify it will pass.

