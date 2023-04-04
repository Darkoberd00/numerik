import math
import sympy as sp
import sympy.vector as spv
import numpy as np


def pqformel(p, q):
    res = (-p)+math.sqrt(p ** 2+q)
    difftozero(p, q, res)
    return "x1="+str(res)


def altformel(p, q):
    x1 = -p-math.sqrt(p ** 2+q)
    res = -q/x1
    difftozero(p, q, res)
    return "x1="+str(res)


def difftozero(p, q, x):
    print("accuracy: "+str(x**2+2*p*x-q))


def esum(x, n):
    sum = 0
    for i in range(n+1):
        sum += math.pow(x, i)/math.factorial(i)
    return str(sum)


def esuminverse(x, n):
    sum = 0
    for i in range(n+1):
        sum += math.pow(x, n-i)/math.factorial(n-i)
    return str(sum)


def area(llim: float, ulim: float, steps: int, formula: sp.Eq):
    area = 0
    width = (ulim-llim)/steps
    i = llim
    x = sp.Symbol('x')
    h = formula.evalf(subs={x: i})
    while i <= ulim:
        area += width*h
        i += width
        h = formula.evalf(subs={x: i})
    print("rect: "+str(area))
    area = 0
    i = llim
    h = formula.evalf(subs={x: i})
    while i <= ulim:
        i += width
        h2 = formula.evalf(subs={x: i})
        area += width*(h+h2)/2
        h = h2
    print("trapez: "+str(area))
    return


def areaVec(llim: float, ulim: float, steps: int, formula: sp.Eq):
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
    print("trapez Vector: "+str(np.trapz(vec, dx=width)))
    return


print("1.a)"+pqformel(10, 1))
print("1.a)"+pqformel(1000, 1))
print("1.a)"+pqformel(100000, 1))
print("1.a)"+pqformel(1000000, 1))
print("1.a)"+pqformel(10000000, 1))

print("1.b)"+altformel(10, 1))
print("1.b)"+altformel(1000, 1))
print("1.b)"+altformel(100000, 1))
print("1.b)"+altformel(1000000, 1))
print("1.b)"+altformel(10000000, 1))


print("2.a)"+esum(2, 1))
print("2.a)"+esum(0.5, 6))
print("2.a)"+esum(12, 10))
print("2.a)"+esum(1, 100))
print("2.a)"+esum(22, 3))

print("2.b)"+esuminverse(2, 1))
print("2.b)"+esuminverse(0.5, 6))
print("2.b)"+esuminverse(12, 10))
print("2.b)"+esuminverse(1, 100))
print("2.b)"+esuminverse(22, 3))

x = sp.Symbol('x')
eq1 = x**-2
eq2 = sp.log(x)
area(0.1, 10, 100, eq1)
area(1, 2, 100, eq2)

areaVec(0.1, 10, 100, eq1)
areaVec(1, 2, 100, eq2)
