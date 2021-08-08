import tkinter as tk
import tkinter.ttk as ttk

class ProgressBar(tk.Frame):
    value = 0

    def __init__(self, n, self_terminate=False):
        super().__init__(tk.Tk())
        self.progress = ttk.Progressbar(self, orient=tk.HORIZONTAL, length=100, mode='determinate')
        self.progress.pack(pady=10)
        self.unit = 100 / n
        self.self_terminate = self_terminate

    def increment(self):
        self.value += self.unit
        self.progress['value'] = self.value
        self.update_idletasks()

        if self.value == 100:
            self.complete = tk.Label(text="Done!")
            self.complete.grid(row=1, column=0, pady=5, padx=5)

            if self.self_terminate:
                self.quit()