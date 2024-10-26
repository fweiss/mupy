import sys
# wound up just puttin ffmpeg in the project directory
sys.path.append('E:\\Projects\\Music\\mupy\\bin')

from pydub.generators import Sine, Sawtooth
from pydub.playback import play
from pydub import AudioSegment
import pydub.scipy_effects

# Define the duration for each note (in milliseconds)
# k216 allegro quarter note ~ 126 bpm
bpm = 126
whole_note_duration = 4 * 60 / bpm * 1000

##################################################################
# override some pydub functions to make it easier to work with

# use "^" to staccato a note
def staccato(note, ratio=0.5):
    note_duration = len(note)
    staccato_ratio = 0.5  # This will reduce the note length to 50%
    staccato_note = note[:int(note_duration * staccato_ratio)]
    silence_duration = int(note_duration * (1 - staccato_ratio))  # Silence to mimic staccato rest
    silence = AudioSegment.silent(duration=silence_duration)
    return staccato_note + silence
AudioSegment.__xor__ = staccato

# use "/" to shorten a note
# ratio_exponent is the power of 2 to shorten the note by
# base duration is quarter note
def shorten(note, ratio_exponent=0):
    note_duration = len(note)
    shorten_note =  note[:int(note_duration / (1 << (ratio_exponent - 0)))]
    return shorten_note
AudioSegment.__truediv__ = shorten

# force a crossfade to remove click betwee notes
def crossfade(self, arg):
    if isinstance(arg, AudioSegment):
        return self.append(arg, crossfade=7)
    else:
        return self.apply_gain(arg)
AudioSegment.__add__ = crossfade

# pattern for defiing a whole note
def N(frequency):
    return Sawtooth(frequency).to_audio_segment(duration=whole_note_duration)

# Define a whole rest
Z = AudioSegment.silent(duration=whole_note_duration)

# Define the whole notes
C2 = N(65.41)
C2s = N(69.30)
D2 = N(73.42)
D2s = N(77.78)
E2 = N(82.41)
F2 = N(87.31)
F2s = N(92.50)
G2 = N(98.00)
G2s = N(103.83)
A2 = N(110.00)
A2s = N(116.54)
B2 = N(123.47)

C3 = N(130.81)
C3s = N(138.59)
D3 = N(146.83)
D3s = N(155.56)
E3 = N(164.81)
F3 = N(174.61)
F3s = N(185.00)
G3 = N(196.00)
G3s = N(207.65)
A3 = N(220.00)
A3s = N(233.08)
B3 = N(246.94)

C4 = N(261.63)
C4s = N(277.18)
D4 = N(293.66)
D4s = N(311.13)
E4 = N(329.63)
F4 = N(349.23)
F4s = N(369.99)
G4 = N(392.00)
G4s = N(415.30)
A4 = N(440.00)
A4s = N(466.16)
B4 = N(493.88)

C5 = N(523.25)
C5s = N(554.37)
D5 = N(587.33)
D5s = N(622.25)
E5 = N(659.25)
F5 = N(698.46)
F5s = N(739.99)
G5 = N(783.99)
G5s = N(830.61)
A5 = N(880.00)
A5s = N(932.33)
B5 = N(987.77)

C6 = N(1046.50)
C6s = N(1108.73)
D6 = N(1174.66)
D6s = N(1244.51)
E6 = N(1318.51)
F6 = N(1396.91)
G6 = N(1567.98)
A6 = N(1760.00)
B6 = N(1975.53)


# nice part starts on page 2 at "D"
# melody = B5 + Z + A5 + Z + G4 + Z + F4 + Z + E4 + Z + D4 + Z + C4 + Z + B4 + Z + D4
scale = C2 + D2 + E2 + F2 + G2 + A2 + B2 + C3 + D3 + E3 + F3 + G3 + A3 + B3 + C4 + D4 + E4 + F4 + G4 + A4 + B4 + C5 + D5 + E5 + F5 + G5 + A5 + B5 + C6 # + D6 + E6 + F6 + G6 + A6 + B6 + C7 + D7 + E7 + F7 + G7 + A7 + B7 + C8

melody = Z/2
melody += (A5/4^1) + (A5/4^1) + (A5/3^1) + (G5s/3^1) + (A5/3^1) + (G5s/3^1) + (A5/2) + (Z/3)
melody += D6/3 + C6s/3 + D6/3 + F5s/3 + B5/3 + A5/3 + G5/3 + (Z/3)
melody += (G5/4^1) + (G5/4^1) + (G5/3^1) + (F5s/3^1) + (G5/3^1) + (F5s/3^1) + (G5/2) + (Z/3)
melody += (D6s/3) + (E6/3) + (G5s/3) + (A5/3) + (E5/3) + (G5/3) + (F5s/3) + (Z/3)

melody += (A5/4^1) + (F5s/4^1) + (D5/4) + (A4/4) + (F4s/4^1) + (D4/4^1) + (G4/4) + (E4/4) + (C4s/4^1) + (A3/4^1)
melody += (F4s/4) + (D4/4) + (G4/4) + (E4/4) + (A4/3^1)
melody += (A5/4^1) + (F5s/4^1) + (D5/4) + (A4/4) + (F4s/4^1) + (D4/4^1) + (G4/4) + (E4/4) + (C4s/4^1) + (A3/4^1)
melody += (F4s/4) + (D4/4) + (G4/4) + (E4/4) + (A4/3) + (Z/3) + (Z/1)

melody += (Z/2) + (Z/3) +(A4/4^1) + (F4s/4^1) + (B4/4^1) + (G4/4^1) + (C5s/4^1) + (A4/4^1) + (D5/4) + (A4/4) + (E5/4) + (C5s/4)
melody += (F5s/4^1) + (D5/4^1) + (G5/4^1) + (E5/4^1) + (A5/4^1) + (F5s/4^1) + (A5s/4^1) + (F5s/4^1) + (B5/2) + (D6/2)
melody += (E5/1) + (E5/4) + (F5s/4) + (G5/4) + (F5s/4) + (A5/4) + (G5/4) + (F5s/4) + (E5/4) + (D5/2)

# like b6
# but the pop was due to the sound card
# no_pop = melody.low_pass_filter(8000, order=3)

# play(melody)
melody.export("melody.wav", format="wav")
