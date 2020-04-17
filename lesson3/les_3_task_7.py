# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

import random

main_list = [random.randint(0, 100) for _ in range(10)]
print('Первоначальное состояние массива: ', main_list)

min1_pos = 0
min1 = main_list[min1_pos]

for i, item in enumerate(main_list):
    if item < min1:
        min1_pos, min1 = i, item

min2_pos = 0
min2 = main_list[min2_pos]
for i, item in enumerate(main_list):
    if item < min2 and item > min1:
        min2_pos, min2 = i, item


print(f'Первый минимальный элемент {min1} находится на позиции {min1_pos}')
print(f'Второй минимальный элемент {min2} находится на позиции {min2_pos}')