
import argparse
from audio_processing import preprocess_audio
from transcription import transcribe_audio

def main():
    parser = argparse.ArgumentParser(description="Audio to Text Converter")
    parser.add_argument('--audio', type=str, required=True, help="Path to the audio file")
    args = parser.parse_args()

    audio_path = args.audio
    print("[INFO] Starting transcription...")
    text = transcribe_audio(audio_path)
    print("\n[TRANSCRIBED TEXT]\n")
    print(text)

if __name__ == "__main__":
    main()
