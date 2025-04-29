from Point import *
from Line import *
from Window import *

class Cell():
    def __init__(self, x1, x2, y1, y2, win = None):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.center = Point(((self._x1 + self._x2)/2),((self._y1 + self._y2)/2))

    def draw(self):
        if self._win == None:
            return
        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            line.draw(self._win.canvas)
        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            line.draw(self._win.canvas)
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            line.draw(self._win.canvas)
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            line.draw(self._win.canvas)

    def draw_move(self, to_cell, undo = False):
        connector = Line(self.center, to_cell.center)
        if undo == False:
            connector.draw(self._win.canvas, "red")
        if undo == True:
            connector.draw(self._win.canvas, "gray")

        

