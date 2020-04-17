# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

main_list = [random.randint(-20, 20) for _ in range(20)]
print('Первоначальное состояние массива: ', main_list)

max = 0
for i, item in enumerate(main_list):
    if item < 0:
        if max == 0:
            max, max_pos = item, i
        else:
            if item > max:
                max, max_pos = item, i

print(f'Максимальный отрицательный элемент в массиве {max} находится на позиции {max_pos}')