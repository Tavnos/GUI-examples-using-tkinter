import tkinter as tk
import numpy as np


# Incorporating all of it inside a class
class SphereVolume:
    def __init__(self):
        self.tk_shell = tk.Tk()
        self.tk_shell.title("Radius into Volume of a sphere.")
        self.tk_frame = tk.Frame(self.tk_shell).grid(column=0, row=0)
        self.volume = tk.StringVar()
        self.radius = tk.StringVar()
        self.radius_entry = tk.Entry(self.tk_frame, width=10, textvariable=self.radius).grid(column=2, row=1)
        tk.Label(self.tk_frame, textvariable=self.volume).grid(column=2, row=2)
        tk.Button(self.tk_frame, text="Calculate", command=self.get_volume).grid(column=3, row=3)
        tk.Label(self.tk_frame, text="radius").grid(column=3, row=1)
        tk.Label(self.tk_frame, text="volume").grid(column=3, row=2)
        for child in self.tk_frame.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
        self.radius_entry.focus()
        self.tk_shell.bind('<Return>', self.get_volume)
        self.tk_shell.eval('tk::PlaceWindow %s center' % self.tk_shell.winfo_pathname(self.tk_shell.winfo_id()))
        self.tk_shell.mainloop()
        
    def calculate(self):
        try:
            value = float(self.radius.get())
            self.volume.set((4/3)*np.pi*(value**3))
        except ValueError:
            pass
        
if __name__ == "__main__":
main_shell = SphereVolume()
