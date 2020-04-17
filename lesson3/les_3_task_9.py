# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random

matrix = [[random.randint(0, 20) for _ in range(5)] for _ in range(5)]

print('Сгенерированная матрица')
for line in matrix:
    print(line)

min_list = [matrix[0][j] for j in range(5)]
print(min_list)
for j in range(5):
    for i in range(5):
        if matrix[i][j] < min_list[j]:
            min_list[j] = matrix[i][j]

max = min_list[0]
for item in min_list:
    if item > max:
        max = item
print('Список минимальных элементов: ', min_list)
print(f'Максимальное значение из минимальных: {max}')