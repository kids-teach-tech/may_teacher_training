import requests
import os
from concurrent.futures import ThreadPoolExecutor

def download_file(url, path):
    """Download a file from a URL to a local path."""
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(path, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {path}")
        else:
            print(f"Failed to download {url}, status code {response.status_code}")
    except requests.RequestException as e:
        print(f"Error downloading {url}: {e}")

def download_notes(base_url, output_dir, notes, octaves, file_type="aiff"):
    """Download all notes across specified octaves in parallel."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = []
        for octave in octaves:
            for note in notes:
                file_name = f"Piano.mf.{note}{octave}.{file_type}"
                url = f"{base_url}/{file_name}"
                path = os.path.join(output_dir, file_name)
                futures.append(executor.submit(download_file, url, path))

        # Wait for all futures to complete
        for future in futures:
            future.result()

# Define the base URL where the sound files are hosted at University of Iowa
base_url = "https://theremin.music.uiowa.edu/sound%20files/MIS/Piano_Other/piano"

# Define the list of notes and octaves to download (using flats for sharps)
notes = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
octaves = range(0, 8)  # Octave range from 0 to 7

# Output directory to save downloaded files
output_dir = "downloaded_piano_sounds"

# Call the download function
download_notes(base_url, output_dir, notes, octaves)
