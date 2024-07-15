def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        a = []
        matrix.append(a)
        for j in range(m):
            a.append(value)
    return matrix


matrix1 = get_matrix(2, 2, 10)
matrix2 = get_matrix(4, 6, 2)
matrix3 = get_matrix(3, 4, 3)
print(matrix1)
print(matrix2)
print(matrix3)
