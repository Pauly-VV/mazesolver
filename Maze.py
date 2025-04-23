from Cell import *
import time

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self._create_cells()
    
    def _create_cells(self):
        cells_list = []
        for x in range(self.num_cols):
            column = []
            for y in range(self.num_rows):
                column.append(Cell(
                    self.x1 + ((x) * self.cell_size_x),
                    self.x1 + ((x+1) * self.cell_size_x),
                    self.y1 + ((y) * self.cell_size_y),
                    self.y1 + ((y+1) * self.cell_size_y),
                    self.win.canvas))
            cells_list.append(column)
        
        for column in cells_list:
            for cell in column:
                cell.draw()
                self._animate()
    
    def _draw_cell(self, i, j):
        pass
    
    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)





                


