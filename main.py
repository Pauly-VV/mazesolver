from Window import *
from Point import *
from Line import *

def main():
    win = Window(800, 600)

    line1 = Line(Point(0, 0), Point(400, 400))
    line2 = Line(Point(800, 0), Point(0, 400))

    win.draw_line(line1)
    win.draw_line(line2, "blue")

    win.waitforclose()

main()