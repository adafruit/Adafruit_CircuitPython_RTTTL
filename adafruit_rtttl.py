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

TODO(description)

* Author(s): Scott Shawcroft
"""

from adafruit_waveform import sine
import simpleio
import audioio
import time

piano = {"4a#": 466.16,
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

def play(pin, rtttl, octave=None, duration=None, tempo=None):
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

    min_freq = 13000

    for note in tune.split(","):
        p = None
        if note[0].isdigit():
            p = note[1]
        else:
            p = note[0]
        if "#" in note:
            p += "#"
        o = octave
        if note[-1].isdigit():
            o = note[-1]
        p = o + p
        if p[-1] != "p" and piano[p] < min_freq:
            min_freq = piano[p]
    wave = sine.sine_wave(16000, min_freq)
    try:
        base_tone = audioio.AudioOut(pin, wave)
        for note in tune.split(","):
            p = None
            d = duration
            if note[0].isdigit():
                d = int(note[0])
                p = note[1]
            else:
                p = note[0]
            if "." in note:
                d *= 1.5
            if "#" in note:
                p += "#"
            o = octave
            if note[-1].isdigit():
                o = note[-1]
            p = o + p
            if p in piano:
                base_tone.frequency = int(16000 * (piano[p] / min_freq))
                base_tone.play(loop=True)
            print(p, d)
            time.sleep(4 / d * 60 / tempo)
            base_tone.stop()
            time.sleep(0.02)
    except(ValueError):
        for note in tune.split(","):
            p = None
            d = duration
            if note[0].isdigit():
                d = int(note[0])
                p = note[1]
            else:
                p = note[0]
            if "." in note:
                d *= 1.5
            if "#" in note:
                p += "#"
            o = octave
            if note[-1].isdigit():
                o = note[-1]
            p = o + p
            if p in piano:
                base_tone_frequency = int(1600 * (piano[p] / min_freq))
                base_tone = simpleio.tone(pin, base_tone_frequency, 1)
            print(p, d)
            time.sleep(4 / d * 60 / tempo)
            base_tone_frequency = 20000
            time.sleep(0.02)
