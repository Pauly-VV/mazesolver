from Window import *
from Point import *
from Line import *
from Cell import *

def main():
    win = Window(800, 600)

    #LINE TEST
    #line1 = Line(Point(0, 0), Point(400, 400))
    #line2 = Line(Point(800, 0), Point(0, 400))
    #win.draw_line(line1)
    #win.draw_line(line2, "blue")

    #CELL TEST
    cell1 = Cell(10, 100, 10, 100, win.canvas)

    cell1.draw()

    win.waitforclose()

main()