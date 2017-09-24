#!/bin/env python

from graphics import *
import math

def deg2rad(n):
    return math.pi * n / 180.0

def delta(theta):
    return (math.cos(theta), -math.sin(theta))

class Turtle:
    def __init__(self):
        self.state = [(50, 50), deg2rad(0)]

    def forward(self, n=1):
        [(x, y), angle] = self.state
        (dx, dy) = delta(angle)
        self.state = [(x+dx*n, y+dy*n), angle]

    def turn(self, amount):
        [position, angle] = self.state
        self.state = [position, angle + amount]

    turn_left = turn

    def turn_right(self, amount):
        self.turn(-amount)


def main():
    t = Turtle()
    print t.state
    t.forward()
    print t.state

if __name__ == '__main__': main()
