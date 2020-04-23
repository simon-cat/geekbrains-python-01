# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
#
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

from collections import namedtuple
from collections import deque

def fill_graph(size):
    graph = {}
    for i in range(size):
        links = str(input(f'Введите связи для вершины #{i} (последовательность цифр без разделителей) '))
        links.strip()
        line = []
        for s in links:
            if (s.isnumeric()) and (int(s) != i) and (0 <= int(s) < size):
                line.append(int(s))
        graph[i] = set(line)
    # graph = {
    #     0: {1, 3, 4},
    #     1: {2, 5},
    #     2: {1, 6},
    #     3: {1, 5, 7},
    #     4: {2, 6},
    #     5: {6},
    #     6: {5},
    #     7: {6},
    # }
    return graph

def find_way(graph, start):
    size = len(graph)
    visited = [0] * size
    routes = deque()
    stack = deque()
    stack.append(start)
    while len(stack) > 0:
        point = stack.pop()
        visited[point] = 1
        for way in graph[point]:
            if visited[way] == 0:
                stack.append(way)
                routes.append(step(point, way))
        # print(point)
    return routes

step = namedtuple('step', ['start', 'end'])

n = int(input('Введите количество вершин графа >>> '))
g = fill_graph(n)
print(g)
start = int(input('start >>> '))
end = int(input('end >>> '))
steps = find_way(g, start)
way = ''
while len(steps) > 0:
    step = steps.pop()
    if step.end == end:
        way = str(step.end) + way
        way = ' -> ' + way
        end = step.start
        if step.start == start:
            break
if start == end:
    way = str(start) + way
    print('Найден путь (не кратчайший): ', way)
else:
    print('Путь не найден')