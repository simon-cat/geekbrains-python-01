# 2. Доработать алгоритм Дейкстры (рассматривался на уроке),
# чтобы он дополнительно возвращал список вершин, которые необходимо обойти.

from collections import deque

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]

def get_max(graph):
    max = 0
    for line in graph:
        for point in line:
            max += point
    return max

def deykstra(graph, start):
    size = len(graph)
    real_start = start
    limit = get_max(graph) + 1
    is_visited = [False] * size
    cost = [float('inf')] * size
    parent = [-1] * size

    cost[start] = 0
    parent[start] = start
    min_cost = 0

    while min_cost < limit:
        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = limit
        for i in range(size):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    routes = []
    for i in range(size):
        # print(i)
        path = deque()
        if parent[i] == -1:
            routes.append(path)
        else:
            last_step = i
            path.appendleft(str(last_step))
            while last_step != real_start:
                last_step = parent[last_step]
                path.appendleft(str(last_step))
            routes.append(path)

    return routes

s = int(input('Введите номер стартовой вершины >>> '))
result = deykstra(g, s)
for i, line in enumerate(result):
    if len(line) == 0:
        print(f'| {i} | - нет пути - ')
    else:
        print(f'| {i} |', '->'.join(line))