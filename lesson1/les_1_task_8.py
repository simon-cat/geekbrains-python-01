# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

print('Введите три числа:')
first = int(input('первое число >>> '))
second = int(input('второе число >>> '))
third = int(input('третье число >>> '))

max = first if first > second else second
max = max if max > third else third
min = first if first < second else second
min = min if min < third else third

if first < max and first > min:
    avg = first
elif second < max and second > min:
    avg = second
elif third < max and third > min:
    avg = third
print(f'Среднее число: {avg}')