import numpy as np
import pyaudio

# Parameters
sample_rate = 44100  # Hz
duration = 2  # seconds
frequency = 440  # A4 note

# Generate a sine wave
t = np.linspace(0, duration, int(sample_rate * duration), False)
signal = np.sin(2 * np.pi * frequency * t)

# Convert the signal to 16-bit integers
audio_data = np.int16(signal * 32767)

# Play the sound
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=sample_rate, output=True)
stream.write(audio_data.tobytes())
stream.stop_stream()
stream.close()
p.terminate()
