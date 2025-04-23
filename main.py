from Window import *
from Point import *
from Line import *
from Cell import *
from Maze import *
import time

def main():
    win = Window(800, 600)

    #LINE TEST
    #line1 = Line(Point(0, 0), Point(400, 400))
    #line2 = Line(Point(800, 0), Point(0, 400))
    #win.draw_line(line1)
    #win.draw_line(line2, "blue")

    #CELL TEST
    """ cell1 = Cell(10, 100, 10, 100, win.canvas)
    cell2 = Cell(50, 500, 50, 500, win.canvas)
    cell3 = Cell(600, 700, 300, 400, win.canvas)
    cell1.has_top_wall = False
    cell2.has_left_wall = False
    cell3.has_bottom_wall = False
    cell1.draw()
    cell2.draw()
    cell3.draw()

    #DRAW CENTER TO CENTER TEST
    cell1.draw_move(cell2)
    cell2.draw_move(cell3, True) """

    #DRAW MAZE TEST
    maze1 = Maze(0, 0, 5, 5, 100, 100, win)

    win.waitforclose()

main()