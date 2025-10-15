# Adaptive Noise Cancellation (ANC) with LMS Filter

This project uses the **Least Mean Squares (LMS)** adaptive filter algorithm, implemented in Python, to remove noise from an audio signal containing speech.

---

## 🎯 Goal

To isolate a clean speech signal by subtracting an estimated noise component from a noisy input signal.

## 🧠 How It Works (LMS Filter)

The core script (`main.py`) performs the ANC:

1.  **Input:** It takes the **Primary Signal** ($d(n)$, which is Speech + Noise) and the **Reference Signal** ($x(n)$, which is the Noise source).
2.  **Estimation:** The LMS filter **estimates the noise** ($y(n)$) found in the Primary Signal using the Reference Signal.
3.  **Output:** The final **Cleaned Output** is the **Error Signal** ($e(n) = d(n) - y(n)$), which contains the resulting speech.
4.  **Learning:** The filter weights ($\mathbf{w}$) are continuously updated using the error to improve noise estimation over time.

### Key Parameters:
* **Step Size ($\mu$)**: `0.01` (Controls learning speed).
* **Filter Order**: `64` (Number of filter taps).

---

## 🛠️ Get Started

1.  **Dependencies:** Install required libraries: `numpy`, `soundfile`, `matplotlib`, `librosa`.
2.  **Data Prep:** Put your audio files (`speech.wav` and `noise.wav`) in a `data/` folder.
3.  **Run:** Execute the scripts in order:
    * `python src/combining.py` (Creates the Primary and Reference inputs).
    * `python src/main.py` (Runs the ANC and generates results).

---

## 📊 Results Summary

The ANC process is successful, resulting in a **Signal-to-Noise Ratio (SNR) improvement**.

| Metric | Before ANC | After ANC |
| :--- | :--- | :--- |
| **SNR** | (Value from your run) dB | (Value from your run) dB |

The plots confirm the noise is significantly reduced in the **Cleaned Signal Spectrogram** while the speech patterns remain visible.

| Primary Signal Spectrogram | Cleaned Signal Spectrogram |
| :---: | :---: |
| ![Primary Spectrogram](primary%20signal%20grph.jpg) | ![Cleaned Spectrogram](cleaned%20signal%20graph.jpg) |
