from Window import *
from Point import *
from Line import *
from Cell import *
from Maze import *
import time

def main():
    #test inputs
    num_rows = 10
    num_cols = 10
    margin = 2
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)
    

    # #LINE TEST
    # line1 = Line(Point(0, 0), Point(400, 400))
    # line2 = Line(Point(800, 0), Point(0, 400))
    # win.draw_line(line1)
    # win.draw_line(line2, "blue")

    # #CELL TEST
    # cell1 = Cell(10, 100, 10, 100, win)
    # cell2 = Cell(50, 500, 50, 500, win)
    # cell3 = Cell(600, 700, 300, 400, win)
    # cell1.has_top_wall = False
    # cell2.has_left_wall = False
    # cell3.has_bottom_wall = False
    # cell1.draw()
    # cell2.draw()
    # cell3.draw()

    # #DRAW CENTER TO CENTER TEST
    # cell1.draw_move(cell2)
    # cell2.draw_move(cell3, True)

    # #DRAW MAZE TEST
    maze1 = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 0)

    win.waitforclose()

main()