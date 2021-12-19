import tkinter as tk
from tkinter import ttk


class LoadingWin(tk.Toplevel):

    def __init__(self):
        tk.Toplevel.__init__(self)
        self.grab_set()
        self.geometry("400x100")
        self.configure(bg="#83568a")
        self.resizable(False, False)
        self.title("Portfolio Maker")
        self.label = tk.Label(self, text="accessing site and getting cookies...", anchor="w",
                                 font=("RobotoCondensed-normal", 10, "normal"), bg="#83568a")
        self.label.pack(fill=tk.BOTH, padx=50, pady=10)
        self.progress = ttk.Progressbar(self, orient=tk.HORIZONTAL, length=300, mode='determinate')
        self.progress.pack(pady=1)
