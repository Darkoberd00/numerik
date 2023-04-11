
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
