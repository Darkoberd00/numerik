

# Aufgabe 1
# Siehe PDF-File im Zip Ordner

# Aufgabe 2
print("Aufgabe 2: \n")
def zerlegung(matrix: list[list]):
    perms = []
    for i in range(matrix.__len__()):
        res = rowswap(matrix, i)
        if res == "invalid matrix":
            return "invalid matrix"
        matrix = res[0]
        perms.append(res[1])
        for j in range(i+1, matrix.__len__()):
            matrix[j][i] = matrix[j][i]/matrix[i][i]
            for column in range(i+1, matrix.__len__()):
                matrix[j][column] = matrix[j][column] - \
                    matrix[j][i]*matrix[j][i]

    return matrix, perms


def rowswap(matrix: list[list], index: int):
    const = index

    while matrix[index][const] == 0:
        index += 1
        if index >= len(matrix):
            return "invalid matrix"
    row = matrix[const].copy()
    matrix[const] = matrix[index]
    matrix[index] = row
    return [matrix, index]


def permutation(p: list, b: list):
    for i in range(p.__len__()):
        # wunderhübscher tausch von elementen des vektors
        temp = b[i]
        b[i] = b[p[i]]
        b[p[i]] = temp
    return b


def vorwaerts(LU: list[list], c: list):
    ret = []
    for i in range(LU.__len__()):
        ret.append(c[i])
        for j in range(i):
            ret[i] -= LU[i][j]*ret[j]
    return ret


def rueckwaerts(LU: list, y: list):
    ret = []
    for i in reversed(range(LU.__len__())):
        ret.append(y[i])
        for j in reversed(range(LU.__len__(), i)):
            ret[ret.__len__()-1] -= LU[i][j]*ret[j]
    return ret


def matrixgen(size: int):
    ret = []
    for i in range(size):
        ret.append([])
        for j in range(size):
            ret[i].append(1/(i+j+1))
    return ret


def bgen(size: int):
    ret = []
    for i in range(size):
        ret.append(1/(i+1))
    return ret


matrix = [[0, 0, 0, 1], [2, 1, 2, 0], [4, 4, 0, 0], [2, 3, 1, 0]]
zerl = zerlegung(matrix)
print(zerl)
vorw = vorwaerts(zerl[0], permutation(zerl[1], [3, 5, 4, 5]))
print(vorw)
rueck = rueckwaerts(zerl[0], vorw)
print(rueck)
matrix = matrixgen(10)
zerl = zerlegung(matrix)
print(zerl)
b = bgen(10)
vorw = vorwaerts(zerl[0], permutation(zerl[1], b))
print(vorw)
rueck = rueckwaerts(zerl[0], vorw)
print(rueck)


# Aufgabe 3
# Aufgabe 3 a)
# Siehe PDF-File im Zip Ordner

# Aufgabe 3b)
print("\n Aufgabe 3 b: \n")

import math
import sympy as sp
import numpy as np


# Aufgabe 3 b)
# Implementieren Sie in Python eine Cholesky-Zerlegung die die Symmetrie und die spezielle
# Tridiagonalgestalt von A ausnutzt. Speichern Sie dazu die (zwei) wesentlichen Matrixdiagonalen in Vektoren ab.
# Lösen Sie das angegebene Gleichungssystem für n = 100/1000/10000.

def createTridiagonalgestaltMatrix(n):
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                A[i][j] = 2
            elif i == j + 1 or i == j - 1:
                A[i][j] = -1
    return A


def cholesky(A):
    n = len(A)
    L = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1):
            sum = 0
            if i == j:
                for k in range(j):
                    sum += L[j][k] ** 2
                L[j][j] = math.sqrt(A[j][j] - sum)
            elif i > j:
                for k in range(j):
                    sum += L[i][k] * L[j][k]
                L[i][j] = (A[i][j] - sum) / L[j][j]
    return L


# hole mir die Diagonale von A und die sub diagonale darunter als vektor
def getDiagonal(A):
    n = len(A)
    diagonal = np.zeros(n)
    subdiagonal = np.zeros(n - 1)
    for i in range(n):
        diagonal[i] = A[i][i]
        if i < n - 1:
            subdiagonal[i] = A[i + 1][i]
    return (diagonal, subdiagonal)


def style(diagonal, subdiagonal):
    return "Diagonal: " + str(diagonal) + " Subdiagonal: " + str(subdiagonal)


matrix0 = createTridiagonalgestaltMatrix(4)
print("3.b) n=4 ", getDiagonal(cholesky(matrix0)))
matrix1 = createTridiagonalgestaltMatrix(100)
print("3.b) n=100 ", getDiagonal(cholesky(matrix1)))
matrix2 = createTridiagonalgestaltMatrix(1000)
print("3.b) n=1000 ", getDiagonal(cholesky(matrix2)))
matrix3 = createTridiagonalgestaltMatrix(10000)
print("3.b) n=10000 ", getDiagonal(cholesky(matrix3)))

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