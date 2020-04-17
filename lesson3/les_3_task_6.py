# 6. В одномерном массиве найти сумму элементов, находящихся
# между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

main_list = [random.randint(0, 100) for _ in range(10)]
print('Первоначальное состояние массива: ', main_list)

max_pos = 0
min_pos = 0
max = main_list[max_pos]
min = main_list[min_pos]

for i, item in enumerate(main_list):
    if item > max:
        max_pos, max = i, item
    if item < min:
        min_pos, min = i, item

if min_pos < max_pos:
    left = min_pos
    right = max_pos
else:
    left = max_pos
    right = min_pos

print(f'Максимальный элемент {max} находится на позиции {max_pos}')
print(f'Минимальный элемент {min} находится на позиции {min_pos}')

if max_pos == min_pos:
    print('Максимальный и минимальный элемент находятся на одной позиции')
else:
    sum = 0
    for i in range(left + 1, right):
        sum += main_list[i]
    print(f'Сумма элементов, находящихся между минимальным и максимальным элементами равна {sum}')