# 2. Закодируйте любую строку по алгоритму Хаффмана.

from collections import deque

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value  # The node value
        self.left = left    # Left child
        self.right = right  # Right child

def ins_in_que_pos(q, weight):
    """Возвращает позцию куда нужно вставить в отсортированную очередь q элемент весом weight"""
    for i in range(len(q)):
        if q[i][0]>= weight:
            return i
    return -1

def process_tree_search(node, elem, path=''):
    if node.value == elem:
        return f'{path}'
    if node.left != None:
        left_step = process_tree_search(node.left, elem, path + '0')
    else:
        left_step = '-1'
    if node.right != None:
        right_step = process_tree_search(node.right, elem, path + '1')
    else:
        right_step = '-1'
    if right_step == '-1' and left_step == '-1':
        return '-1'
    elif right_step == '-1':
        return left_step
    else:
        return right_step

str_dict = {}
str_vocabulary = {}
str = str(input('Введите строку для кодирования >>> '))
# str = 'beep boop beer!'
for s in str:
    if s in str_dict:
        str_dict[s] += 1
    else:
        str_dict[s] = 1
        str_vocabulary[s] = ''

leaves = deque()
while len(str_dict) > 0:
    max = 0
    for i in str_dict.keys():
        if str_dict[i] > max:
            i_max = i
            max = str_dict[i]
            item_max = str_dict[i]
    leaves.appendleft((item_max, Node(i_max)))
    str_dict.pop(i_max)

while len(leaves) > 1:
    first = leaves.popleft()
    sec = leaves.popleft()
    new = Node(first[0] + sec[0])
    new.left = first[1]
    new.right = sec[1]
    if len(leaves) > 0:
        pos = ins_in_que_pos(leaves, new.value)
        if pos != -1:
            leaves.insert(pos, (new.value, new))
        else:
            leaves.append((new.value, new))
    else:
        root = new

for k in str_vocabulary.keys():
    str_vocabulary[k] = process_tree_search(root, k)
print('Получился словарь:')
print(str_vocabulary)
res = ''
for s in str:
    res += str_vocabulary[s]
    res += ' '
print(f'Закодированная строка выглядит: {res}')