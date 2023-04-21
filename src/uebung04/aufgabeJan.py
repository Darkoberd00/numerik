# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 13:22:31 2023

@author: janericstorms
"""

import numpy

#LU Zerlegung
def zerlegung(A):
    p = numpy.arange(A.shape[0])
    LU = A.copy() #Kopie von A anlegen
    for i in range(LU.shape[0]):
        if LU[i, i] == 0:
            for j in range(i+1, LU.shape[0]): #Tauschen
                if LU[j, i] != 0:
                    LU[[i, j]] = LU[[j, i]]
                    p[i] = j
                    break
        for j in range(i+1, LU.shape[0]):
            LU[j, i] /= LU[i, i]
            LU[j, i+1:] -= LU[j, i] * LU[i, i+1:]
    return LU, p
def permutation(p, b): # Permutation anwenden
    b_perm = b.copy()
    for i in range(len(p)):
        b_perm[[i, p[i]]] = b_perm[[p[i], i]]
    return b_perm
def vorwaerts(LU, c): # Vorwärts einsetzen
    y = numpy.zeros(c.shape)
    for i in range(y.shape[0]):
        y[i] = c[i] - LU[i, :i] @ y[:i]
    return y
def rueckwaerts(LU, y): # Rückwerts einsetzen
    x = numpy.zeros(y.shape)
    for i in range(y.shape[0]-1, -1, -1):
        x[i] = (y[i] - LU[i, i+1:] @ x[i+1:]) / LU[i, i]
    return x

#Sherman
def sherman(A, b, u, v): # Sherman anwenden
    #Anwendung der LU Zerlegung
    LU, p = zerlegung(A)

    u_perm = permutation(p, u)
    y = vorwaerts(LU, u_perm)

    z = rueckwaerts(LU, y)

    #Testen ob regulär
    div = (1 + v.T @ z)
    if div == 0:
        raise ArithmeticError('1 + v^T z = 0')

    #Sherman anzuwenden
    alpha = 1 / div
    b_perm = permutation(p, b)
    y_2 = vorwaerts(LU, b_perm)

    z_2 = rueckwaerts(LU, y_2)

    x_2 = z_2 - alpha * (v.T @ z_2) * z
    return x_2


def test_function():
    A = numpy.array([[0,0,0,1],[2,1,2,0],[4,4,0,0],[2,3,1,0]])

    u = numpy.array([0,1,2,3])
    v = numpy.array([0,0,0,1])

    b = numpy.array([3,5,4,5])

    result = sherman(A,b,u,v)

    print(result)


test_function()
