import tkinter as tk
import numpy as np


#Trying to obtain a number or else pass to avoid errors with a letter input.
def get_volume():
    try:
        value = float(radius.get())
        volume.set((4/3)*np.pi*(value**3))
    except ValueError:
        pass  

tk_shell = tk.Tk()

# Naming the main shell.
tk_shell.title("Radius into Volume of a sphere.")

tk_frame = tk.Frame(tk_shell)
tk_frame.grid()
volume = tk.StringVar()
radius = tk.StringVar()
radius_entry = tk.Entry(tk_frame, width=7, textvariable=radius)
radius_entry.grid(column=2, row=1)
tk.Label(tk_frame, textvariable=volume).grid(column=2, row=2)
tk.Button(tk_frame, text="Calc", command=get_volume).grid(column=3, row=3)

# Labels indicating values from their respective places
tk.Label(tk_frame, text="radius").grid(column=3, row=1)
tk.Label(tk_frame, text="volume").grid(column=3, row=2)

# Spacing and focusing object on the canvas and binding return to calculate func.
for child in tk_frame.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
radius_entry.focus()
tk_shell.bind('<Return>', get_volume)

# Centering the canvas
tk_shell.eval('tk::PlaceWindow %s center' % tk_shell.winfo_pathname(tk_shell.winfo_id()))

tk_shell.mainloop()
