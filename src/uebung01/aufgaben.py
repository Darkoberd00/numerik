import math
import sympy as sp
import numpy as np

# Aufgabe 1
def pqformel(p, q): # Formel aus der Aufgabe 1 a)
    res = (-p)+math.sqrt(p ** 2+q)
    difftozero(p, q, res)
    return "x1="+str(res)


def altformel(p, q): # Formel aus der Aufgabe 1 b)
    x1 = -p-math.sqrt(p ** 2+q)
    res = -q/x1
    difftozero(p, q, res)
    return "x1="+str(res)


def difftozero(p, q, x): # Funktion um die Differenz zu 0 zu berechnen
    print("accuracy: "+str(x**2+2*p*x-q))

# Resultate der Aufgabe 1 a) und b)
print("1.a)"+pqformel(10, 1))
print("1.a)"+pqformel(1000, 1))
print("1.a)"+pqformel(100000, 1))
print("1.a)"+pqformel(1000000, 1))
print("1.a)"+pqformel(10000000, 1))
print("")
print("1.b)"+altformel(10, 1))
print("1.b)"+altformel(1000, 1))
print("1.b)"+altformel(100000, 1))
print("1.b)"+altformel(1000000, 1))
print("1.b)"+altformel(10000000, 1))

print("")
# Aufgabe 2
def esum(x, n): # Funktion aus der Aufgabe 2 a)
    sum = 0
    for i in range(n+1):
        sum += math.pow(x, i)/math.factorial(i)
    return str(sum)


def esuminverse(x, n): # Funktion aus der Aufgabe 2 b)
    sum = 0
    for i in range(n+1):
        sum += math.pow(x, n-i)/math.factorial(n-i)
    return str(sum)

# Resultate der Aufgabe 2 a) und b)
print("2.a) "+esum(2, 1))
print("2.a) "+esum(0.5, 6))
print("2.a) "+esum(12, 10))
print("2.a) "+esum(1, 100))
print("2.a) "+esum(22, 3))
print("")
print("2.b) "+esuminverse(2, 1))
print("2.b) "+esuminverse(0.5, 6))
print("2.b) "+esuminverse(12, 10))
print("2.b) "+esuminverse(1, 100))
print("2.b) "+esuminverse(22, 3))

print("")
# Aufgabe 3
def area(llim: float, ulim: float, steps: int, formula: sp.Eq): # Funktion aus der Aufgabe 3
    area = 0
    width = (ulim-llim)/steps
    i = llim
    x = sp.Symbol('x')
    h = formula.evalf(subs={x: i})
    while i <= ulim: # Rechteck-Summe aus der Aufgabe 3
        area += width*h
        i += width
        h = formula.evalf(subs={x: i})
    print("3.) Rechecksumme: "+str(area))
    area = 0
    i = llim
    h = formula.evalf(subs={x: i})
    while i <= ulim: # Trapezregel aus der Aufgabe 3
        i += width
        h2 = formula.evalf(subs={x: i})
        area += width*(h+h2)/2
        h = h2
    print("3.) Trapezsumme: "+str(area))
    return

x = sp.Symbol('x')
eq1 = x**-2
eq2 = sp.log(x)

# Resultate der Aufgabe 3
area(0.1, 10, 100, eq1)
area(1, 2, 100, eq2)

print("")
# Aufgabe 4
def areaVec(llim: float, ulim: float, steps: int, formula: sp.Eq): # Trapezregel in Vektornotation aus der Aufgabe 4
    count = 1
    width = (ulim-llim)/steps
    x = sp.Symbol('x')
    i = llim
    vals = [formula.evalf(subs={x: i})]
    while i <= ulim:
        i += width
        vals.append(formula.evalf(subs={x: i}))
        count = count+1
    vec = np.array(vals)
    print("4.) Trapezregel in Vektornotation: "+str(np.trapz(vec, dx=width)))
    return

# Resultate der Aufgabe 4
areaVec(0.1, 10, 100, eq1)
areaVec(1, 2, 100, eq2)

print("")
# Aufgabe 5
def taylor(k: int, formula: sp.Eq, x0: float): # Taylorentwicklung aus der Aufgabe 5 a)
    taylorsum = 0
    x = sp.Symbol('x')
    for i in range(k):
        taylorsum += (formula.evalf(subs={x: x0})/sp.factorial(i))*(x-x0)**i
        formula = sp.diff(formula, x)
    return taylorsum


def heron(k: int, x: float): # Heron-Verfahren aus der Aufgabe 5 b)
    ret = x
    for i in range(k):
        ret = 0.5*(ret+x/ret)
    return ret

sqrt2 = math.sqrt(2)
eq3 = taylor(10, x**0.5, 1)

# Resultate der Aufgabe 5 a) und b)
print("5.a) Entwicklungspunkt 1, k=10: "+str(eq3.evalf(subs={x: 2})))
print(sqrt2-eq3.evalf(subs={x: 2}))

eq3 = taylor(10, x**0.5, 4)
print("5.a) Entwicklungspunkt 4, k=10 "+str(eq3.evalf(subs={x: 2})))
print(sqrt2-eq3.evalf(subs={x: 2}))

print("5.b) Heron k=10: "+str(heron(10, 2.0)))
print(sqrt2-heron(10, 2))

#   _____                      _           _    __      __         
#  / ____|                    (_)         | |   \ \    / /         
# | |  __  ___ _ __   ___ _ __ _  ___ _ __| |_   \ \  / /__  _ __  
# | | |_ |/ _ \ '_ \ / _ \ '__| |/ _ \ '__| __|   \ \/ / _ \| '_ \ 
# | |__| |  __/ | | |  __/ |  | |  __/ |  | |_     \  / (_) | | | |
#  \_____|\___|_| |_|\___|_|__|_|\___|_|_ _\__| ____\/_\___/|_| |_|
#  / ____| |  | |   /\|__   __|    / ____|  __ \__   __|           
# | |    | |__| |  /  \  | |______| |  __| |__) | | |              
# | |    |  __  | / /\ \ | |______| | |_ |  ___/  | |              
# | |____| |  | |/ ____ \| |      | |__| | |      | |              
#  \_____|_|  |_/_/    \_\_|       \_____|_|      |_|
#  _   _ _      _     _     _ 
# | \ | (_)    | |   | |   | |
# |  \| |_  ___| |__ | |_  | |
# | . ` | |/ __| '_ \| __| | |
# | |\  | | (__| | | | |_  |_|
# |_| \_|_|\___|_| |_|\__| (_)                                                               