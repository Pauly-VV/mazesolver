from Cell import *
import time
import random

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None, seed = None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells_list = []
        self.seed = seed
        if self.seed != None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
    
    def _create_cells(self):
        self.cells_list = []
        for x in range(self.num_cols):
            column = []
            for y in range(self.num_rows):
                column.append(Cell(
                    self.x1 + ((x) * self.cell_size_x),
                    self.x1 + ((x+1) * self.cell_size_x),
                    self.y1 + ((y) * self.cell_size_y),
                    self.y1 + ((y+1) * self.cell_size_y),
                    self.win))
            self.cells_list.append(column)
        
        for column in self.cells_list:
            for cell in column:
                self._draw_cell(cell)
                
    
    def _draw_cell(self, cell):
        if self.win == None:
            return
        cell.draw()
        self._animate()
    
    def _animate(self):
        if self.win == None:
            return
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self.cells_list[0][0].has_top_wall = False
        self._draw_cell(self.cells_list[0][0])
        self.cells_list[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cell(self.cells_list[self.num_cols - 1][self.num_rows - 1])

    def _break_walls_r(self, i, j):
        self.cells_list[i][j].visited = True
        while True:
            to_visit = []
            if (i + 1) < (self.num_cols) and self.cells_list[i+1][j].visited == False:
                to_visit.append((i + 1, j))
            if (j + 1) < (self.num_rows) and self.cells_list[i][j+1].visited == False:
                to_visit.append((i, j + 1))
            if (i - 1) >= 0 and self.cells_list[i-1][j].visited == False:
                to_visit.append((i - 1, j))
            if (j - 1) >= 0 and self.cells_list[i][j-1].visited == False:
                to_visit.append((i, j - 1))
            if to_visit == []:
                self.cells_list[i][j].draw()
                return
            direction = random.randrange(len(to_visit))
            next_cell_ij = to_visit[direction]
            if next_cell_ij[0] > i:
                self.cells_list[i][j].has_right_wall = False
                self._draw_cell(self.cells_list[i][j])
                self.cells_list[i+1][j].has_left_wall = False
                self._draw_cell(self.cells_list[i+1][j])
            if next_cell_ij[0] < i:
                self.cells_list[i][j].has_left_wall = False
                self._draw_cell(self.cells_list[i][j])
                self.cells_list[i-1][j].has_right_wall = False
                self._draw_cell(self.cells_list[i-1][j])
            if next_cell_ij[1] > j:
                self.cells_list[i][j].has_bottom_wall = False
                self._draw_cell(self.cells_list[i][j])
                self.cells_list[i][j+1].has_top_wall = False
                self._draw_cell(self.cells_list[i][j+1])
            if next_cell_ij[1] < j:
                self.cells_list[i][j].has_top_wall = False
                self._draw_cell(self.cells_list[i][j])
                self.cells_list[i][j-1].has_bottom_wall = False
                self._draw_cell(self.cells_list[i][j-1])

            self._break_walls_r(next_cell_ij[0], next_cell_ij[1])

    def _reset_cells_visited(self):
        for col in self.cells_list:
            for cell in col:
                cell.visited = False
        
        

