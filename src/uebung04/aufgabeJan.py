"""
Created on Thu Apr 20 13:22:31 2023

@author: janericstorms
"""

import numpy

#LU Zerlegung
def zerlegung(A, pivot=False):
    p = numpy.arange(A.shape[0])
    LU = A.copy()

    for i in range(LU.shape[0]):
        if pivot:
            # Pivot Element finden
            max_idx = numpy.argmax(numpy.abs(LU[i:, i])) + i
            if max_idx != i:
                p[i] = max_idx
                LU[[i, max_idx]] = LU[[max_idx, i]]
        else:
            if LU[i, i] == 0: #Tauschen
                for j in range(i + 1, LU.shape[0]):
                    if LU[j, i] != 0:
                        p[i] = j
                        LU[[i, j]] = LU[[j, i]]
                        break

        for j in range(i + 1, LU.shape[0]):
            LU[j, i] /= LU[i, i]
            LU[j, i + 1:] -= LU[j, i] * LU[i, i + 1:]

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

def test_function():
    print("Testen der Funktion --> Werte aus Hausaufgabe 3, Aufgabe 2c) \n")

    A = numpy.array([[0,0,0,1],[2,1,2,0],[4,4,0,0],[2,3,1,0]])

    LU, p = zerlegung(A)

    print(f"LU = {LU}")
    print(f"p = {p}")

    b = numpy.array([3,5,4,5])
    c = permutation(p,b)
    y = vorwaerts(LU,c)
    x = rueckwaerts(LU,y)

    print(f"b = {b}")
    print(f"c = {c}")
    print(f"y = {y}")
    print(f"x = {x}")

def pivot_vergleich():
    beta = 10

    for n in [10, 20, 100]:
        A = numpy.eye(n, n) + numpy.diag(numpy.full((n - 1,), -beta), -1)
        A[0, -1] = beta
        A[-1, -1] = 0

        b = numpy.full((n,), 1 - beta)
        b[0] = 1 + beta
        b[-1] = -beta

        for pivot in [True, False]:
            LU, p = zerlegung(A, pivot)
            b_perm = permutation(p, b)
            y = vorwaerts(LU, b_perm)
            x = rueckwaerts(LU, y)
            print(f"n = {n}, pivot = {pivot},x = \n {x}")

    print(f"\n Vergleicht man die Werte, die mit und ohne Pivot erhält, dann fällt auf, dass die Werte mit Pivot besser sind.")


# Aufruf der Funktionen:
test_function()
print("\n")
pivot_vergleich()


