# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
#
# Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

dec_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,\
            '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

hex_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',\
            8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

def sum_h(a, b):
    res = dec_dict[a] + dec_dict[b]
    if res > 15:
        return hex_dict[res // 16] + hex_dict[res % 16]
    else:
        return hex_dict[res]

def mult_h(a, b):
    res = dec_dict[a] * dec_dict[b]
    if res > 15:
        return hex_dict[res // 16] + hex_dict[res % 16]
    else:
        return hex_dict[res]

def sum_full(aa, bb):
    a = deque(aa)
    b = deque(bb)
    if len(a) < len(b):
        a.appendleft('0' * (len(b) - len(a)))
    elif len(b) < len(a):
        b.appendleft('0' * (len(a) - len(b)))

    total = deque()
    balance = ''
    for i in range(len(a)).__reversed__():
        spam = sum_h(a[i], b[i])
        if balance == '':
            total.appendleft(spam[-1])
        else:
            total.appendleft(sum_h(balance, spam[-1]))
        if len(spam) > 1:
            balance = spam[0]
        else:
            balance = ''
    if balance != '':
        total.appendleft(balance)
    return total

def mult_ful(aa, bb):
    a = deque(aa)
    b = deque(bb)

    line = deque()
    rate = 0
    total = []
    for i in range(len(b)).__reversed__():
        line = deque()
        balance = ''
        if rate != 0:
            for r in range(rate):
                line.append('0')
        for j in range(len(a)).__reversed__():
            sum = ''
            spam = mult_h(b[i], a[j])
            if balance == '':
                line.appendleft(spam[-1])
            else:
                sum = sum_h(balance, spam[-1])
                if len(sum) == 1:
                    line.appendleft(sum)
                elif len(sum) > 0:
                    line.appendleft(sum[-1])
            if len(spam) > 1 or len(sum) > 1:
                if len(spam) == 1:
                    if len(sum) == 1:
                        balance = ''
                    elif len(sum) == 2:
                        balance = sum[0]
                elif len(spam) == 2:
                    if len(sum) == 1 or len(sum) == 0:
                        balance = spam[0]
                    elif len(sum) == 2:
                        balance = sum_h(spam[0], sum[0])
            else:
                balance = ''
        line.appendleft(balance)
        if rate == 0:
            total = line
        else:
            total = sum_full(total, line)
        rate += 1

    return total


first = str(input('Введите первое число >>> ')).upper()
second = str(input('Введите второе число >>> ')).upper()

print(sum_full(first, second))
print(mult_ful(first, second))
