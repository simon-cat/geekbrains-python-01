# 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
#
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
#
# * задача считается решённой, если в коде использована функция
# вычисления хеша (hash(), sha1() или любая другая из модуля hashlib)

import hashlib

hash_dict = {}
hash_str = {}
str = str(input('Введите строку для обработки >>> '))
len_max = len(str)
for l in range(1, len_max // 2 + 1):
    for i in range(len_max - l + 1):
        a = hashlib.sha1(str[i:i+l].encode('utf-8')).hexdigest()
        if a in hash_dict:
            hash_dict[a] += 1
        else:
            hash_str[a] = str[i:i+l]
            hash_dict[a] = 1
for hash in hash_dict:
    print(f'Подстрока {hash_str[hash]} встречается {hash_dict[hash]} раз')