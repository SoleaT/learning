# Напишите функцию для транспонирования матрицы

def matrix_transpose(matrix):
    return list(list(i) for i in zip(*matrix))  # внутренний цикл - чтоб сделать внутри списки, а не кортежи


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix2 = [
    [1, 2],
    [4, 5],
    [7, 8]
]
matrix3 = [
    [1, 2, 3, 7],
    [4, 5, 6, 9],
]

print(matrix)
print(matrix_transpose(matrix))
print(matrix2)
print(matrix_transpose(matrix2))
print(matrix3)
print(matrix_transpose(matrix3))
