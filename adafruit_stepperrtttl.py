# SPDX-FileCopyrightText: 2017, 2018 Scott Shawcroft for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_stepperrtttl`
====================================================

Play notes to a digialio pin using ring tone text transfer language (rtttl).

* Author(s): Scott Shawcroft, Alec Delaney
"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/tekktrik/Adafruit_CircuitPython_StepperRTTTL"

import sys
import time
import pwmio
import gc

try:
    from typing import Optional, Tuple
    import tic_driver.motor.cpy
    from tic_driver.constants import StepMode
except ImportError:
    pass

C3_NOTE = 33.37
C4_NOTE = 66.74
C5_NOTE = 133.48
C6_NOTE = 266.96

HALF_STEP_FACTOR = 1.059463

PIANO = {}
NOTES_LIST = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"]
OCTAVES_LIST = range(3, 7)
last_note = C3_NOTE

for octave in OCTAVES_LIST:
    for note in NOTES_LIST:
        PIANO[str(int(octave)) + note] = last_note
        last_note *= HALF_STEP_FACTOR
gc.collect()

#PIANO = {
#    "4c": 261.626,
#    "4c#": 277.183,
#    "4d": 293.665,
#    "4d#": 311.127,
#    "4e": 329.628,
#    "4f": 349.228,
#    "4f#": 369.994,
#    "4g": G5_NOTE / 2, # start
#    "4g#": G5_NOTE * G_TO_GSHARP,
#    "4a": 440,
#    "4a#": 466.164,
#    "4b": 493.883,
#    "5c": 523.251,
#    "5c#": 554.365,
#    "5d": 587.330,
#    "5d#": 622.254,
#    "5e": 659.255,
#    "5f": 698.456,
#    "5f#": 739.989,
#    "5g": G5_NOTE, # 
#    "5g#": G5_NOTE * G_TO_GSHARP,
#    "5a": G5_NOTE * G_TO_A,
#    "5a#": G5_NOTE * G_TO_ASHARP,
#    "5b": G5_NOTE * G_TO_B,
#    "6c": G5_NOTE * G_TO_C,
#    "6c#": G5_NOTE * G_TO_CSHARP,
#    "6d": G5_NOTE * G_TO_D,
#    "6d#": G5_NOTE * G_TO_DSHARP,
#    "6e": G5_NOTE * G_TO_E,
#    "6f": G5_NOTE * G_TO_F,
#    "6f#": G5_NOTE * G_TO_FSHARP,
#    "6g": G5_NOTE * 2,
#    "6g#": 1661.22,
#    "6a": 1760,
#    "6a#": 1864.66,
#    "6b": 1975.53,
#    "7c": 2093,
#    "7c#": 2217.46,
#}


def _parse_note(note: str, duration: int = 2, octave: int = 6) -> Tuple[str, float]:
    note = note.strip()
    piano_note = None
    note_duration = duration
    if note[0].isdigit() and note[1].isdigit():
        note_duration = int(note[:2])
        piano_note = note[2]
    elif note[0].isdigit():
        note_duration = int(note[0])
        piano_note = note[1]
    else:
        piano_note = note[0]
    if "." in note:
        note_duration *= 1.5
    if "#" in note:
        piano_note += "#"
    note_octave = str(octave)
    if note[-1].isdigit():
        note_octave = note[-1]
    piano_note = note_octave + piano_note
    return piano_note, note_duration

def _play_to_stepper(
    tune: str,
    motor,
    duration: int,
    octave: int,
    tempo: int,
) -> None:
    for note in tune.split(","):
        piano_note, note_duration = _parse_note(note, duration, octave)
        if piano_note in PIANO:
            motor.drive(PIANO[piano_note])

        time.sleep(4 / note_duration * 60 / tempo)
        motor.drive(0)
        time.sleep(0.02)


# pylint: disable-msg=too-many-arguments
def play(
    motor,
    rtttl: str,
    octave: Optional[int] = None,
    duration: Optional[int] = None,
    tempo: Optional[int] = None,
) -> None:
    """Play notes to a digialio pin using ring tone text transfer language (rtttl).
    :param ~digitalio.DigitalInOut pin: the speaker pin
    :param str rtttl: string containing rtttl
    :param int octave: represents octave number (default 6 starts at middle c)
    :param int duration: length of notes (default 4 quarter note)
    :param int tempo: how fast (default 63 beats per minute)
    """
    _, defaults, tune = rtttl.lower().split(":")
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

    base_tone = None

    _play_to_stepper(tune, motor, duration, octave, tempo)
