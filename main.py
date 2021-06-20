import tkinter as tk
import ctypes
import glob, os
import time
from tkinter import PhotoImage
from random import randint


RESOLUTION = [ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)]
TRANSPARENTCOLOR = "gray"
WCD_DIR = os.getcwd()

kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')

SW_HIDE = 0

hWnd = kernel32.GetConsoleWindow()
if hWnd:
    user32.ShowWindow(hWnd, SW_HIDE)


class Boar:
    def __init__(self):
        self.images = []
        self.step = - 1
        self.vector2 = [-100, RESOLUTION[1]/2]
        self.main()
        
    def main(self):
        self.root = tk.Tk()
        self.root.attributes("-transparentcolor", TRANSPARENTCOLOR)
        self.root.attributes("-topmost", True)
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg = TRANSPARENTCOLOR)
        self.root.overrideredirect(True)
        
        self.canvas = tk.Canvas(self.root,
                                width = RESOLUTION[0], height = RESOLUTION[1],
                                bg = TRANSPARENTCOLOR, highlightthickness = 0)
        self.canvas.pack(fill = "both")
        os.chdir(WCD_DIR + "/frames/")
        for file in glob.glob("*.png"):
            self.images.append(PhotoImage(master = self.canvas, file = WCD_DIR + "/frames/" + file))
        self.canvas.create_text(60, RESOLUTION[1] - 10, text = "Jede to jak divočák", font = ("Arial", 8, "bold"))
        
        self.root.after(75, self.render)
        self.root.mainloop()
    
    def render(self):
        self.step += 1
        self.canvas.delete("boar")
        self.canvas.create_image(self.vector2, image = self.images[self.step], tag = "boar")

        if self.step == len(self.images) - 1:
            self.step = 0
        
        if self.vector2[0] < RESOLUTION[0] + 100:
            self.vector2[0] += randint(10, 20)
        else:
            self.vector2[0] = - 100
            self.vector2[1] = randint(100, RESOLUTION[1] - 100)
        
        self.root.after(75, self.render)

if __name__ == "__main__":
    Boar()