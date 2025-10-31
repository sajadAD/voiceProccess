import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from histogram import plot_histogram
from energy import plot_energy
from vad import plot_vad
from zcr import plot_zcr


class AudioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎵 Audio Analyzer")
        self.root.geometry("800x800")
        self.root.resizable(True, True)

        self.file_path = None

        self.setup_style()
        self.setup_ui()

    def setup_style(self):
        style = ttk.Style()
        style.theme_use("clam") 
        style.configure("Title.TLabel",
                        font=("Poppins", 16, "bold"),
                        foreground="#222")

        style.configure("Info.TLabel",
                        font=("Poppins", 10),
                        foreground="gray")

        button_style = {
            "font": ("Poppins", 11, "bold"),
            "foreground": "white",
            "padding": 8,
            "relief": "flat",
            "anchor": "center"
        }

        style.configure("Green.TButton", background="#4CAF50", **button_style)
        style.map("Green.TButton", background=[("active", "#45A049")])

        style.configure("Blue.TButton", background="#2196F3", **button_style)
        style.map("Blue.TButton", background=[("active", "#1976D2")])

        style.configure("Orange.TButton", background="#FF9800", **button_style)
        style.map("Orange.TButton", background=[("active", "#FB8C00")])

        style.configure("Purple.TButton", background="#9C27B0", **button_style)
        style.map("Purple.TButton", background=[("active", "#7B1FA2")])

        style.configure("DeepPurple.TButton", background="#673AB7", **button_style)
        style.map("DeepPurple.TButton", background=[("active", "#512DA8")])

        style.configure("Red.TButton", background="#F44336", **button_style)
        style.map("Red.TButton", background=[("active", "#D32F2F")])

        self.style = style

    def setup_ui(self):
        ttk.Label(self.root, text="🎵 Audio Analyzer", style="Title.TLabel").pack(pady=10)

        self.file_label = ttk.Label(self.root, text="No file selected", style="Info.TLabel")
        self.file_label.pack(pady=5)

        ttk.Button(self.root, text="Select WAV File",
                   command=self.select_file, style="Green.TButton").pack(pady=8)

        ttk.Button(self.root, text="Show Histogram",
                   command=self.show_histogram, style="Blue.TButton").pack(pady=5)

        ttk.Button(self.root, text="Show Energy",
                   command=self.show_energy, style="Orange.TButton").pack(pady=5)

        ttk.Button(self.root, text="Show VAD",
                   command=self.show_vad, style="Purple.TButton").pack(pady=5)

        ttk.Button(self.root, text="Show ZCR",
                   command=self.show_zcr, style="DeepPurple.TButton").pack(pady=5)

        ttk.Button(self.root, text="Exit",
                   command=self.root.destroy, style="Red.TButton").pack(pady=10)

    # ----------------- File selection -----------------
    def select_file(self):
        file = filedialog.askopenfilename(
            title="Select WAV file",
            filetypes=[("WAV files", "*.wav")]
        )
        if file:
            self.file_path = file
            self.file_label.config(text=f"Selected: {file.split('/')[-1]}")

    # ----------------- Plot functions -----------------
    def check_file(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please select a WAV file first.")
            return False
        return True

    def show_histogram(self):
        if not self.check_file(): return
        try:
            plot_histogram(self.file_path)
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong:\n{e}")

    def show_energy(self):
        if not self.check_file(): return
        try:
            plot_energy(self.file_path)
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong:\n{e}")

    def show_vad(self):
        if not self.check_file(): return
        try:
            plot_vad(self.file_path)
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong:\n{e}")

    def show_zcr(self):
        if not self.check_file(): return
        try:
            plot_zcr(self.file_path)
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong:\n{e}")