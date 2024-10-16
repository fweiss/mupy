import sys
# wound up just puttin ffmpeg in the project directory
sys.path.append('E:\\Projects\\Music\\mupy\\bin')

from pydub.generators import Sine
from pydub.playback import play
from pydub import AudioSegment

# Define the duration for each note (in milliseconds)
duration = 500  # ms for each note

def staccato(note, ratio=0.5):
    note_duration = len(note)
    staccato_ratio = 0.5  # This will reduce the note length to 50%
    staccato_note = note[:int(note_duration * staccato_ratio)]
    silence_duration = int(note_duration * (1 - staccato_ratio))  # Silence to mimic staccato rest
    silence = AudioSegment.silent(duration=silence_duration)
    return staccato_note + silence
AudioSegment.__xor__ = staccato

def shorten(note, ratio=2):
    note_duration = len(note)
    shorten_note =  note[:int(note_duration / ratio)]
    return shorten_note
AudioSegment.__truediv__ = shorten

# Define the frequencies for each note in Hz
f_Z = 0

f_C4 = 261.63  # Middle C
f_D4 = 293.66
f_E4 = 329.63
f_F4 = 349.23
f_G4 = 392.00
f_A4 = 440.00
f_B4 = 493.88

f_A5 = f_A4 * 2
f_B5 = f_B4 * 2

f_C5 = f_C4 * 2

# Generate the notes as sine waves
note_C = Sine(f_G4).to_audio_segment(duration=duration)
# Z = Sine(f_Z).to_audio_segment(duration=duration)
Z = AudioSegment.silent(duration=duration)
note_D = Sine(f_G4).to_audio_segment(duration=duration)
note_E = Sine(f_G4).to_audio_segment(duration=duration)
note_F = Sine(f_F4).to_audio_segment(duration=duration)

C2 = Sine(f_C4 / 4).to_audio_segment(duration=duration)
D2 = Sine(f_D4 / 4).to_audio_segment(duration=duration)
E2 = Sine(f_E4 / 4).to_audio_segment(duration=duration)
F2 = Sine(f_F4 / 4).to_audio_segment(duration=duration)
G2 = Sine(f_G4 / 4).to_audio_segment(duration=duration)
A2 = Sine(f_A4 / 4).to_audio_segment(duration=duration)
B2 = Sine(f_B4 / 4).to_audio_segment(duration=duration)
C3 = Sine(f_C4 / 2).to_audio_segment(duration=duration)
D3 = Sine(f_D4 / 2).to_audio_segment(duration=duration)
E3 = Sine(f_E4 / 2).to_audio_segment(duration=duration)
F3 = Sine(f_F4 / 2).to_audio_segment(duration=duration)
G3 = Sine(f_G4 / 2).to_audio_segment(duration=duration)
A3 = Sine(f_A4 / 2).to_audio_segment(duration=duration)
B3 = Sine(f_B4 / 2).to_audio_segment(duration=duration)
C4 = Sine(f_C4).to_audio_segment(duration=duration) # middle C
C4s = Sine(277.18).to_audio_segment(duration=duration) # middle C
D4 = Sine(f_D4).to_audio_segment(duration=duration)
E4 = Sine(f_E4).to_audio_segment(duration=duration)
F4 = Sine(f_F4).to_audio_segment(duration=duration)
F4s = Sine(369.99).to_audio_segment(duration=duration)
G4 = Sine(f_G4).to_audio_segment(duration=duration)
A4 = Sine(f_A4).to_audio_segment(duration=duration)
B4 = Sine(f_B4).to_audio_segment(duration=duration)
A5 = Sine(f_A5).to_audio_segment(duration=duration)
B5 = Sine(f_B5).to_audio_segment(duration=duration)
C5 = Sine(f_C5).to_audio_segment(duration=duration)
D5 = Sine(f_D4 * 2).to_audio_segment(duration=duration)
E5 = Sine(f_E4 * 2).to_audio_segment(duration=duration)
F5 = Sine(f_F4 * 2).to_audio_segment(duration=duration)
F5s = Sine(739.99).to_audio_segment(duration=duration)
G5 = Sine(f_G4 * 2).to_audio_segment(duration=duration)
G5s = Sine(830.61).to_audio_segment(duration=duration)

# A5 = Sine(f_A5).to_audio_segment(duration=duration)
# B5 = Sine(f_B5).to_audio_segment(duration=duration)
C6 = Sine(f_C5 * 2).to_audio_segment(duration=duration)
C6s = Sine(1046.50).to_audio_segment(duration=duration)
D6 = Sine(f_D4 * 4).to_audio_segment(duration=duration)
D6s = Sine(1174.66).to_audio_segment(duration=duration)
E6 = Sine(1318.51).to_audio_segment(duration=duration)
E6s = Sine(f_D4 * 4).to_audio_segment(duration=duration)

# nice part starts on page 2 at "D"
# melody = B5 + Z + A5 + Z + G4 + Z + F4 + Z + E4 + Z + D4 + Z + C4 + Z + B4 + Z + D4
scale = C2 + D2 + E2 + F2 + G2 + A2 + B2 + C3 + D3 + E3 + F3 + G3 + A3 + B3 + C4 + D4 + E4 + F4 + G4 + A4 + B4 + C5 + D5 + E5 + F5 + G5 + A5 + B5 + C6 # + D6 + E6 + F6 + G6 + A6 + B6 + C7 + D7 + E7 + F7 + G7 + A7 + B7 + C8

melody = (A5/4^1) + (A5/4^1) + (A5/2^1) + (G5s/2^1) + (A5/2^1) + (G5s/2^1) + (A5^1) + Z/8
melody += D6/2 + C6s/2 + D6/2 + F5s/2 + B5/2 + A5/2 + G5/2 + Z/8
melody += (G5/4^1) + (G5/4^1) + (G5/2^1) + (F5s/2^1) + (G5/2^1) + (F5s/2^1) + (G5^1) + Z/8
melody += (D6s/2) + (E6/2) + (G5s/2) + (A5/2) + (E5/2) + (G5/2) + (F5s/2) + (Z/8)
melody += (A5/4^1) + (F5s/4^1) + (D5/4) + (A4/4) + (F4s/4^1) + (D4/4^1) + (G4/4) + (E4/4) + (C4s/4^1) + (A3/4^1)
melody += (F4s/4) + (D4/4) + (G4/4) + (E4/4) + (A4/2^1)
melody += (A5/4^1) + (F5s/4^1) + (D5/4) + (A4/4) + (F4s/4^1) + (D4/4^1) + (G4/4) + (E4/4) + (C4s/4^1) + (A3/4^1)
melody += (F4s/4) + (D4/4) + (G4/4) + (E4/4) + (A4/2^1)

# melody = A5 + F5s + D5 + A4
# melody = (A5/4^1) + (F5s/4^1) + (D5/4) + (A4/4) + (F4s/4^1) + (D4/4^1) + (G4/4) + (E4/4) + (C4s/4^1) + (A3/4^1)
# melody += (F4s/4) + (D4/4) + (G4/4) + (E4/4) + (A4/2^1)

play(melody)
