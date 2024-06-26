def get_matrix(n, m, value):
    matrix = []
    for _ in range(n):
        row = []
        for _ in range(m):
            row.append(value)
        matrix.append(row)
    return matrix

result_matrix1 = get_matrix(3, 5, 8)
result_matrix2 = get_matrix(7, 2, ':)')
result_matrix3 = get_matrix(5, 5, 5)
print(result_matrix1)
print(result_matrix2)
print(result_matrix3)