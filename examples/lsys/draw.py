from state import *
from graphics import *

class PenState:
    def __init__(self):
        self.is_down = True
        self.width = 1
        self.color = '#000000'

class TurtleDraw:
    def __init__(self, win):
        self.state = TurtleState()
        self.pen = PenState()
        self.win = win
        self.buffer = []

    def clear(self):
        for line in self.buffer:
            line.undraw()
        self.buffer = []

    def goto(self, x, y):
        last_pos = self.state.position
        self.state.position = (x, y)
        self.draw_line(last_pos,
                       self.state.position)

    def pensize(self, w):
        self.pen.width = w

    def penup(self):
        self.pen.is_down = False

    def pendown(self):
        self.pen.is_down = True

    def set_color(self, r, g, b):
        self.pen.color = '#{:02x}{:02x}{:02x}'.format(r, g, b)

    def draw_line(self, (x1, y1), (x2, y2)):
        if self.pen.is_down:
            line = Line(Point(x1, y1), Point(x2, y2))
            line.draw(self.win)
            line.setFill(self.pen.color)
            line.setWidth(self.pen.width)
            self.buffer.append(line)

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
