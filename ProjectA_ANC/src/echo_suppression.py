import numpy as np
import soundfile as sf
import os
from utils import load_wav, save_wav, normalize_signal, plot_waveforms, plot_spectrogram

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
RESULTS_DIR = os.path.join(BASE_DIR, "results")
os.makedirs(RESULTS_DIR, exist_ok=True)

# Load far-end signal (x) and microphone signal (d)
x, fs = load_wav(os.path.join(DATA_DIR, "farend.wav"))
d, _ = load_wav(os.path.join(DATA_DIR, "mic_recorded.wav"))

x = normalize_signal(x)
d = normalize_signal(d)

mu = 0.01
filter_order = 128

N = min(len(x), len(d))
w = np.zeros(filter_order)
y = np.zeros(N)
e = np.zeros(N)

# Adaptive filter loop
for n in range(filter_order, N):
    x_vec = x[n-filter_order:n][::-1]
    y[n] = np.dot(w, x_vec)
    e[n] = d[n] - y[n] 
    w += 2 * mu * e[n] * x_vec

# Save output
output_path = os.path.join(RESULTS_DIR, "echo_suppressed.wav")
save_wav(output_path, e, fs)

print(f"Echo suppressed signal saved at {output_path}")
plot_waveforms(d, e)
plot_spectrogram(d, fs, "Before Echo Suppression")
plot_spectrogram(e, fs, "After Echo Suppression")
