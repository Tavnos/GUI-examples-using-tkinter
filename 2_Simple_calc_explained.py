import tkinter as tk
import numpy as np


def get_volume():
    value = float(radius.get()) # radius = .get() whatever comes in the value var
    volume.set((4/3)*np.pi*(value**3)) # volume = calculated inside .set()
    
# Tk() root object creation
tk_shell = tk.Tk()

# Canvas/frame object creation
tk_frame = tk.Frame(tk_shell).grid()

# Tk variable declaration
volume = tk.StringVar()
radius = tk.StringVar()

# An empty input entry defining its size, independant var, and position
radius_entry = tk.Entry(tk_frame, width=7, textvariable=radius).grid(column=2, row=1)

# Output label with its dependant var and pos.
tk.Label(tk_frame, textvariable=volume).grid(column=2, row=2)

# The function executing button
tk.Button(tk_frame, text="radius2volume", command=get_volume).grid(column=3, row=3)

# Running loop
tk_shell.mainloop()
