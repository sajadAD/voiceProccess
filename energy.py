import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read

def plot_energy(file_path, window_size=1024):
    """Reads a WAV file and plots its short-term energy."""
    rate, data = read(file_path)

    if data.ndim > 1:
        data = data[:, 0]

    samples = data / np.max(np.abs(data))

    energy = []
    for i in range(0, len(samples), window_size):
        window = samples[i:i+window_size]
        e = np.sum(window ** 2)
        energy.append(e)

    energy = np.array(energy)
    time_axis = np.arange(len(energy)) * (window_size / rate)

    plt.figure(figsize=(8, 4))
    plt.plot(time_axis, energy, color='red')
    plt.title("Short-Term Energy of Audio Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Energy")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()
