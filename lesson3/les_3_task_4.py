# 4. Определить, какое число в массиве встречается чаще всего.

import random

main_list = [random.randint(0, 10) for _ in range(20)]
print('Первоначальное состояние массива: ', main_list)

elems = {}
for item in set(main_list):
    elems[item] = 0

for item in main_list:
    elems[item] += 1

max_key = main_list[0]
max = elems[max_key]
for key in elems.keys():
    if elems[key] > max:
        max, max_key = elems[key], key
print(f'Элемент {max_key} встречает {max} раз. Это самый часто встречающийся элемент')