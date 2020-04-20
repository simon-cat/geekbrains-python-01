# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

# Программа хранит данные о каждой из организаций тремя разными способами:
#   1. В виде именованного кортежа (namedtuple)
#   2. Обычного списка
#   3. Собственного объекта

import sys
import ctypes
from collections import namedtuple

def show_size(x, level=0):
    print('\t' * level, f'type= {x.__class__}, size= {sys.getsizeof(x)}, object= {x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items:
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)

def input_org(order):
    name = str(input(f'Название организации #{order} >>> '))
    q1 = int(input(f'Организация "{name}" - прибыль за 1-ый квартал: '))
    q2 = int(input(f'Организация "{name}" - прибыль за 2-ой квартал: '))
    q3 = int(input(f'Организация "{name}" - прибыль за 3-ий квартал: '))
    q4 = int(input(f'Организация "{name}" - прибыль за 4-ый квартал: '))
    return name, q1, q2, q3, q4, (q1 + q2 + q3 + q4) / 4


class Organization:

    def __init__(self, name, quarter1, quarter2, quarter3, quarter4, average):
        self.name = name
        self.quarter1 = quarter1
        self.quarter2 = quarter2
        self.quarter3 = quarter3
        self.quarter4 = quarter4
        self.average = average

props = ['name', 'quarter1', 'quarter2', 'quarter3', 'quarter4', 'average']
titles = ['Наименование', 'Квартал #1', 'Квартал #2', 'Квартал #3', 'Квартал #4', "Среднее"]
New_Org = namedtuple('New_Org', props)

count = int(input('Введите количество организаций >>> '))
orgs_1 = []
orgs_2 = []
orgs_3 = []
for i in range(count):
    org = input_org(i + 1)
    orgs_1.append(New_Org(org[0], org[1], org[2], org[3], org[4], org[5]))
    orgs_2.append([org[0], org[1], org[2], org[3], org[4], org[5]])
    orgs_3.append(Organization(org[0], org[1], org[2], org[3], org[4], org[5]))

avg_1 = sum([i.average for i in orgs_1]) / count
avg_2 = sum([i[5] for i in orgs_2]) / count
avg_3 = sum([i.average for i in orgs_3]) / count

print('*' * 60)
print(f'Первый вариант: {avg_1}     Второй вариант: {avg_2}     Третий вариант:{avg_3}')

above = []
below = []
for org in orgs_1:
    if org.average > avg_1:
        above.append(org.name)
    if org.average < avg_1:
        below.append(org.name)
if len(above) == 0:
    print('Нет организаций с прибылью выше средней')
else:
    print(f'Прибыль выше среднего имеют организации:', ', '.join(above))
if len(below) == 0:
    print('Нет организаций с прибылью ниже средней')
else:
    print(f'Прибыль ниже среднего имеют организации:', ', '.join(below))

print('*' * 60)
print(sys.version, sys.platform)
print('*' * 60)
print('Первый вариант:')
show_size(orgs_1[0])
print('*' * 60)
print('Второй вариант:')
show_size(orgs_2[0])
print('*' * 60)
print('Третий вариант:')
show_size(orgs_3[0])
show_size(orgs_3[0].name)
show_size(orgs_3[0].quarter1)
show_size(orgs_3[0].quarter2)
show_size(orgs_3[0].quarter3)
show_size(orgs_3[0].quarter4)
show_size(orgs_3[0].average)
print('*' * 60)

# При любом из вариантов хранения непосредственно данные занимает одинаковый размер в памяти.
# Но при использовании третьего вариант сам объект, хранящий ссылки и описания,
# занимает в памяти минимальный размер
# ************************************************************
# 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52)
# [Clang 6.0 (clang-600.0.57)] darwin
# ************************************************************
# Первый вариант:
#  type= <class '__main__.New_Org'>, size= 104, object= New_Org(name='acme', quarter1=1, quarter2=2, quarter3=3, quarter4=4, average=2.5)
# 	 type= <class 'str'>, size= 53, object= acme
# 	 type= <class 'int'>, size= 28, object= 1
# 	 type= <class 'int'>, size= 28, object= 2
# 	 type= <class 'int'>, size= 28, object= 3
# 	 type= <class 'int'>, size= 28, object= 4
# 	 type= <class 'float'>, size= 24, object= 2.5
# ************************************************************
# Второй вариант:
#  type= <class 'list'>, size= 120, object= ['acme', 1, 2, 3, 4, 2.5]
# 	 type= <class 'str'>, size= 53, object= acme
# 	 type= <class 'int'>, size= 28, object= 1
# 	 type= <class 'int'>, size= 28, object= 2
# 	 type= <class 'int'>, size= 28, object= 3
# 	 type= <class 'int'>, size= 28, object= 4
# 	 type= <class 'float'>, size= 24, object= 2.5
# ************************************************************
# Третий вариант:
#  type= <class '__main__.Organization'>, size= 64, object= <__main__.Organization object at 0x107c9dfd0>
#  type= <class 'str'>, size= 53, object= acme
#  type= <class 'int'>, size= 28, object= 1
#  type= <class 'int'>, size= 28, object= 2
#  type= <class 'int'>, size= 28, object= 3
#  type= <class 'int'>, size= 28, object= 4
#  type= <class 'float'>, size= 24, object= 2.5
# ************************************************************