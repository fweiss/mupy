from pydub.generators import Sine
from pydub.playback import play

# Define the frequencies for each note in Hz
C4 = 261.63  # Middle C
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88

# Define the duration for each note (in milliseconds)
duration = 500  # 500 ms for each note

# Generate the notes as sine waves
note_C = Sine(C4).to_audio_segment(duration=duration)
note_D = Sine(D4).to_audio_segment(duration=duration)
note_E = Sine(E4).to_audio_segment(duration=duration)
note_F = Sine(F4).to_audio_segment(duration=duration)
note_G = Sine(G4).to_audio_segment(duration=duration)

# Combine the notes to create a melody
melody = note_C + note_D + note_E + note_F + note_G

# Play the melody
play(melody)
