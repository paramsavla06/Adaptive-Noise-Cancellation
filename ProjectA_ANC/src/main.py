# src/main.py
import numpy as np
import os
from utils import load_wav, save_wav, normalize_signal, compute_snr, plot_waveforms, plot_spectrogram

# --- Directories ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
RESULTS_DIR = os.path.join(BASE_DIR, "results")
os.makedirs(RESULTS_DIR, exist_ok=True)

# --- Load signals ---
primary, fs = load_wav(os.path.join(DATA_DIR, "primary.wav"))
reference, _ = load_wav(os.path.join(DATA_DIR, "reference.wav"))
clean_speech, _ = load_wav(os.path.join(DATA_DIR, "speech.wav"))

# --- Normalize ---
primary = normalize_signal(primary)
reference = normalize_signal(reference)
clean_speech = normalize_signal(clean_speech)

# --- LMS Adaptive Filter Parameters ---
mu = 0.01
filter_order = 64

# --- Initialize ---
N = len(reference)
w = np.zeros(filter_order)
y = np.zeros(N)
e = np.zeros(N)

# --- Adaptive Filtering Loop ---
for n in range(filter_order, N):
    x = reference[n-filter_order:n][::-1]  # reference input window
    y[n] = np.dot(w, x)                    # estimated noise
    e[n] = primary[n] - y[n]               # error signal
    w += 2 * mu * e[n] * x                 # LMS update

# --- Save output ---
output_path = os.path.join(RESULTS_DIR, "clean_output.wav")
save_wav(output_path, e, fs)
print(f"✅ Cleaned audio saved at {output_path}")

# --- Compute SNR ---
snr_input = compute_snr(clean_speech, primary)
snr_output = compute_snr(clean_speech, e)
print(f"SNR before ANC: {snr_input:.2f} dB")
print(f"SNR after ANC: {snr_output:.2f} dB")
print(f"SNR improvement: {snr_output - snr_input:.2f} dB")

# --- Plot results ---
plot_waveforms(primary, e, clean_speech)
plot_spectrogram(primary, fs, title="Primary Signal")
plot_spectrogram(e, fs, title="Cleaned Signal")
