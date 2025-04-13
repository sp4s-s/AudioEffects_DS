import librosa
import numpy as np


def pitchify(y, sr, n_steps=None):
    if n_steps is None:
        n_steps = np.random.uniform(-3, 3)
    return librosa.effects.pitch_shift(y=y, sr=sr, n_steps=n_steps)


def stretch_time(y, rate=None):
    if rate is None:
        rate = np.random.uniform(0.4, 2.5)
    return librosa.effects.time_stretch(y, rate=rate)


def add_noise(y, noise_factor=None):
    if noise_factor is None:
        noise_factor = np.random.uniform(0.001, 0.01)
    noise_data = np.random.randn(len(y))
    return y + noise_factor * noise_data