# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

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

print(f'Максимальный элемент {max} находится на позиции {max_pos}')
print(f'Минимальный элемент {min} находится на позиции {min_pos}')
main_list[max_pos], main_list[min_pos] = main_list[min_pos], main_list[max_pos]
print('Измененное состояние массива: ', main_list)