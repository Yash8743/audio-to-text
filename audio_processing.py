
import librosa
import numpy as np
import os
from pydub import AudioSegment

def preprocess_audio(audio_path, target_sr=16000):
    audio, sr = librosa.load(audio_path, sr=target_sr)
    return audio, sr
