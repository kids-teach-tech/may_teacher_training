import os
import json

def note_value(note, octave):
    """Convert note and octave to a single integer to enable sorting by pitch."""
    note_ranks = {'C': 1, 'Db': 2, 'D': 3, 'Eb': 4, 'E': 5, 'F': 6, 'Gb': 7, 'G': 8, 'Ab': 9, 'A': 10, 'Bb': 11, 'B': 12}
    return note_ranks[note] + (int(octave) * 12)

def process_files(directory):
    """Process and sort piano sound files, then save metadata to JSON."""
    files = os.listdir(directory)
    parsed_files = []
    
    # Parse files and sort by musical order
    for filename in files:
        if filename.endswith('.aiff'):
            parts = filename.split('.')
            note_octave = parts[2]  # e.g., 'C4' or 'Db3'
            note = ''.join([i for i in note_octave if not i.isdigit()])  # Extracts 'C' or 'Db'
            octave = ''.join([i for i in note_octave if i.isdigit()])  # Extracts '4' or '3'
            parsed_files.append((filename, note, octave))
    
    # Sort by octave and note value
    parsed_files.sort(key=lambda x: (int(x[2]), note_value(x[1], x[2])))

    # Create JSON metadata
    sounds_metadata = []
    for index, (filename, note, octave) in enumerate(parsed_files):
        metadata = {
            'index': index,
            'filename': filename,
            'note': note + octave
        }
        sounds_metadata.append(metadata)

    # Write to JSON file
    with open(os.path.join(directory, 'sounds_metadata.json'), 'w') as f:
        json.dump(sounds_metadata, f, indent=4)

    print("Metadata JSON file has been created successfully.")

# Specify the directory containing the sound files
directory = 'downloaded_piano_sounds'
process_files(directory)
