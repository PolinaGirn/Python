"""
Задание 1.
Реализуйте свои пользовательские функции, в которых реализуйте:
a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
   И укажите сложность каждой ф-ции, которую вы применяете для заполнения.
   У этих ф-ций может быть разная сложность. Поэтому время заполнения списка и словаря может как совпадать, так и отличаться.
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
   И укажите сложность ф-ций, которые вы используете для операций.
   Операцию clear() не используем.
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
from random import randint
from timeit import timeit


# O(n)
def full_list(lst, n=10000):
    for i in range(n):
        lst.append(randint(0, 100))     # O(1)


# O(n)
def full_dict(dct, n=10000):
    for i in range(n):
        dct[i] = randint(0, 100)        # O(1)


# O(n^2)
def test_list(lst):
    # O(n^2)
    for i in range(500):
        lst.pop(i)              # O(n)
    # O(n)
    for i in range(len(lst)):
        lst[i] = i * 7          # O(1)


# O(n)
def test_dict(dct):
    # O(n)
    for i in range(500):
        dct.pop(i)              # O(1)
    # O(n)
    for i in range(500, len(dct)):
        dct[i] = 'fff'          # O(1)


empty_list = []
empty_dict = {}
print('заполнение списка', timeit('full_list(empty_list)', globals=globals(), number=1))        # 0.0067822
print('заполнение словаря', timeit('full_dict(empty_dict)', globals=globals(), number=1))       # 0.0069906

# Заполнение словаря немного дольше, что странно,
# потому что он должен заполняться быстрее, потому что ведет себя как хеш таблица.
# Тем не менее, сложность функций одинаковая и
# скорость можно считать одинаковой, ссылаясь на погрешность.
# В одном из запусков всё-таки получила другие цифры,
# где словарь заполнялся быстрее
# возможно такая проблема возникает из-за рандома

# print(empty_list)
# print(empty_dict)

print('изменение списка', timeit('test_list(empty_list)', globals=globals(), number=1))        # 0.0014074
print('изменение словаря', timeit('test_dict(empty_dict)', globals=globals(), number=1))       # 0.0005191

# в функции test_list lst.pop(i) имеет линейную сложность. Из-за этого функция работает дольше.
# Если сделать удаление не по индексу, а с конца, время работы будет примерно одинаковым.
# Удаление по индексу (ключу) у списка выполняется быстрее, поэтому и время лучше

# print(empty_list)
# print(empty_dict)
