# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и
# возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Второй — без использования «Решета Эратосфена».

def is_simple(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def prime(num):
    if num == 0:
        return 0
    if num == 1:
        return 2
    i = prime(num - 1) + 1
    while not is_simple(i):
        i += 1
    return i

def sieve(num):
    size = 10000
    s = [i for i in range(size)]
    s[1] = 0

    for i in range(2, size):
        if s[i] != 0:
            j = i * 2
            while j < size:
                s[j] = 0
                j += i

    ii = 0
    for i in range(size):
        if s[i] != 0:
            ii += 1
            if ii == num:
                break
    return s[i]

# python3 -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve(1)"
# 1000 loops, best of 5: 3.24 msec per loop
#
# python3 -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve(2)"
# 1000 loops, best of 5: 3.24 msec per loop
#
# python3 -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve(5)"
# 1000 loops, best of 5: 3.23 msec per loop

# python3 -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime(1)"
# 1000 loops, best of 5: 351 nsec per loop
#
# python3 -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime(2)"
# 1000 loops, best of 5: 843 nsec per loop
#
# python3 -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime(5)"
# 1000 loops, best of 5: 6.1 usec per loop
