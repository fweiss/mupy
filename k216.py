from pydub.generators import Sine
from pydub.playback import play

# Define the frequencies for each note in Hz
f_Z = 0
f_C4 = 261.63  # Middle C
f_D4 = 293.66
f_E4 = 329.63
f_F4 = 349.23
f_G4 = 392.00
f_A4 = 440.00
f_B4 = 493.88

# Define the duration for each note (in milliseconds)
duration = 500 # ms for each note

# Generate the notes as sine waves
note_C = Sine(f_G4).to_audio_segment(duration=duration)
Z = Sine(f_Z).to_audio_segment(duration=duration)
note_D = Sine(f_G4).to_audio_segment(duration=duration)
note_E = Sine(f_G4).to_audio_segment(duration=duration)
note_F = Sine(f_F4).to_audio_segment(duration=duration)

D4 = Sine(f_D4).to_audio_segment(duration=duration)
E4 = Sine(f_E4).to_audio_segment(duration=duration)
F4 = Sine(f_F4).to_audio_segment(duration=duration)
G4 = Sine(f_G4).to_audio_segment(duration=duration)
A4 = Sine(f_A4).to_audio_segment(duration=duration)
B4 = Sine(f_B4).to_audio_segment(duration=duration)

# nice part starts on page 4 at "D"
melody = B4 + Z + B4 + Z + B4 + Z + A4 + Z + G4 + Z + E4 + Z + D4

# Play the melody

play(melody)
