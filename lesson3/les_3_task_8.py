# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки
# и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

matrix = [[0 for _ in range(5)] for _ in range(4)]

for i in range(4):
    sum_line = 0
    for j in range(4):
        matrix[i][j] = int(input(f'Введите значение элемента массива {i},{j}: '))
        sum_line += matrix[i][j]
    matrix[i][j + 1] = sum_line

for line in matrix:
    print(line)