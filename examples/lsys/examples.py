class Fibonacci:
    axiom = 'A'
    rules = {
        'A': 'AB',
        'B': 'A'
    }


class KochIsland:
    axiom = 'F-F-F-F'
    rules = {
        'F': 'F-F+F+FF-F-F+F'
    }

class QuadraticSnowflake:
    axiom = '-F'
    rules = {
        'F': 'F+F-F-F+F'
    }

class IslandsAndLakes:
    axiom = 'F+F+F+F'
    rules = {
        'F': 'F+f-FF+F+FF+Ff+FF-f+FF-F-FF-Ff-FFF',
        'f': 'ffffff'
    }

class Plant:
    axiom = 'X'
    rules = {
        'X': 'F-[[X]+X]+F[+FX]-X',
        'F': 'FF'
    }
    angle = 22.5

class Penrose:
    axiom = '[N]++[N]++[N]++[N]++[N]'
    rules = {
        'M': 'OA++PA----NA[-OA----MA]++',
        'N': '+OA--PA[---MA--NA]+',
        'O': '-MA++NA[+++OA++PA]-',
        'P': '--OA++++MA[+PA++++NA]--NA',
        'A': ''
    }
    angle = 36
