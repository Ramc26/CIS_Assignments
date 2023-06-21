from pydub import AudioSegment
from pydub.playback import play
import time

def play_audio_and_text(audio_file, text_file):
    # Load audio file
    audio = AudioSegment.from_file(audio_file)

    # Start playing the audio
    play(audio)

    # Open and read the text file
    with open(text_file, 'r') as file:
        lines = file.readlines()

    # Calculate the duration per line
    audio_duration = len(audio)
    line_duration = audio_duration / len(lines)

    # Iterate over each line and display it at the corresponding timestamp
    for line in lines:
        # Extract the timestamp and text from the line
        timestamp, text = line.strip().split(' ', 1)

        # Convert the timestamp to seconds
        minutes, seconds = map(int, timestamp.split(':'))
        timestamp_seconds = minutes * 60 + seconds

        # Wait for the corresponding timestamp
        time.sleep(timestamp_seconds)

        # Display the text
        print(text)

# Provide the paths to your audio and text files
audio_file = './Note.mp3'
text_file = './Note.txt'

# Call the function to synchronize the files
play_audio_and_text(audio_file, text_file)
