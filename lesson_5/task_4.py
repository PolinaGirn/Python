"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from timeit import timeit
from collections import OrderedDict
from random import randint

origin_dict = {}
order_dict = OrderedDict()
NUM = 1000000


# не вижу смысла делать разные функции для OrderedDict и обычного словаря,
# так как функции и методы, в них использующиеся, работают с обоими видами словарей.
# Я просто буду в одну функцию поочередно передавать разные словари

def fill_dict(dct, num=NUM):
    for i in range(num):
        dct[i] = randint(0, 100)
    return dct


def test_dict(dct):
    # изменяю все элементы
    for i in range(NUM):
        dct[i] = randint(100, 200)
    # удаляю 10 000 элемнетов
    for i in range(10000):
        dct.pop(i)
    # изменяю четные элементы с проверкой на четность
    for key in dct:
        if key % 2 == 0:
            dct[key] = 'четное'
    return dct


print('заполнение обычного словаря: ', timeit('fill_dict(origin_dict)', globals=globals(), number=1))       # 0.842662
print('заполнение OrderedDict: ', timeit('fill_dict(order_dict)', globals=globals(), number=1))             # 0.8624455
# обычный словарь заполняется быстрее, потому что OrderedDict
# реализован на питоне для быстрого переупорядочивания элементов, а обычный словарь написан на С

print()

print('изменение обычного словаря: ', timeit('test_dict(origin_dict)', globals=globals(), number=5))        # 4.1337375
print('изменение OrderedDict: ', timeit('test_dict(order_dict)', globals=globals(), number=5))              # 4.3962895
# Операции выполняются быстрее с обычным словарем

# Нет смысла использовать OrderedDict на версиях пайтон 3.6 и выше,
# потому что на них обычный словарь тоже поддерживает запоминание порядка добавления элементов.
# OrderedDict пригодится только для использования его особых функций и методов, которых нет у обычного словаря

