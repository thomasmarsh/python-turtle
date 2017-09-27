#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The length module provides a useful method `length` that efficiently
computest the length of a generated string after `n` iterations of
application of production rules to an L-system.

Typical usage of this module is simply as follows:

    from length import length
    from examples import Penrose

    print length(Penrose, 100)
"""

from collections import deque
import sys

def variables(lsys):
    # By definition, the variables of the D0L grammar are those that
    # can be replaced by substitution. Those are the left-hand-side
    # of the production rules, or, in other words, they keys of our
    # `rules` attribute.
    return set(lsys.rules.keys())

def constants(lsys):
    # In our format, the constants of an L-systems are implicit.
    # Therefore, we need to work it out by finding all symbols in the
    # system and eliminating those that are known to be variables.
    a = set(lsys.axiom)
    b = set(''.join(lsys.rules.values()))
    return (a | b) - variables(lsys)

def alphabet(lsys):
    # The alphabet is returned as a string rather than a set because
    # the ordering is useful in certain contexts.
    return ''.join(sorted(variables(lsys)) + sorted(constants(lsys)))

def build_lut(lsys, ss):
    # The lookup-table (or "lut") is a map of a string of symbols to
    # a tuple in the form (h, c, s), where h is a histogram, c is a
    # count of all the constants, and s is the set of unique symbols
    # in the the axiom.
    #
    # We precompute histograms for each symbol list in the system, where
    # a symbol list can be an axiom or the right-hand-side of a rule.
    #
    # For example, with axiom = 'FF', and rules = {'F': 'F+F+F'}, we
    # would get the following hcache:
    #
    #   {
    #       'FF':    { 'F': 2 },
    #       'F+F+F': { 'F': 3, '+': 2 }

    # The set of constants in the system
    cs = constants(lsys)

    # The set of variables in the system
    vs = variables(lsys)

    lut = {}
    for s in ss:
        # Unique symbols in this axiom
        sa = set(s)

        # Compute the histogram for the string
        h = { k: s.count(k) for k in sa }

        # Count all the constants in this axiom
        nc = sum([h[x] for x in (sa & cs)])

        # Build the lut entry. The last element is the set of variables in
        # this axiom.
        lut[s] = (h, nc, sa & vs)

    return lut

def length(lsys, n):
    """
    Calculates the length of the generated string after `n` iterations
    of application of the production rules.
    """

    # All the symbol lists in the system
    ss = [lsys.axiom] + lsys.rules.values()

    # Build the LUT
    lut = build_lut(lsys, ss)

    # Build the cache, prepulated with n==0 entries
    cache = { (k, 0): len(k) for k in ss }

    # Invoke the recursive implementation which memoizes results
    # into a cache.
    return length_impl(lsys.axiom,
                       lsys.rules,
                       n,
                       cache,
                       lut)

def length_impl(axiom,  # The current axiom
                rules,  # Production rules
                n,      # Number of iterations remaining
                cache,  # Cache of results mapping (axiom, n) -> length
                lut):   # Map of axiom -> (histogram, constant count, symbols)

    # We use the current axiom and the depth as the key into a cache.
    k = (axiom, n)
    q = deque([k])

    result = 0
    while q:
        # Peek at the top of the stack
        k = q[-1]

        if k in cache:
            # If we have a result, pop it off. The last entry on the stack
            # will be the top level key, so cache[k] will hold the result.
            q.pop()
        else:
            (axiom, n) = k

            # Base case should be pre-populated.
            #assert(n > 0)

            (h, nc, s) = lut[axiom]

            # Good if all children are cached
            good = True

            # Accumulator for the variables
            nv = 0

            # For variable character in this axiom
            for x in s:
                kp = (rules[x], n-1)
                if not kp in cache:
                    good = False
                    q.append(kp)
                elif good:
                    nv += h[x] * cache[kp]

            # Compute final value for this cache entry as sum
            # of contribution from constants and variables.
            if good:
                cache[k] = nc + nv

    return cache[k]


# The following methods require numpy
try:
    import numpy as np

    def growth_matrix(lsys):
        cs = constants(lsys)
        ab = alphabet(lsys)
        return np.matrix([[(1 if vi == vj else 0) if vi in cs
                           else lsys.rules[vi].count(vj)
                           for vj in ab]
                          for vi in ab],
                         dtype='object')

    def start_array(lsys):
        return np.array([lsys.axiom.count(v)
                         for v in alphabet(lsys)],
                        dtype='object')

    def matrix_length(lsys, n):
        """
        Calculates the length of the generated string after `n` iterations
        of application of the production rules.
        """
        # This is the canonical method for determining the length of a generated
        # string from an L-system after `n` iterations. Despite being very
        # space-efficient, it is slower than the memoized approach above.
        pi = start_array(lsys)
        A = growth_matrix(lsys)
        return np.sum(pi * (A ** n))

except ImportError as error:
    def matrix_length(lsys, n):
        raise error

#
# Visualization and inspection
#

def print_info(lsys):
    write = sys.stderr.write
    write('V = ' + repr(alphabet(lsys)) + '\n')
    write('ω = ' + repr(lsys.axiom) + '\n')
    write('P = {\n')
    for (v, q) in lsys.rules.items():
        write('    {} → {}\n'.format(repr(v), repr(q)))
    write('}\n\n')

    write('π =\n' + repr(start_array(lsys)) + '\n\n')
    write('A =\n' + repr(growth_matrix(lsys)) + '\n\n')
    write('π * A =\n' + repr(start_array(lsys)*growth_matrix(lsys)) + '\n\n')

def print_dot(lsys):
    print_info(lsys)

    def out(msg):
        sys.stdout.write(msg + '\n')

    out('digraph G {')
    indent = ' '*4
    out(indent + 'bgcolor=transparent;')
    out(indent + 'node[shape=square];')

    # Build a map from each character to a symbol name
    sym = {s: 'v{}'.format(k)
           for (k, s) in enumerate(alphabet(lsys))}


    def print_nodes(entries, extras=[]):
        for v in entries:
            attrs = [('label', '"{}"'.format(v)),
                    ('shape', 'square')] + extras
            fmt_attrs = map(lambda x: '='.join(x), attrs)
            out(indent + '{}[{}];'.format(sym[v], ','.join(fmt_attrs)))

    print_nodes(variables(lsys))
    print_nodes(constants(lsys), [('style', 'filled'),
                                  ('color', 'lightgrey')])

    for vi in variables(lsys):
        for vj in alphabet(lsys):
            n = lsys.rules[vi].count(vj)
            if n > 0:
                label = ' [label=" {}"]'.format(n)
                out(indent + '{} -> {}{};'.format(sym[vi], sym[vj], label))
    out('}')


#
# Testing
#

def random_lsys(n=1000):
    import random
    import string

    def choose_repeat(xs, n):
        return ''.join([random.choice(xs) for _ in xrange(n)])

    letters = string.ascii_lowercase + string.ascii_uppercase
    ab = letters if n >= len(letters) else ''.join(random.sample(letters, n))
    cs = '+-[]'

    class Dummy: pass
    lsys = Dummy()

    lsys.axiom = choose_repeat(ab, n)
    vs = random.sample(ab, len(ab)-1)
    lsys.rules = {
        v: choose_repeat(ab+cs, n) for v in vs
    }
    return lsys

def do_test():
    from examples import Plant
    lsys = Plant #random_lsys(5)
    print_info(lsys)

    for n in xrange(0, 100):
        m = matrix_length(lsys, n)
        r = length(lsys, n)
        sys.stdout.write(' '.join(map(repr, [n, m, r])))
        assert(m == r)

def verify():
    sys.stdout.write('Verifying...\n')
    sys.stdout.flush()
    from examples import Demo, Fibonacci, KochIsland, QuadraticSnowflake, \
                         IslandsAndLakes, Plant, Penrose, Arrowhead, \
                         DragonCurve, Triangle, Stress

    for lsys in [Demo, Fibonacci, KochIsland, QuadraticSnowflake,
                 IslandsAndLakes, Plant, Penrose, Arrowhead,
                 DragonCurve, Triangle, Stress] \
                + [random_lsys(20) for i in xrange(20)]:
        for n in xrange(0,20):
            m = matrix_length(lsys, n)
            r = length(lsys, n)
            assert(m == r)

def benchmark():
    import timeit
    import sys
    from examples import Stress

    verify()

    global lsys
    lsys = Stress

    setup = 'from __main__ import lsys, matrix_length, length'
    prog = '[{}(lsys, n) for n in xrange(20)]'
    for fn, label in [('length', 'Memo (stack)'),
                      ('matrix_length', 'Matrix')]:
        sys.stdout.write('{} method: '.format(label))
        sys.stdout.flush()
        t = timeit.timeit(prog.format(fn), number=100, setup=setup)
        sys.stdout.write(repr(t) + '\n')

def main():
    from examples import Plant
    print_dot(Plant)

if __name__ == '__main__': benchmark()
