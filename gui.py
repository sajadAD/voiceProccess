import tkinter as tk
from tkinter import filedialog, messagebox
from histogram import plot_histogram
from energy import plot_energy
from vad import plot_vad
from zcr import plot_zcr

class AudioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Analyzer")
        self.root.geometry("800x800")
        self.root.resizable(True, True)

        self.file_path = None
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="🎵 Audio Analyzer",
                 font=("Arial", 16, "bold")).pack(pady=10)

        self.file_label = tk.Label(self.root, text="No file selected", fg="gray")
        self.file_label.pack(pady=5)

        tk.Button(self.root, text="Select WAV File",
                  command=self.select_file, bg="#4CAF50",
                  fg="white", width=20).pack(pady=8)

        tk.Button(self.root, text="Show Histogram",
                  command=self.show_histogram, bg="#2196F3",
                  fg="white", width=20).pack(pady=5)

        tk.Button(self.root, text="Show Energy",
                  command=self.show_energy, bg="#FF9800",
                  fg="white", width=20).pack(pady=5)
        
        tk.Button(self.root, text="Show VAD",
                  command=self.show_vad, bg="#9C27B0",
                  fg="white", width=20).pack(pady=5)
        
        tk.Button(self.root, text="Show ZCR",
                  command=self.show_zcr, bg="#673AB7",
                  fg="white", width=20).pack(pady=5)
        
        tk.Button(self.root, text="Exit",
                  command=self.root.destroy, bg="#f44336",
                  fg="white", width=20).pack(pady=10)
        


    def select_file(self):
        file = filedialog.askopenfilename(
            title="Select WAV file",
            filetypes=[("WAV files", "*.wav")]
        )
        if file:
            self.file_path = file
            self.file_label.config(text=f"Selected: {file.split('/')[-1]}")

    def show_histogram(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please select a WAV file first.")
            return

        try:
            plot_histogram(self.file_path)
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong:\n{e}")

    def show_energy(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please select a WAV file first.")
            return

        try:
            plot_energy(self.file_path)
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong:\n{e}")
            
    def show_vad(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please select a WAV file first.")
            return
        try:
            plot_vad(self.file_path)
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong:\n{e}")

    def show_zcr(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please select a WAV file first.")
            return
        try:
            plot_zcr(self.file_path)
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong:\n{e}")
