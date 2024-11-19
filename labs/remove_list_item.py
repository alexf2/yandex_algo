# Импорт модуля os из стандартной библиотеки
# для взаимодействия с операционной системой.
import os
import sys

# Считывание переменной окружения REMOTE_JUDGE, чтобы определить,
# локально выполняется код или на удалённом сервере.
LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

# Если код выполняется на локальном компьютере, то...
if LOCAL:
    # Класс, описывающий элементы связного списка:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(node, idx):
    if idx < 0 or not node:
        # or not isinstance(node, Node):
        raise ValueError('Bad arguments')

    i = 0
    p = node
    prev = None

    while i < idx:
        i = i + 1
        prev = p
        p = p.next_item

    if prev is None:
        prev = p.next_item
        p.next_item = None
        return prev
    else:
        prev.next_item = p.next_item
        p.next_item = None
        return node


def dump(node):
    while node:
        print(node.value)
        node = node.next_item


def wrapper():
    count = int(sys.stdin.readline().strip())

    node = None
    while count > 0:
        node = Node(sys.stdin.readline().strip(), node)
        count = count - 1

    index = int(sys.stdin.readline().strip())

    dump(solution(node, index))


def test():
    node3 = Node("Задача 4: Обследовать грунт в радиусе 3 м", None)
    node2 = Node("Задача 3: Измерить температуру атмосферы", node3)
    node1 = Node("Задача 2: Пробурить скважину глубиной 0.5 м", node2)
    node0 = Node("Задача 1: Фотосъёмка 360°", node1)

    new_head = solution(node0, 1)
    # Выражение, начинающееся с ключевого слова assert,
    # проверяет, что утверждение в выражении истинно.
    # Если утверждение ложно - в этом месте возникнет ошибка.
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3


if __name__ == '__main__':
    """
    if LOCAL:
        test()
    else:
        wrapper()
    """

    wrapper()
