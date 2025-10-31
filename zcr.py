import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read

def compute_zcr(audio_path, frame_duration_ms=20):
    rate, data = read(audio_path)

    if data.ndim > 1:
        data = data.mean(axis=1)
    data = data / np.max(np.abs(data))

    frame_length = int(rate * frame_duration_ms / 1000)
    num_frames = len(data) // frame_length
    zcr = []

    for i in range(num_frames):
        frame = data[i * frame_length:(i + 1) * frame_length]
        zero_crossings = np.sum(np.abs(np.diff(np.sign(frame)))) / 2
        zcr.append(zero_crossings / frame_length)

    time = np.arange(num_frames) * (frame_duration_ms / 1000.0)
    return time, np.array(zcr)

def plot_zcr(audio_path):
    time, zcr = compute_zcr(audio_path)

    plt.figure(figsize=(12, 4))
    plt.plot(time, zcr, color='purple', linewidth=1.5)
    plt.title("Zero Crossing Rate (ZCR) over Time")
    plt.xlabel("Time (s)")
    plt.ylabel("ZCR")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.show()
