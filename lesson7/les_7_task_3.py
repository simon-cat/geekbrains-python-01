# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
#
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте
# метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).

import random

def sort_count(array):
    """Сортировка методом подсчета"""
    count_array = [0 for _ in range(MAX + 1)]
    for item in array:
        count_array[item] += 1
    index = 0
    for i in range(MAX + 1):
        if count_array[i] != 0:
            for j in range(index, index + count_array[i]):
                array[j] = i
            index += count_array[i]

m = int(input('Введите значение для m >>> '))
SIZE = 2*m + 1
MAX = 100
main_list = [random.randint(0, MAX) for _ in range(SIZE)]
print('Исходный массив: ', main_list)
sort_count(main_list)
#print('Отсортированный массив: ', main_list)
med = main_list[len(main_list) // 2]
print('Медиана: ', med)