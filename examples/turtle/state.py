import math

def deg2rad(n):
    return math.pi * n / 180.0

def delta(theta):
    return (math.cos(theta), -math.sin(theta))

class TurtleState:
    def __init__(self):
        self.position = (50.0, 50.0)
        self.angle = deg2rad(0)

    def __repr__(self):
        (x, y) = self.position
        return 'TurtleState(({}, {}), {})'.format(x, y, self.angle)

    def forward(self, n=1):
        (x, y) = self.position
        (dx, dy) = delta(self.angle)
        self.position = (x+dx*n, y+dy*n)

    def turn(self, amount=deg2rad(90)):
        self.angle += amount

    left = turn

    def right(self, amount=deg2rad(90)):
        self.turn(-amount)
