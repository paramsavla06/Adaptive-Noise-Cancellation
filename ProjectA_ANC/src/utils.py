import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
import librosa
import librosa.display


def load_wav(path):
    data, fs = sf.read(path)
    if data.ndim > 1:
        data = np.mean(data, axis=1)
    return data, fs


def save_wav(path, data, fs):
    sf.write(path, data, fs)


def normalize_signal(x):
    return x / np.max(np.abs(x))


def compute_snr(clean, noisy):
    N = min(len(clean), len(noisy))
    clean = clean[:N]
    noisy = noisy[:N]
    noise = noisy - clean
    snr = 10 * np.log10(np.sum(clean**2) / np.sum(noise**2))
    return snr


def plot_waveforms(primary, cleaned, clean_speech=None):
    plt.figure(figsize=(12, 6))
    plt.subplot(3, 1, 1)
    plt.plot(primary)
    plt.title("Primary (Speech + Noise)")
    plt.subplot(3, 1, 2)
    plt.plot(cleaned)
    plt.title("Cleaned Output (ANC)")
    if clean_speech is not None:
        plt.subplot(3, 1, 3)
        plt.plot(clean_speech[:len(primary)])
        plt.title("Original Clean Speech")
    plt.tight_layout()
    plt.show()


def plot_spectrogram(signal, fs, title="Spectrogram"):
    plt.figure(figsize=(10, 4))
    D = np.abs(librosa.stft(signal))
    librosa.display.specshow(librosa.amplitude_to_db(D, ref=np.max), sr=fs, y_axis='log', x_axis='time')
    plt.colorbar(format='%+2.0f dB')
    plt.title(title)
    plt.tight_layout()
    plt.show()
