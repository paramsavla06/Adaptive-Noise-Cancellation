# src/combining.py
import os
import numpy as np
import soundfile as sf

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)


def to_mono(x):
    """Convert stereo to mono by averaging channels"""
    if x.ndim > 1:
        x = np.mean(x, axis=1)
    return x


# Load speech and noise files (replace with your own filenames)
speech, fs1 = sf.read(os.path.join(DATA_DIR, "speech.wav"))
noise, fs2 = sf.read(os.path.join(DATA_DIR, "noise.wav"))

speech = to_mono(speech)
noise = to_mono(noise)

if fs1 != fs2:
    raise ValueError(f"Sample rates differ: speech={fs1}, noise={fs2}")

# Match lengths
N = min(len(speech), len(noise))
speech = speech[:N]
noise = noise[:N]

# Normalize
speech = speech / np.max(np.abs(speech))
noise = noise / np.max(np.abs(noise))

# Create primary (speech + noise)
primary = speech + 0.5 * noise

# Reference signal (aligned noise, no delay)
reference = noise.copy()

# Save to data folder
sf.write(os.path.join(DATA_DIR, "primary.wav"), primary, fs1)
sf.write(os.path.join(DATA_DIR, "reference.wav"), reference, fs1)

print("✅ Created primary.wav and reference.wav in 'data/'")
