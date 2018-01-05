# The MIT License (MIT)
#
# Copyright (c) 2017 Scott Shawcroft for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`adafruit_rtttl`
====================================================

Play notes to a digialio pin using ring tone text transfer language (rtttl).

* Author(s): Scott Shawcroft
"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_RTTTL"

import time
from adafruit_waveform import sine
import audioio

PIANO = {"4a#": 466.16,
         "4b" : 493.88,
         "5c" : 523.25,
         "5c#": 554.37,
         "5d" : 587.33,
         "5d#": 622.25,
         "5e" : 659.26,
         "5f" : 698.46,
         "5f#": 739.99,
         "5g" : 783.99,
         "5g#": 830.61,
         "5a" : 880,
         "5a#": 932.33,
         "5b" : 987.77,
         "6c" : 1046.5,
         "6c#": 1108.7,
         "6d" : 1174.7,
         "6d#": 1244.5,
         "6e" : 1318.5,
         "6f" : 1396.9,
         "6f#": 1480,
         "6g" : 1568,
         "6g#": 1661.2,
         "6a" : 1760,
         "6a#": 1864.7,
         "6b" : 1975.5,
         "7c" : 2093,
         "7c#": 2217.5}

def _get_wave(tune, octave):
    """Returns the proper waveform to play the song along with the minimum
    frequency in the song.
    """
    min_freq = 13000

    for note in tune.split(","):
        piano_note = None
        if note[0].isdigit():
            piano_note = note[1]
        else:
            piano_note = note[0]
        if "#" in note:
            piano_note += "#"
        note_octave = octave
        if note[-1].isdigit():
            note_octave = note[-1]
        piano_note = note_octave + piano_note
        if piano_note[-1] != "p" and PIANO[piano_note] < min_freq:
            min_freq = PIANO[piano_note]
    return sine.sine_wave(16000, min_freq), min_freq


#pylint: disable-msg=too-many-arguments
def _play_to_pin(tune, base_tone, min_freq, duration, octave, tempo):
    """Using the prepared input send the notes to the pin
    """
    for note in tune.split(","):
        piano_note = None
        note_duration = duration
        if note[0].isdigit():
            note_duration = int(note[0])
            piano_note = note[1]
        else:
            piano_note = note[0]
        if "." in note:
            note_duration *= 1.5
        if "#" in note:
            piano_note += "#"
        note_octave = octave
        if note[-1].isdigit():
            note_octave = note[-1]
        piano_note = note_octave + piano_note
        if piano_note in PIANO:
            base_tone.frequency = int(16000 * (PIANO[piano_note] / min_freq))
            base_tone.play(loop=True)
        print(piano_note, note_duration)
        time.sleep(4 / note_duration * 60 / tempo)
        base_tone.stop()
        time.sleep(0.02)

#pylint: disable-msg=too-many-arguments
def play(pin, rtttl, octave=None, duration=None, tempo=None):
    """Play notes to a digialio pin using ring tone text transfer language (rtttl).
    :param ~digitalio.DigitalInOut pin: the speaker pin
    :param rtttl: string containing rtttl
    :param int octave: represents octave number (default 6 starts at middle c)
    :param int duration: length of notes (default 4 quarter note)
    :param int tempo: how fast (default 63 beats per minute)
    """
    _, defaults, tune = rtttl.split(":")
    for default in defaults.split(","):
        if default[0] == "d" and not duration:
            duration = int(default[2:])
        elif default[0] == "o" and not octave:
            octave = default[2:]
        elif default[0] == "b" and not tempo:
            tempo = int(default[2:])
    if not octave:
        octave = 6
    if not duration:
        duration = 4
    if not tempo:
        tempo = 63

    print("tempo", tempo, "octave", octave, "duration", duration)

    wave, min_freq = _get_wave(tune, octave)

    base_tone = audioio.AudioOut(pin, wave)

    _play_to_pin(tune, base_tone, min_freq, duration, octave, tempo)
