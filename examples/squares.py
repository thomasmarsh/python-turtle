from graphics import *

def rgb_to_color(r, g, b):
    # Test that all numbers are in range
    for n in [r, g, b]:
        assert(0 <= n <= 256)

    # Build and return a color string
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

# Set up window
win = GraphWin("Color", 200, 150)
win.setBackground('black')

# We choose a random starting color set
(r, g, b) = (1, 234, 56)

# For each row
for y in range(0, 150, 10):

    # For each column
    for x in range(0, 200, 10):

        # Compute the RGB color string and draw the square
        color = rgb_to_color(r, g, b)

        # Construct a Rectangle object
        s = Rectangle(Point(x, y), Point(x+10, y+10))

        # Set the fill color. Note that the outline color will be black
        # unless changed here too, using `setOutline`
        s.setFill(color)

        # Draw our object on-screen
        s.draw(win)

        # Cycle the colors
        r = (r * 2 + r) % 256
        g = (g / 2 - g) % 256
        b = (r * g - b) % 256

win.getMouse()
win.close()
