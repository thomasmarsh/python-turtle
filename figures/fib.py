#!/usr/bin/env python

class Counter:
    def __init__(self):
        self.value = 0

    def next(self):
        result = self.value
        self.value += 1
        return result

class Node:
    def __init__(self, symbol, counter, parent=None):
        self.parent = parent
        self.symbol = symbol
        self.label = '{}{}'.format(symbol, counter.next())
        self.counter = counter
        self.children = []

    def add(self, symbol):
        self.children.append(Node(symbol, self.counter, self.label))

    def populate(self, n):
        if n == 0:
            return
        if self.symbol == 'A':
            self.add('A')
            self.add('B')
        else:
            assert(self.symbol == 'B')
            self.add('A')

        for child in self.children:
            child.populate(n-1)

    def levels(self):
        q = [self]
        result = []
        while q:
            work = q
            q = []
            for node in work:
                for child in node.children:
                    q.append(child)
            result.append(work)
        return result

    def dot_def(self):
        return '{}[label="{}"];'.format(self.label, self.symbol)

    def dot_defs(self):
        yield '    ' + self.dot_def()
        for child in self.children:
            for  result in child.dot_defs():
                yield result

    def __repr__(self):
        suffix = ''
        if len(self.children) > 0:
            suffix = '({})'.format(', '.join([repr(x)
                                   for x in self.children]))
        return self.label + suffix

def to_dot(top):
    print 'digraph G {'
    print '    bgcolor="transparent";'
    levels = top.levels()
    n = 0
    for level in levels:
        print '    subgraph cluster_{} {{'.format(n)
        indent = ' '*8
        print indent + 'rank=same;'
        print indent + 'labeljust="l";'
        print indent + 'shape=rect;'
        print indent + 'color=grey;'
        print indent + 'label="n = {}";'.format(n)
        print indent + 'node [shape=square];'
        for x in reversed(level):
            print '{}{}'.format(' '*8, x.dot_def())
        print '    }'
        n += 1

    for level in levels:
        for x in level:
            if x.parent:
                print '{}{} -> {};'.format(' '*4, x.parent, x.label)
    print '}'

def main():
    top = Node('A', Counter())
    top.populate(5)
    to_dot(top)

if __name__ == '__main__': main()
