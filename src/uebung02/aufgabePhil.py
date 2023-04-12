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

#hole mir die Diagonale von A und die sub diagonale darunter als vektor
def getDiagonal(A):
    n = len(A)
    diagonal = np.zeros(n)
    subdiagonal = np.zeros(n-1)
    for i in range(n):
        diagonal[i] = A[i][i]
        if i < n-1:
            subdiagonal[i] = A[i+1][i]
    return (diagonal, subdiagonal)

def style(diagonal, subdiagonal): 
    return "Diagonal: " + str(diagonal) + " Subdiagonal: " + str(subdiagonal)
        
matrix0 = createTridiagonalgestaltMatrix(4)
print("3.b) n=4 " , getDiagonal(cholesky(matrix0)))
matrix1 = createTridiagonalgestaltMatrix(100) 
print("3.b) n=100 " , getDiagonal(cholesky(matrix1)))
matrix2 = createTridiagonalgestaltMatrix(1000)
print("3.b) n=1000 " , getDiagonal(cholesky(matrix2)))
matrix3 = createTridiagonalgestaltMatrix(10000)
print("3.b) n=10000 " , getDiagonal(cholesky(matrix3)))
