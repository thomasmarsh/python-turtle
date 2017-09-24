class LSys:
    def __init__(self, turtle, lsys):
        self.lsys = lsys
        self.prog = lsys.axiom
        self.turtle = turtle
        self.step_size = 4
        self.angle = 90
        if hasattr(lsys, 'angle'):
            self.angle = lsys.angle

    def rewrite(self, n):
        axiom = self.lsys.axiom
        for _ in xrange(n):
            result = []
            for c in axiom:
                result.append(self.lsys.rules.get(c, c))
            axiom = ''.join(result)
        self.prog = axiom 
    
    def run(self):
        for cmd in self.prog:
            if cmd.isupper():
                self.turtle.forward(self.step_size)
            elif cmd.islower():
                self.turtle.penup()
                self.turtle.forward(self.step_size)
                self.turtle.pendown()
            elif cmd == '[':
                self.turtle.state.push()
            elif cmd == ']':
                self.turtle.state.pop()
            elif cmd == '+':
                self.turtle.left(self.angle)
            elif cmd == '-':
                self.turtle.right(self.angle)
            else:
                print 'did not understand:', cmd
