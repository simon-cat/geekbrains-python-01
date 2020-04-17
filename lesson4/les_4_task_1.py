# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр
# и вывести на экран. Например, если введено число 3486, надо вывести 6843.

# num = 123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890

def reverse_num_recursive(num):
    if num < 10:
        return str(num)
    return str(num % 10) + reverse_num_recursive(num // 10)

def reverse_num(num):
    res = ''
    while num != 0:
        res += str(num % 10)
        num //= 10
    return res

def reverse_num_int(num):
    res = 0
    while num != 0:
        res *= 10
        res += num % 10
        num //= 10
    return res

# python3 -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.reverse_num_int(123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890)"
# 1000 loops, best of 5: 32.2 usec per loop

#  python3 -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.reverse_num(123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890)"
# 1000 loops, best of 5: 47.1 usec per loop

# python3 -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.reverse_num_recursive(123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890)"
# 1000 loops, best of 5: 56.2 usec per loop

# Алгоритм с перестановкой цифр без использования рекурсии и использования преобразования в строку самый эффективный
