# Adaptive Noise Cancellation (ANC) with LMS Filter

This project demonstrates **Adaptive Noise Cancellation (ANC)** using the **Least Mean Squares (LMS)** algorithm to remove noise from an audio signal containing speech.

---

## Goal

Isolate a clean speech signal by estimating and subtracting the noise from a noisy input signal.

---

## How It Works

1. **Input Signals**:
   - **Primary signal**: Contains speech plus noise.
   - **Reference noise signal**: Correlated noise used for estimation.

2. **Adaptive Filtering**:
   - LMS adaptive filter generates an output approximating the noise in the primary signal.
   - The **error signal** (primary minus filter output) represents the cleaned speech.

3. **Filter Update (Conceptual)**:
   - The filter adjusts its coefficients iteratively to minimize the error between predicted noise and actual noise.

4. **Output**:
   - The error signal is the **noise-canceled speech**.

---

## Advantages

- **Simple and effective** for real-time applications.  
- **Adaptive**: Tracks changing noise patterns automatically.  
- **Lightweight**: Low computational requirement, suitable for embedded systems.  
- Can handle **correlated noise** that is unknown in advance.

---

## Visualization

- Plot noisy vs. cleaned speech signals to verify performance.  
- Optional: Display spectrograms to observe noise reduction across frequencies.

---

## References

1. Haykin, S. *Adaptive Filter Theory*, 5th Edition, Pearson.  
2. Widrow, B., & Stearns, S. *Adaptive Signal Processing*, Prentice Hall, 1985.  
3. S. K. Mitra, *Digital Signal Processing: A Computer-Based Approach*, 4th Edition, McGraw-Hill.

---

## Notes

- Works best with a reference noise signal **correlated to the noise** in the primary input.  
- Performance depends on **filter order** and **step size (learning rate)**.  
- Can be extended to **real-time audio processing** using streaming inputs.
