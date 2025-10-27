import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read

def plot_histogram(file_path):
    """Read a WAV file and plot its amplitude histogram."""
    rate, data = read(file_path)

    if data.ndim > 1:
        data = data[:, 0]

    samples = data / np.max(np.abs(data))

    bins = 50
    min_val, max_val = np.min(samples), np.max(samples)
    bin_edges = np.linspace(min_val, max_val, bins + 1)

    counts = [0] * bins
    for s in samples:
        for i in range(bins):
            if bin_edges[i] <= s < bin_edges[i + 1]:
                counts[i] += 1
                break

    centers = (bin_edges[:-1] + bin_edges[1:]) / 2

    plt.figure(figsize=(8, 4))
    plt.bar(centers, counts, width=(max_val - min_val)/bins,
            color='orange', edgecolor='black')
    plt.title("Histogram of WAV File")
    plt.xlabel("Amplitude")
    plt.ylabel("Count")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()
