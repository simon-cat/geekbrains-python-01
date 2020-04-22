# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random

def sort_union(array):
    if len(array) == 1:
        return array
    first = []
    last = []
    for i in range(len(array)):
        if i < len(array) // 2:
            first.append(array[i])
        else:
            last.append(array[i])
    first_sort = sort_union(first)
    last_sort = sort_union(last)
    print(first_sort,last_sort)
    res = []
    fst, lst = 0, 0
    while fst < len(first_sort) or lst < len(last_sort):
        if fst == len(first_sort):
            res.append(last_sort[lst])
            lst += 1
        elif lst == len(last_sort):
            res.append(first_sort[fst])
            fst += 1
        elif last_sort[lst] < first_sort[fst]:
            res.append(last_sort[lst])
            lst += 1
        elif first_sort[fst] < last_sort[lst]:
            res.append(first_sort[fst])
            fst += 1
    return res

SIZE = 11
main_list = [random.random() * 50 for _ in range(SIZE)]
print('Исходный массив: ', main_list)
sec_list = sort_union(main_list)
print('Отсортированный массив: ', sec_list)