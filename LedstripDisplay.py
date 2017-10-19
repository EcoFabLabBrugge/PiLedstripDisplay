import tkinter as tk
import DisplaySimulator as dp
import PatternCreator as pa

xPixel = 18
yPixel = 11

root = tk.Tk()
display = dp.DisplaySimulator(root, xPixel, yPixel)
pattern = pa.PatternCreator(xPixel, yPixel)

def CalcNextFrame():
    display.DisplayFrame(pattern.GetFrame())
    root.after(40, CalcNextFrame)

root.after(100, CalcNextFrame)
root.mainloop()