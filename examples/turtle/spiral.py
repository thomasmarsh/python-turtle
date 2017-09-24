import draw
from graphics import *

def spiral(t):
    step = 4
    laenge = step
    t.color(0, 255, 0)
    t.pensize(3)
    t.left(180)
    for i in range(-2, 80):
        if i > 0:
            t.color((255-15*i)%256, 0, (15*i)%256)
        for _ in range(3):
            t.forward(laenge)
            t.left(120)
        laenge += step
        t.left(15)

def main():
    win = GraphWin("Spiral", 800, 800)
    t = draw.TurtleDraw(win)
    t.penup()
    t.goto(400, 400)
    t.pendown()

    spiral(t)

    win.getMouse()

if __name__ == '__main__': main()
