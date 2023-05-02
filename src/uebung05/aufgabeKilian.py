import numpy


def genA(n: int):
    ret = []
    for i in range(n):
        ret.append([])
        current = ret[i]
        for j in range(n):
            if (i == j):
                current.append(1)
            elif (j < i):
                current.append(-1)
            elif (j == n-1):
                current.append(1)
            else:
                current.append(0)

    return ret


def genB(n: int):
    ret = []
    for i in range(n-1):
        ret.append(2-i)
    ret.append(2-n)
    return ret


def householder(A: list):
    matrices = []
    for i in range(A.__len__()-1):
        d = 0
        for j in range(i, A.__len__()):
            d += A[j][i]**2
        alpha = -numpy.sign(A[i][i])*numpy.sqrt(d)
        omega = A[i].copy()
        for j in range(i):
            omega[j] = 0
        omega[i] -= alpha
        beta = 1/(numpy.sqrt(d)*(numpy.sqrt(d)+numpy.abs(A[i][i])))
        s = []
        for x in range(omega.__len__()):
            arr = []
            s.append(arr)
            for y in range(omega.__len__()):
                arr.append(-beta*omega[x]*omega[y])
                if (x == y):
                    arr[x] += 1
        A = numpy.matmul(A, s)
        matrices.append(s)
    Q = matrices[0]
    for i in range(1, matrices.__len__()):
        Q = numpy.matmul(Q, matrices[i])
    return A, Q


A = genA(50)
b = genB(50)
A = householder(A)
print(numpy.linalg.solve(numpy.matmul(A[1], A[0]), b))
