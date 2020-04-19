# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple


def input_org(order):
    name = str(input(f'Название организации #{order} >>> '))
    q1 = int(input(f'Организация "{name}" - прибыль за 1-ый квартал: '))
    q2 = int(input(f'Организация "{name}" - прибыль за 2-ой квартал: '))
    q3 = int(input(f'Организация "{name}" - прибыль за 3-ий квартал: '))
    q4 = int(input(f'Организация "{name}" - прибыль за 4-ый квартал: '))
    return name, q1, q2, q3, q4, (q1 + q2 + q3 + q4) / 4

props = ['name', 'quarter1', 'quarter2', 'quarter3', 'quarter4', 'average']
titles = ['Наименование', 'Квартал #1', 'Квартал #2', 'Квартал #3', 'Квартал #4', "Среднее"]
New_Org = namedtuple('New_Org', props)

count = int(input('Введите количество организаций >>> '))
orgs = []
for i in range(count):
    org = input_org(i + 1)
    orgs.append(New_Org(org[0], org[1], org[2], org[3], org[4], org[5]))

print(' | '.join(titles))
for org in orgs:
    print(f'{org.name} | {org.quarter1} | {org.quarter2} | {org.quarter3} | {org.quarter4} | {org.average}')

avg = sum([i.average for i in orgs]) / count

above = []
below = []
for org in orgs:
    if org.average > avg:
        above.append(org.name)
    if org.average < avg:
        below.append(org.name)
if len(above) == 0:
    print('Нет организаций с прибылью выше средней')
else:
    print(f'Прибыль выше среднего имеют организации:', ', '.join(above))
if len(below) == 0:
    print('Нет организаций с прибылью ниже средней')
else:
    print(f'Прибыль ниже среднего имеют организации:', ', '.join(below))
