#!/usr/bin/env python

from graphics import *
import time                 # Added import

# Open the window
win = GraphWin()

for p in [Point(50, 100), Point(150, 100)]:
    for r in range(9, 180, 3):
        c = Circle(p, r)
        c.draw(win)
        #print c             # Added print statement
        #time.sleep(1)       # Added time.sleep()

win.getMouse()
win.close()
