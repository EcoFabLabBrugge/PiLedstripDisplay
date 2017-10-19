import tkinter as tk
from tkinter import W, N, S, E

class DisplaySimulator:
    xPixel = 18
    yPixel = 11
    pixels = []

    def __init__(self, master, xPixel, yPixel):
        self.xPixel = xPixel
        self.yPixel = yPixel

        master.title("Display Simulator")

        #maximize window on startup
        m = master.maxsize()
        master.geometry('{}x{}+0+0'.format(*m))
        
        tk.Grid.rowconfigure(master, 0, weight=1)
        tk.Grid.columnconfigure(master, 0, weight=1)

        frame = tk.Frame(master)
        frame.grid(row=0, column=0, sticky=N+S+E+W)

        i = 0
        while i < self.yPixel:
            tk.Grid.rowconfigure(frame, i, weight=1)
            y = 0
            while y < self.xPixel:
                tk.Grid.columnconfigure(frame, y, weight=1)
                c = tk.Canvas(frame ,background = 'black')
                self.pixels.append(c)
                c.grid(row=i, column=y, sticky=N+S+E+W)
                y += 1
            i += 1

    def Red(self):
        for canvas in self.pixels:
            canvas.config(background = 'red')
    def DisplayFrame(self, frame):
        y = 0
        pixNum = 0
        while y < self.yPixel:
            x = 0
            while x < self.xPixel:
                self.pixels[pixNum].config(background = '#' + format(frame[y][x], 'x'))
                pixNum += 1
                x +=1
            y += 1
        