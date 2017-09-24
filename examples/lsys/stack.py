def interpret(prog):
    state = 0
    stack = []
    for c in prog:
        if c == 'F':
            state += 1
        elif c == '[':
            print 'SAVED STATE:', state
            stack.append(state)
        elif c == ']':
            state = stack.pop()
            print 'RESTORED STATE:', state
        else:
            print 'could not understand:', c
        print 'saw:', c, 'state:', state, 'stack:', stack

def main():
    interpret('F[F[F]F]F')

if __name__ == '__main__': main()
