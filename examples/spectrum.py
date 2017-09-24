#!/usr/bin/env/python

from graphics import *

# Multiply t against all elements
def rgb_multiply(t, (r, g, b)):
    return (t*r, t*g, t*b)


# Add two RGB vectors element-wise
def rgb_add(c1, c2):
    return (c1[0] + c2[0],
            c1[1] + c2[1],
            c1[2] + c2[2])

# Lerp in two dimensions.
def bilinear(tx, ty, c00, c10, c01, c11):
    # With a linear algebra package this would just be:
    #
    #     a = (1-tx)*c00 + tx*c10;
    #     b = (1-tx)*c01 + tx*c11;
    #     return (1-ty)*a + ty*b

    a = rgb_add(rgb_multiply(1-tx, c00),
                rgb_multiply(tx,   c10))

    b = rgb_add(rgb_multiply(1-tx, c01),
                rgb_multiply(tx,   c11))

    return rgb_add(rgb_multiply(1-ty, a),
                   rgb_multiply(ty, b))


def rgb_to_color(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def spectrum(tx, ty):
    # The colors that dominate each quadrant
    c00 = (255, 0,   0)   # Red     - Top left
    c10 = (0,   255, 0)   # Green   - Top right
    c01 = (128, 0,   255) # Violet  - Bottom left
    c11 = (0,   0,   255) # Blue    - Bottom right

    (r, g, b) = bilinear(tx, ty, c00, c10, c01, c11)

    # We need to convert the values back to ints
    return (int(r), int(g), int(b))

size = 4
width, height = (512, 512)

# NOTE: we turn off flushing (last param False) so that we can
# draw this screen in a reasonable amount of time.
win = GraphWin("Spectrum", width, height, False)

for y in range(0, height, size):
    ty = y/float(height)

    for x in range(0, width, size):
        tx = x/float(width)

        # Find curent color
        (r, g, b) = spectrum(tx, ty)
        color = rgb_to_color(r, g, b)

        square = Rectangle(Point(x, y), Point(x+size, y+size))
        square.setFill(color)
        square.setOutline(color)
        square.draw(win)

win.getMouse()
win.close()
