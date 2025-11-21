import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read

def plot_cepstrum(filepath):
    sr, signal = read(filepath)

    if len(signal.shape) == 2:
        signal = signal[:, 0]

    spectrum = np.fft.fft(signal)

    log_spectrum = np.log(np.abs(spectrum) + 1e-10)

    cepstrum = np.abs(np.fft.ifft(log_spectrum))

    plt.figure(figsize=(10, 4))
    plt.plot(cepstrum[:600])
    plt.title("Cepstral Coefficients")
    plt.xlabel("Quefrency Index")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
