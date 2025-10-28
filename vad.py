import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read

def compute_vad(audio_path, frame_duration_ms=20, threshold=0.02):
    rate, data = read(audio_path)
    
    if data.ndim > 1:
        data = data.mean(axis=1)
    data = data / np.max(np.abs(data))
    
    frame_length = int(rate * frame_duration_ms / 1000)
    num_frames = len(data) // frame_length
    
    energies = []
    for i in range(num_frames):
        frame = data[i * frame_length:(i + 1) * frame_length]
        energy = np.sum(frame ** 2)
        energies.append(energy)
    
    energies = np.array(energies)
    vad = energies > threshold
    time = np.arange(num_frames) * (frame_duration_ms / 1000.0)
    
    return time, vad

def plot_vad(audio_path):
    time, vad = compute_vad(audio_path)
    
    plt.figure(figsize=(12, 3))
    plt.step(time, vad.astype(int), where='post', color='green', linewidth=2, label='Voice Active')
    plt.fill_between(time, 0, vad.astype(int), step='post', color='green', alpha=0.3)
    
    plt.title("Voice Activity Detection (VAD)")
    plt.xlabel("Time (s)")
    plt.ylabel("Speech Activity")
    plt.yticks([0, 1], ["Silence", "Speech"])
    plt.ylim(-0.2, 1.2)
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.legend()
    plt.tight_layout()
    plt.show()
