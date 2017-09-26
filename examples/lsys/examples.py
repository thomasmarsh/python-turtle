class Demo:
    axiom = 'F'
    rules = {
        'F': 'FF[f]-',
        'f': '+F'
    }
    angle = 20

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

class Arrowhead:
    axiom = 'A'
    rules = {
        'A': 'B-A-B',
        'B': 'A+B+A'
    }
    angle = 60

class DragonCurve:
    axiom = 'FX'
    rules = {
        'X': 'X+YF+',
        'Y': '-FX-Y'
    }

class Triangle:
    axiom = 'W'
    rules = {
        'W': '+++X--F--ZFX+',
        'X': '---W++F++YFW-',
        'Y': '+ZFX--F--Z+++',
        'Z': '-YFW++F++Y---',
    }
    angle = 30
    n = 6
