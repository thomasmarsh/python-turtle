from state import *
from graphics import *

class DrawState:
    def __init__(self):
        self.down = True
        self.color = '#000000'
        self.width = 1

class TurtleDraw:
    def __init__(self, win):
        self.state = TurtleState()
        self.pen = DrawState()
        self.win = win

    def goto(self, x, y):
        last_pos = self.state.position
        self.state.position = (x, y)
        self.draw_line(last_pos,
                       self.state.position)

    def pensize(self, width):
        self.pen.width = width

    def penup(self):
        self.pen.down = False

    def pendown(self):
        self.pen.down = True

    def color(self, r, g, b):
        self.pen.color = '#{:02x}{:02x}{:02x}'.format(r, g, b)

    def draw_line(self, (x1, y1), (x2, y2)):
        if self.pen.down:
            line = Line(Point(x1, y1), Point(x2, y2))
            line.setFill(self.pen.color)
            line.setWidth(self.pen.width)
            line.draw(self.win)

    def forward(self, n=1):
        last_pos = self.state.position
        self.state.forward(n)
        self.draw_line(last_pos,
                       self.state.position)

    def right(self, amount=90):
        self.state.right(deg2rad(amount))

    def left(self, amount=90):
        self.state.left(deg2rad(amount))

def main():
    # Open the window
    win = GraphWin("Turtle", 512, 512)

    do_turtle_stuff(win)

    win.getMouse()
    win.close()

def at_start((x1, y1), (x2, y2), n=2.0):
    a = x2 - y1
    b = y2 - y1
    distance = math.sqrt(a*a + b*b)
    print distance
    return distance < n

def do_turtle_stuff(win):
    t = TurtleDraw(win)
    t.state.position = (156, 256)
    start = t.state.position
    
    while True:
        t.forward(200)
        t.left(80)
        print t
        if at_start(start, t.state.position):
            break

if __name__ == '__main__': main()
