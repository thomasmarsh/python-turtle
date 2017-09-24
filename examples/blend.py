#!/usr/bin/env python

from graphics import *

def lerp(a, b, t):
    return (1-t)*a + t*b

def lerp_rgb(ca, cb, t):
    return (int(lerp(ca[0], cb[0], t)),
            int(lerp(ca[1], cb[1], t)),
            int(lerp(ca[2], cb[2], t)))

def blend(tx, ty):
    a = (255, 0,   0)   # Red
    b = (0,   255, 0)   # Green
    c = (255, 255, 0)   # Yellow
    d = (0,   0,   255) # Blue

    color_t = lerp_rgb(a, b, tx)
    color_u = lerp_rgb(c, d, ty)
    return lerp_rgb(color_t, color_u, 0.5)

def rgb_to_color(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

size = 4
width, height = (512, 512)

# NOTE: we turn off flushing (last param False) so that we can
# draw this screen in a reasonable amount of time.
win = GraphWin("Blend", width, height, False)

for y in range(0, height, size):
    ty = y/float(height)

    for x in range(0, width, size):
        tx = x/float(width)

        # Find curent color
        (r, g, b) = blend(tx, ty)
        color = rgb_to_color(r, g, b)

        square = Rectangle(Point(x, y), Point(x+size, y+size))
        square.setFill(color)
        square.setOutline(color)
        square.draw(win)

win.getMouse()
win.close()
