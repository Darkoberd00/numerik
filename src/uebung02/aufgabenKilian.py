# entweder verwende ich numpy ganz oder gar nicht. Danke.

def zerlegung(matrix: list[list]):
    perms = []
    for i in range(matrix.__len__()):
        print(i, matrix)
        res = permutation(matrix, i)
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


def permutation(matrix: list[list], index: int):
    const = index

    while matrix[index][const] == 0:
        index += 1
        if index >= len(matrix):
            return "invalid matrix"
    row = matrix[const].copy()
    matrix[const] = matrix[index]
    matrix[index] = row
    return [matrix, index]


matrix = [[0, 0, 0, 1], [2, 1, 2, 0], [4, 4, 0, 0], [2, 3, 1, 0]]
print(zerlegung(matrix))
