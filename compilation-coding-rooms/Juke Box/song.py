# Student Reference: https://docs.google.com/document/d/1sFyM6kCK5QOnmvQy8mnu3177Hj3ta28FkseBOag6kkk/edit?usp=sharing

from jukebox import note_to_index, play_note_by_index, sounds, metadata; import time;

example_song = [
    # Intro
    ('Db4', 200), ('Eb4', 200), ('F4', 200), ('Ab4', 400), 
    ('F4', 200), ('Eb4', 200), ('Db4', 200),
    
    # Verse pattern with embellishments
    ('Ab4', 150), ('F4', 150), ('Ab4', 150), ('Db5', 300),
    ('C5', 150), ('Ab4', 300), ('F4', 150), ('Ab4', 150),
    ('C5', 150), ('Db5', 300), ('C5', 150), ('Ab4', 300),
    ('Eb4', 150), ('F4', 150), ('Gb4', 150), ('Ab4', 300),
    ('Bb4', 150), ('Ab4', 300), ('Gb4', 150), ('F4', 150),
    ('Db4', 150), ('Eb4', 150), ('F4', 150), ('Gb4', 300),
    
    # Chorus with increased tempo and transitions
    ('Ab4', 120), ('F4', 120), ('Ab4', 120), ('Db5', 240),
    ('C5', 120), ('Ab4', 240), ('F4', 120), ('Ab4', 120),
    ('C5', 120), ('Db5', 240), ('C5', 120), ('Ab4', 240),
    ('Eb4', 120), ('F4', 120), ('Gb4', 120), ('Ab4', 240),
    ('Bb4', 120), ('Ab4', 240), ('Gb4', 120), ('F4', 120),
    ('Db5', 120), ('Eb5', 120), ('F5', 120), ('Gb5', 480),
    
    # Bridge section with lower dynamics
    ('Db4', 200), ('Eb4', 200), ('F4', 200), ('Ab4', 400), 
    ('F4', 200), ('Eb4', 200), ('Db4', 200),
    
    # Repetition and finale with a crescendo
    ('Ab4', 150), ('F4', 150), ('Ab4', 150), ('Db5', 300),
    ('C5', 150), ('Ab4', 300), ('F4', 150), ('Ab4', 150),
    ('C5', 150), ('Db5', 300), ('C5', 150), ('Ab4', 300),
    ('Eb4', 150), ('F4', 150), ('Gb4', 150), ('Ab4', 300),
    ('Bb4', 150), ('Ab4', 300), ('Gb4', 150), ('F4', 150),
    ('Db5', 600),  # Final note held longer for effect
] * 2  # Repeat the pattern for a longer composition

def play_song(song):
    # Loop over all notes in the song

play_song(example_song)