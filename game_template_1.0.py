import tkinter as tk
import random as rd

class Grid_Ref(tk.Tk):
    instance = 0
    object_size = 20
    board_size = 30
    frame_width = 2*5 + board_size*object_size
    frame_height = 2*5 + board_size*object_size
    npc_row_pos = 8
    npc_col_pos = 8
    enemy1_row_pos = 27
    enemy1_col_pos = 27
    game_delay = 1000
    def __init__(self):
        super().__init__()
        self.tk_frame = tk.Canvas(self, width=self.frame_width, height=self.frame_height)
        self.bind("<Key>", self.key_pressed)
        self.tk_frame.pack()
        self.init_grid()
        self.timer_clock()
    def init_grid(self):
        self.grid_list = []
        self.write_first_instance()
        self.move_player(0,0)
        self.render_frame()
    def reset_frame(self): 
        self.tk_frame.delete(tk.ALL)
        self.render_frame()
    def reset_game(self):
        self.grid_list = []
        self.write_first_instance()
        self.player_row_pos = int(self.board_size/2)
        self.player_col_pos = int(self.board_size/2)
        self.move_player(0,0)
        self.render_frame()
    def render_frame(self): 
        for i_row in range(self.board_size):
            for f_col in range(self.board_size): 
                rect_left = 5 + f_col * self.object_size 
                rect_right = rect_left + self.object_size
                rect_top = 5 + i_row * self.object_size
                rect_bottom = rect_top + self.object_size
                if self.grid_list[i_row][f_col] == 1: # Player 
                    self.tk_frame.create_oval(rect_left, rect_top, rect_right, rect_bottom, fill="blue")
                if self.grid_list[i_row][f_col] == 2: # Npc 
                    self.tk_frame.create_oval(rect_left, rect_top, rect_right, rect_bottom, fill="brown")
                if self.grid_list[i_row][f_col] == 10: # Enemies 
                    self.tk_frame.create_oval(rect_left, rect_top, rect_right, rect_bottom, fill="red")
                if self.grid_list[i_row][f_col] == 20: # Items
                    self.tk_frame.create_rectangle(rect_left, rect_top, rect_right, rect_bottom, fill="yellow")
                if self.grid_list[i_row][f_col] == 30: # Walls 
                    self.tk_frame.create_rectangle(rect_left, rect_top, rect_right, rect_bottom, fill="black")
                if self.grid_list[i_row][f_col] == 40: # Border 
                    self.tk_frame.create_rectangle(rect_left, rect_top, rect_right, rect_bottom, fill="green")
                if self.grid_list[i_row][f_col] == 88: # Floor 
                    self.tk_frame.create_rectangle(rect_left, rect_top, rect_right, rect_bottom, fill="white") 
                if self.grid_list[i_row][f_col] == 777: # Exit 
                    self.tk_frame.create_rectangle(rect_left, rect_top, rect_right, rect_bottom, fill="cyan")
                if self.grid_list[i_row][f_col] == 1000: # Return 
                    self.tk_frame.create_rectangle(rect_left, rect_top, rect_right, rect_bottom, fill="orange")
    
    def write_first_instance(self):
        self.instance = 0
        self.player_row_pos = int(self.board_size/2)
        self.player_col_pos = int(self.board_size/2)
        for row in range(self.board_size): 
            self.grid_list += [[88] * self.board_size]
        for row in range(self.board_size-1): 
            self.grid_list[0][row] = 40
            self.grid_list[self.board_size-1][row] = 40
        for col in range(self.board_size):
            self.grid_list[col][0] = 40
            self.grid_list[col][self.board_size-1] = 40 
        for i in range(7): 
            self.grid_list[9][i+1] = 30 
        for i in range(9):
            self.grid_list[i+1][9] = 30 
        for i in range(17): 
            self.grid_list[9][i+11] = 30 
        for i in range(8):
            self.grid_list[i+1][20] = 30 
        for i in range(10): 
            self.grid_list[17][i+18] = 30
        for i in range(12):
            self.grid_list[i+17][17] = 30 
        for i in range(12): 
            self.grid_list[13][i+17] = 30
        for i in range(18): 
            self.grid_list[i+10][11] = 30 
        for i in range(18): 
            self.grid_list[i+11][7] = 30 
        for i in range(18): 
            self.grid_list[i+10][3] = 30
        self.grid_list[1][1] = 20
        self.grid_list[28][28] = 20
        self.grid_list[1][28] = 20
        self.grid_list[10][2] = 777
        self.grid_list[10][1] = 777
        self.move_npc()
        self.move_opponent_1()
    def write_second_instance(self):  
        self.instance = 1
        self.grid_list = []
        for row in range(self.board_size): 
            self.grid_list += [[88] * self.board_size]
        for row in range(self.board_size-1): 
            self.grid_list[0][row] = 40
            self.grid_list[self.board_size-1][row] = 40
        for col in range(self.board_size):
            self.grid_list[col][0] = 40
            self.grid_list[col][self.board_size-1] = 40 
        self.player_row_pos = 2
        self.player_col_pos = 28
        self.grid_list[1][28] = 1000
    def move_player(self, dist_row, dist_col): 
        if self.grid_list[self.player_row_pos + dist_row][self.player_col_pos + dist_col] == 88:
            self.grid_list[self.player_row_pos][self.player_col_pos] = 88
            self.player_row_pos = self.player_row_pos + dist_row
            self.player_col_pos = self.player_col_pos + dist_col
            self.grid_list[self.player_row_pos][self.player_col_pos] = 1
        if self.grid_list[self.player_row_pos + dist_row][self.player_col_pos + dist_col] == 777:
            self.grid_list[self.player_row_pos][self.player_col_pos] = 88
            self.write_second_instance()
            self.move_player(0,0)
            self.render_frame()        
        if self.grid_list[self.player_row_pos + dist_row][self.player_col_pos + dist_col] == 1000:
            self.grid_list[self.player_row_pos][self.player_col_pos] = 88
            self.write_first_instance()
            self.move_player(0,0)
            self.render_frame()
    def move_npc(self):
        n_row = rd.randrange(self.npc_row_pos - 2,self.npc_row_pos + 2)
        n_col = rd.randrange(self.npc_col_pos - 2,self.npc_col_pos + 2)
        if self.grid_list[n_row][n_col] == 88:
            self.grid_list[self.npc_row_pos][self.npc_col_pos] = 88
            self.npc_row_pos = n_row
            self.npc_col_pos = n_col
            self.grid_list[self.npc_row_pos][self.npc_col_pos] = 2
    def move_opponent_1(self):
        e_row = rd.randrange(self.enemy1_row_pos - 1,self.enemy1_row_pos + 1)
        e_col = rd.randrange(self.enemy1_col_pos - 1,self.enemy1_col_pos + 1)
        if self.grid_list[e_row][e_col] == 88:
            self.grid_list[self.enemy1_row_pos][self.enemy1_col_pos] = 88
            self.enemy1_row_pos = e_row
            self.enemy1_col_pos = e_col
            self.grid_list[self.enemy1_row_pos][self.enemy1_col_pos] = 10
    def timer_clock(self):
        if self.instance == 0:
            self.move_npc()
            self.move_opponent_1()
        self.render_frame()
        self.tk_frame.after(self.game_delay, self.timer_clock)
    def key_pressed(self, tk_command):
        self.tk_frame = tk_command.widget.tk_frame
        if (tk_command.char == "r"):
            self.reset_game()
            self.reset_frame()
        if tk_command.keysym == "Up":
            self.move_player(-1, 0) 
            self.reset_frame()
        if tk_command.keysym == "Down":
            self.move_player(+1, 0) 
            self.reset_frame()
        if tk_command.keysym == "Left":
            self.move_player(0,-1) 
            self.reset_frame()
        if tk_command.keysym == "Right":
            self.move_player(0,+1) 
            self.reset_frame()
init_grid = Grid_Ref()
init_grid.mainloop()
