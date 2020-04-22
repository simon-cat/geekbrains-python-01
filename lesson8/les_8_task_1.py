# 1. На улице встретились N друзей.
# Каждый пожал руку всем остальным друзьям (по одному разу).
# Сколько рукопожатий было?
# 
# Примечание. Решите задачу при помощи построения графа.

from collections import deque

def make_graph(array, count):
    """Заполнение графа"""
    for i in range(count):
        vertex = []
        for j in range(count):
            if i != j:
                vertex.append(1)
            else:
                vertex.append(0)
        array.append(vertex)

def calc_graph(array):
    """Подсчет количества ребер методом поиска в ширину"""
    vertex_status = [0 for _ in range(SIZE)]
    count = 0
    vertex = deque()
    vertex.appendleft(0)
    while len(vertex) > 0:
        point = vertex.pop()
        vertex_status[point] = 1
        for i in range(SIZE):
            if array[point][i] == 1 and vertex_status[i] == 0:
                vertex.appendleft(i)
                count += 1
    return count
    
SIZE  = int(input('Введите количество друзей >>> '))
graph = []
make_graph(graph, SIZE)
amount = calc_graph(graph)
print(f'Было {amount} рукопожатий')
