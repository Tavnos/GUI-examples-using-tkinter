# Getting the volume of a sphere from its radius

import tkinter as tk
import numpy as np


def get_volume():
    value = float(radius.get()) 
    volume.set((4/3)*np.pi*(value**3))
    
tk_shell = tk.Tk()
tk_frame = tk.Frame(tk_shell).grid()
volume = tk.StringVar()
radius = tk.StringVar()
radius_entry = tk.Entry(tk_frame, width=7, textvariable=radius).grid(column=2, row=1)
tk.Label(tk_frame, textvariable=volume).grid(column=2, row=2)
tk.Button(tk_frame, text="radius2volume", command=get_volume).grid(column=3, row=3)

tk_shell.mainloop()
