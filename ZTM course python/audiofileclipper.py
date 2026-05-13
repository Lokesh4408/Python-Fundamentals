from pydub import AudioSegment
import audioread

def clip_audio(input_path, output_path, start_time, end_time):
    """
    Clips a segment from an MP3 audio file.

    Args:
        input_path (str): Path to the input MP3 file.
        output_path (str): Path to save the clipped audio file.
        start_time (int): Start time in seconds.
        end_time (int): End time in seconds.
    """
    # Load the MP3 file with audioread support
    audio = AudioSegment.from_file(input_path, format="mp3")
    
    # Clip the audio between start and end times (in milliseconds)
    clipped_audio = audio[start_time * 1000:end_time * 1000]

    # Export the clipped audio to the output path in MP3 format
    clipped_audio.export(output_path, format="mp3")
    print(f"Clipped audio saved to {output_path}")

# Example usage:
input_file = r'C:/Users/ivanr/OneDrive/Desktop/github/Python-Fundamentals/audiofiles/upworkAudiofile.mp3'
output_file = r'C:/Users/ivanr/OneDrive/Desktop/github/Python-Fundamentals/audiofiles/clipped_audio.mp3'

clip_audio(input_file, output_file, start_time=0, end_time=5)
