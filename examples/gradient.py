#!/usr/bin/env python

from graphics import *

def lerp(a, b, t):
    return (1-t)*a + t*b

def lerp_rgb(ca, cb, t):
    return (int(lerp(ca[0], cb[0], t)),
            int(lerp(ca[1], cb[1], t)),
            int(lerp(ca[2], cb[2], t)))

def rgb_to_color(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

start = (255, 0, 0)
end = (0, 0, 255)

win = GraphWin("Gradient", 200, 200)
for x in range(0, 200, 10):
    rect = Rectangle(Point(x, 0), Point(x+10, 200))

    # Our `t` is equal to the percentage of the screen we've processed
    (r, g, b) = lerp_rgb(start, end, x/float(200))
    color = rgb_to_color(r, g, b)
    rect.setFill(color)
    rect.setOutline(color)

    rect.draw(win)

win.getMouse()
win.close()
