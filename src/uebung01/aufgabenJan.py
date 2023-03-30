# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 12:44:48 2023

@author: jes_f
"""
import numpy
import math

'AUFGABE1 :'
print("Aufgabe1: ")
def x1(p,q):
    x = -p + numpy.sqrt((p**2)+ q)
    return (x)

def x2(p,q):
    x1 = -p - numpy.sqrt((p**2)+ q)
    x2 = -q / x1
    return (x2)

print('Ergebnisse: ')
print('p = 10^2, q = 1')
print(x1(10**2,1))
print(x2(10**2,1))

print('p = 10^4, q = 1')
print(x1(10**4,1))
print(x2(10**4,1))

print('p = 10^6, q = 1')
print(x1(10**6,1))
print(x2(10**6,1))

print('p = 10^7, q = 1')
print(x1(10**7,1))
print(x2(10**7,1))

print('p = 10^8, q = 1')
print(x1(10**8,1))
print(x2(10**8,1))

"""
Ergebnisse: 
p = 10^2, q = 1
0.004999875006248544
0.004999875006249609
p = 10^4, q = 1
5.000000055588316e-05
4.9999999874999996e-05
p = 10^6, q = 1
5.00003807246685e-07
4.999999999998749e-07
p = 10^7, q = 1
5.029141902923584e-08
4.999999999999987e-08
p = 10^8, q = 1
0.0
5e-09

Fazit:
    Die zweite Formel x2 ist für große p genauer.
"""

'Aufgabe2 :'
print()
print("Aufgabe2:")
def expo1(n,x):
    i = 0
    ret = 0
    while (i <= n):
        ret = ret + (x**i)/math.factorial(i)
        i +=1
    return(ret)


def expo2(n,x):
    i = 0
    ret = 0
    while (i <= n):
        ret = ret + (x**(n-i))/math.factorial(n-i)
        i+=1
    return(ret)

print('Ergebnisse: ')
print('n: 10, x: 1')
print(expo1(10,1))
print(expo2(10,1))

print('n: 10, x: 0.75')
print(expo1(10,0.75))
print(expo2(10,0.75))

print('n: 10, x: 0.5')
print(expo1(10,0.5))
print(expo2(10,0.5))

print('n: 10, x: 0.25')
print(expo1(10,0.25))
print(expo2(10,0.25))

print('n: 20, x: 0.5')
print(expo1(20,0.5))
print(expo2(20,0.5))

"""
Aufgabe2:
Ergebnisse: 
n: 10, x: 1
2.7182818011463845
2.7182818011463845
n: 10, x: 0.75
2.1170000154844355
2.117000015484435
n: 10, x: 0.5
1.6487212706873655
1.6487212706873655
n: 10, x: 0.25
1.2840254166877356
1.2840254166877354
n: 20, x: 0.5
1.6487212707001278
1.6487212707001282
"""

'Aufgabe3 :'
print()
print("Aufgabe3:")
def squareRule(f,a,b,n):
    
    return(ret)


def trapezeRule(f,a,b,n):
    
    return(ret)

print('Ergebnisse: ')
print('n: 10, x: 1')
print(expo1(10,1))
print(expo2(10,1))

print('n: 10, x: 0.75')
print(expo1(10,0.75))
print(expo2(10,0.75))

print('n: 10, x: 0.5')
print(expo1(10,0.5))
print(expo2(10,0.5))

print('n: 10, x: 0.25')
print(expo1(10,0.25))
print(expo2(10,0.25))

print('n: 20, x: 0.5')
print(expo1(20,0.5))
print(expo2(20,0.5))

"""
Aufgabe2:
Ergebnisse: 
n: 10, x: 1
2.7182818011463845
2.7182818011463845
n: 10, x: 0.75
2.1170000154844355
2.117000015484435
n: 10, x: 0.5
1.6487212706873655
1.6487212706873655
n: 10, x: 0.25
1.2840254166877356
1.2840254166877354
n: 20, x: 0.5
1.6487212707001278
1.6487212707001282
"""