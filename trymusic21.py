from music21 import stream, note

# Create a simple scale
scale = stream.Stream()
notes = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']

for note_name in notes:
    n = note.Note(note_name)
    scale.append(n)

# Save the scale as a MIDI file
# midi_file = scale.write('midi', fp='my_scale.mid')
scale.show('midi')

print(f"MIDI file saved as: {midi_file}")
