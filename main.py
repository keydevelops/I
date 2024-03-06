import tkinter as tk
import random
import time

class FakeVirus:
    def __init__(self):
        self.screen_width = tk.Tk().winfo_screenwidth()
        self.screen_height = tk.Tk().winfo_screenheight()

        self.width = 400
        self.height = 400
        self.window = tk.Toplevel()
        self.canvas = tk.Canvas(self.window, width=self.width, height=self.height, bg='white')
        self.canvas.pack()
        self.window.overrideredirect(1)  # Make window stay on top
        self.window.geometry(f"{self.width}x{self.height}+{random.randint(0, self.screen_width - self.width)}+{random.randint(0, self.screen_height - self.height)}")
        self.window.attributes('-topmost', 1)  # Make window stay on top
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)  # Intercept close event
        self.window.after(100, self.move_window)  # Start the movement loop

    def move_window(self):
        x = random.randint(-1000, self.screen_width - self.width - 1)
        y = random.randint(-1000, self.screen_height - self.height - 1)
        self.window.geometry(f"{self.width}x{self.height}+{x}+{y}")
        self.canvas.create_line(random.randint(0, self.width), random.randint(0, self.height), random.randint(0, self.width), random.randint(0, self.height), fill='black')
        self.window.after(100, self.move_window)

    def on_close(self):
        # Reopen the window after a delay
        self.window.after(1, self.reopen_window)

    def reopen_window(self):
        # Create a new window
        self.window = tk.Toplevel()
        self.canvas = tk.Canvas(self.window, width=self.width, height=self.height, bg='white')
        self.canvas.pack()
        self.window.overrideredirect(1)  # Make window stay on top
        self.window.geometry(f"{self.width}x{self.height}+{random.randint(0, self.screen_width - self.width)}+{random.randint(0, self.screen_height - self.height)}")
        self.window.attributes('-topmost', 1)  # Make window stay on top
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)  # Intercept close event
        self.window.after(100, self.move_window)

def reopen_ww():
    virus_list = []
    for _ in range(100):
        virus = FakeVirus()
        virus_list.append(virus)
    while True:
        for virus in virus_list:
            try:
                virus.move_window()
            except:
                reopen_ww()

        tk.Tk().update()  # Corrected line
        tk.Tk().update_idletasks()  # Corrected line

virus_list = []
for _ in range(100):
    virus = FakeVirus()
    virus_list.append(virus)
while True:
    for virus in virus_list:
        try:
            virus.move_window()
        except:
            reopen_ww()

        tk.Tk().update()  # Corrected line
        tk.Tk().update_idletasks()