class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({}, {})'.format(self.x, self.y)

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return 'Rectangle({}, {})'.format(str(self.p1),
                                          str(self.p2))

    def width(self):
        return self.p2.x - self.p1.x

    def height(self):
        return self.p2.y - self.p1.y

    def area(self):
        return self.width() * self.height()

    def move(self, dx, dy):
        self.p1.move(dx, dy)
        self.p2.move(dx, dy)

    def scale(self, n):
        self.p2.x = self.p1.x + self.width() * n
        self.p2.y = self.p1.y + self.height() * n
