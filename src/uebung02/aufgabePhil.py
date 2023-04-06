import math
import sympy as sp
import numpy as np

# Aufgabe 3 b)
#Implementieren Sie in Python eine Cholesky-Zerlegung die die Symmetrie und die spezielle
#Tridiagonalgestalt von A ausnutzt. Speichern Sie dazu die (zwei) wesentlichen Matrixdiagonalen in Vektoren ab.
#Lösen Sie das angegebene Gleichungssystem für n = 100/1000/10000.

def createTridiagonalgestaltMatrix(n):
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                A[i][j] = 2
            elif i == j+1 or i == j-1:
                A[i][j] = -1
    return A

def cholesky(A):
    n = len(A)
    L = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1):
            sum = 0
            if i == j:
                for k in range(j):
                    sum += L[j][k]**2
                L[j][j] = math.sqrt(A[j][j] - sum)
            elif i > j:
                for k in range(j):
                    sum += L[i][k]*L[j][k]
                L[i][j] = (A[i][j]-sum)/L[j][j]
    return L

def cholesky_spezial(n):
    V1 = np.zeros(n)
    V2 = np.zeros(n)
                

def printMatrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
        
matrix0 = createTridiagonalgestaltMatrix(4)
printMatrix(cholesky(matrix0))
matrix1 = createTridiagonalgestaltMatrix(100) 
matrix2 = createTridiagonalgestaltMatrix(1000)
matrix3 = createTridiagonalgestaltMatrix(10000)
