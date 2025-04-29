from Cell import *
import time

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells_list = []

        self._create_cells()
    
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





                


