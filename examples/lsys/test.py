from graphics import GraphWin
from draw import TurtleDraw
from lsys import LSys

from examples import *


def draw_lsys(win):
    t = TurtleDraw(win)
    t.state.position = (150, 155)
    t.state.left()
    t.set_color(40, 180, 30)
    lsys = LSys(t, Penrose)
    lsys.rewrite(6)
    lsys.step_size = 5
    print 'Program:', lsys.prog
    lsys.run()

def main():
    win = GraphWin('', 300, 300, False)
    draw_lsys(win)
    win.getMouse()
    win.close()

if __name__ == '__main__': main()
