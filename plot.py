import wave
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Load the .wav file
file_path = "melody.wav"  # Replace with your .wav file path
sample_rate, audio_data = wavfile.read(file_path)

# If the audio is stereo, select one channel for simplicity
if len(audio_data.shape) == 2:
    audio_data = audio_data[:, 0]

# Create the time axis in seconds
time_axis = np.linspace(0, len(audio_data) / sample_rate, num=len(audio_data))

# Plot the waveform
plt.figure(figsize=(10, 4))
plt.plot(time_axis, audio_data)
plt.title("Waveform of the Audio File")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.show()
