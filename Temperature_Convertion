class D_calc(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("US/EU temp conversion")
        tk.Label(self, text='Enter num and declare temp').grid()
        self.temp_entry = tk.StringVar()
        self.string_output = tk.StringVar()
        self.entry_var = tk.Entry(self, width=8, textvariable=self.temp_entry)
        self.entry_var.grid()
        self.output_label = tk.Label(self, textvariable=self.string_output)
        self.output_label.grid()
        f_btn = tk.Button(self, text='Fahrenheit', command=self.f_from_c)
        f_btn.grid()
        c_btn = tk.Button(self, text='Celsius', command=self.c_from_f)
        f_btn.grid()
        self.entry_var.focus()
        for child in self.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
        self.eval('tk::PlaceWindow %s center' % self.winfo_pathname(self.winfo_id()))
    def c_from_f(self):
        fahrenheit = float(self.temp_entry.get())
        celsius = (5 / 9) * (fahrenheit - 32)
        self.string_output.set('{} Fahrenheit is {} Celsius'.format(fahrenheit, celsius))
    def f_from_c(self):
        celsius = float(self.temp_entry.get())
        fahrenheit = (celsius * (9 / 5)) + 32
        self.string_output.set('{} Celsius is {} Fahrenheit'.format(celsius, fahrenheit))
run_calc = D_calc()
run_calc.mainloop()
