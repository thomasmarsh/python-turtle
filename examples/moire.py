#!/bin/env python

from graphics import *

max_x = 512
max_y = 512

# Open the window
win = GraphWin("Moire", max_x, max_y)

for x in range(0, max_x, 2):
    Line(Point(x, 0), Point(x, max_y)).draw(win)
    Line(Point(x, 0), Point(x+(x/2), max_y)).draw(win)

win.getMouse()
win.close()
