import librosa as lb
import numpy as n
import soundfile as sf
from pathlib import Path

p = './pink.mp3'
audio , sr = lb.load(p, sr= None)

