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
    b_perm = numpy.copy(b)
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

def solve(LU,p,b):
    c = permutation(p, b)
    y = vorwaerts(LU, c)
    x = rueckwaerts(LU, y)
    return x

def solve_with_nachiteration(a, b, eps=1e-10):
    LU, p = zerlegung(a)
    x = solve(LU, p, b)
    i = 0
    while(True):
        i += 1
        ri = b - a @ x
        pk = solve(LU, p, ri)
        x += pk
        if (numpy.linalg.norm(pk)/numpy.linalg.norm(x) < eps):
            break
    print(f'it took {i} steps.')
    return x


def homework_a(eps=1e-10):
    for n in (50, 70, 100):
        a = numpy.zeros((n,)) + numpy.eye(n) + numpy.tril(numpy.full((n, n), -1), -1)
        a[:, -1] = 1
        b = numpy.arange(2, 3 - n, -1, dtype=numpy.float64)
        b = numpy.r_[b, 2 - n]
        x = solve_with_nachiteration(a, b, eps=1e-10)
        print(x)


def homework_b(eps=1e-10):
    for n in (5, 10, 15):
        a = numpy.zeros((n, n), dtype=numpy.float64)
        for i in range(n):
            for j in range(n):
                a[i, j] = 0 if j > i else (1 if j == i else i + j)
        # print(a)
        b = numpy.array([1] + [0] * (n - 1), dtype=numpy.float64)
        x = solve_with_nachiteration(a, b, eps)
        print(x.round() - x)

# Aufruf der Funktionen:
homework_a(5)
print("\n")
homework_b()
