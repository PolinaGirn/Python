"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.
Задача:
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.
В первую очередь необходимо выполнить замеры для ф-ций appendleft, popleft, extendleft дека и для их аналогов у списков.
"""

from timeit import timeit
from collections import deque
from random import randint

num = 100000


def fill_arr_append(arr, count=num):
    for i in range(count):
        arr.append(randint(0, 100))         # O(1)
    return arr


def fill_arr_appendleft(arr, count=num):
    for i in range(count):
        arr.appendleft(randint(0, 100))     # O(1)
    return arr


def fill_arr_insert(arr, count=num):
    for i in range(count):
        arr.insert(0, randint(0, 100))      # O(n)
    return arr


def test_list(arr):
    for i in range(10000):
        arr[randint(1, num-1)] = randint(100, 200)
    return arr


def test_deque(arr):
    for i in range(10000):
        arr[randint(1, num-1)] = randint(100, 200)
    return arr


lst = []
dec = deque()

print('заполнение списка вставка в конец: ', timeit('fill_arr_append(lst)', globals=globals(), number=1))    # 0.0686796
print('заполнение дека вставка в конец: ', timeit('fill_arr_append(dec)', globals=globals(), number=1))      # 0.0685083
# время заполнения вставкой в конец примерно одинаковое, так как сложность .append для списка и дека O(1)

print()
lst.clear()
dec.clear()

print('заполнение списка вставка в начало: ', timeit('fill_arr_insert(lst)', globals=globals(), number=1))   # 2.1193243
print('заполнение дека вставка в начало: ', timeit('fill_arr_appendleft(dec)', globals=globals(), number=1)) # 0.0657532
# вставкой в начало дек заполняется намного быстрее, так как сложность .insert(0, n) для списка O(n)
# а у .appendleft(n) для дека сложность O(1)

print()

print('изменение списка: ', timeit('test_list(lst)', globals=globals(), number=10))     # 0.1342661
print('изменение дека: ', timeit('test_deque(dec)', globals=globals(), number=10))      # 0.3136882
# изменение списка проходит быстрее, чем изменение дека

print()

print('извлечение первого элемента списка: ', timeit('lst.pop(0)', globals=globals(), number=10000))        # 0.2099557
print('извлечение первого элемента дека: ', timeit('dec.popleft()', globals=globals(), number=10000))       # 0.0003927
# извлечение первого элемента быстрее у дека, чем у списка, так как сложность .pop(0) для списка - O(n),
# а сложность .popleft() для дека O(1)

print()

print('извлечение последнего элемента списка: ', timeit('lst.pop()', globals=globals(), number=10000))      # 0.0004311
print('извлечение последнего элемента списка: ', timeit('dec.pop()', globals=globals(), number=10000))      # 0.0004024
# скорость извлечения последнего элемента примерно одинаковая, так как слжность .pop()
# для списка и дека - O(1)








