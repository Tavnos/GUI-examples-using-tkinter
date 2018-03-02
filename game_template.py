# Basically a top down 2d first level game template. 
class Grid_Ref(tk.Tk):
    grid_list = []
    rows = 10
    cols = 10
    row_pos = int(rows/2)
    col_pos = int(cols/2)
    frame_width = 2*5 + cols*30
    frame_height = 2*5 + rows*30
    def __init__(self):
        super().__init__()
        for row in range(self.rows):  
            self.grid_list += [[0] * self.cols]  
        for row in range(len(self.grid_list)):
            self.grid_list[0][row] +=3
            self.grid_list[9][row] +=3
        for col in range(len(self.grid_list[0])):
            self.grid_list[col][0] +=3
            self.grid_list[col][9] +=3
        self.tk_frame = tk.Canvas(self, width=self.frame_width, height=self.frame_height)
        self.bind("<Key>", self.key_pressed)
        self.tk_frame.pack()
    def redraw_frame(self):
        self.tk_frame.delete(tk.ALL)
        self.draw_frame()
    def update_player(self, dist_row, dist_col):
        if self.grid_list[self.row_pos + dist_row][self.col_pos + dist_col] == 0:
            self.grid_list[self.row_pos][self.col_pos] = 0
            self.row_pos = self.row_pos + dist_row
            self.col_pos = self.col_pos + dist_col
            self.grid_list[self.row_pos][self.col_pos] = 1
    def key_pressed(self, tk_command):
        self.tk_frame = tk_command.widget.tk_frame 
        if tk_command.keysym == "Up":
            self.update_player(-1, 0) 
            self.redraw_frame()
        elif tk_command.keysym == "Down":
            self.update_player(+1, 0) 
            self.redraw_frame()
        elif tk_command.keysym == "Left":
            self.update_player(0,-1) 
            self.redraw_frame()
        elif tk_command.keysym == "Right":
            self.update_player(0,+1) 
            self.redraw_frame()
    def draw_frame(self):
        for i_row in range(self.rows):
            for f_col in range(self.cols):
                rect_left = 5 + f_col * 30
                rect_right = rect_left + 30
                rect_top = 5 + i_row * 30
                rect_bottom = rect_top + 30
                self.tk_frame.create_rectangle(rect_left, rect_top, rect_right, rect_bottom, fill="white") 
                if self.grid_list[i_row][f_col] == 1:
                    self.tk_frame.create_oval(rect_left, rect_top, rect_right, rect_bottom, fill="blue") 
                if self.grid_list[i_row][f_col] == 3:
                    self.tk_frame.create_oval(rect_left, rect_top, rect_right, rect_bottom, fill="green") 
init_grid = Grid_Ref()
init_grid.mainloop()
