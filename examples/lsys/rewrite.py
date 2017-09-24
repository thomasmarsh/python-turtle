from examples import Fibonacci

def rewrite(lsys, n):
    axiom = lsys.axiom
    for _ in xrange(n):
        result = []
        for c in axiom:
            result.append(lsys.rules.get(c, c))
        axiom = ''.join(result)
    return axiom 

def main():
    for n in range(0, 10):
        r = rewrite(Fibonacci, n)
        print 'n =', n,
        print 'length =', len(r),
        print 'result =', r

if __name__ == '__main__': main()
