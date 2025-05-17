import pygame
import json
import os
import time

# Initialize Pygame Mixer
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.mixer.set_num_channels(600)  # Adjust the number of channels based on needs
pygame.mixer.music.set_volume(1000)


def load_sounds_and_metadata(directory, json_file):
    with open(os.path.join(directory, json_file), 'r') as file:
        metadata = json.load(file)
    
    sounds = {}
    for item in metadata:
        sound_path = os.path.join(directory, item['filename'])
        try:
            sounds[item['index']] = pygame.mixer.Sound(sound_path)
        except pygame.error as e:
            print(f"Failed to load sound {sound_path}: {e}")
    
    return sounds, metadata

# Load sounds and metadata
directory = 'downloaded_piano_sounds'
json_file = 'sounds_metadata.json'
sounds, metadata = load_sounds_and_metadata(directory, json_file)

def note_to_index(note, metadata):
    for item in metadata:
        if item['note'] == note:
            return item['index']
    return None

def play_note_by_index(sounds, index, duration=None):
    if index in sounds:
        sound = sounds[index]
        channel = sound.play()
        if duration:
            time.sleep(duration / 1000)
            #channel.stop()
        else:
            while channel.get_busy():
                time.sleep(0.05)