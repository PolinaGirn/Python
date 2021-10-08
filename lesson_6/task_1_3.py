from memory_profiler import profile
from random import randint
from numpy import array

# переворачивание числа разными способами


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    result = ''.join(reversed(str(enter_num)))
    return result


@profile
def test_1(num=100000):
    arr = []
    for i in range(num):
        arr.append(revers_2(randint(1000, 10000)))
    # тут какие-то действия


@profile
def test_2(num=100000):
    arr = array([revers_3(randint(1000, 10000)) for i in range(num)])
    # тут какие-то действия
    del arr


@profile
def test_3(num=100000):
    arr = array([revers_4(randint(1000, 10000)) for i in range(num)])
    # тут какие-то действия
    del arr


test_1()
'''
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    27     30.2 MiB     30.2 MiB           1   @profile
    28                                         def test_1(num=100000):
    29     30.2 MiB      0.0 MiB           1       arr = []
    30     34.4 MiB      3.1 MiB      100001       for i in range(num):
    31     34.4 MiB      1.2 MiB      100000           arr.append(revers_2(randint(1000, 10000)))
    32                                             # тут какие-то действия
'''

test_2()
'''
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    35     31.0 MiB     31.0 MiB           1   @profile
    36                                         def test_2(num=100000):
    37     37.1 MiB  -2359.8 MiB      100003       arr = array([revers_3(randint(1000, 10000)) for i in range(num)])
    38                                             # тут какие-то действия
    39     31.1 MiB     -6.0 MiB           1       del arr
'''

test_3()
'''
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    41     31.1 MiB     31.1 MiB           1   @profile
    42                                         def test_3(num=100000):
    43     37.1 MiB      2.7 MiB      100003       arr = array([revers_4(randint(1000, 10000)) for i in range(num)])
    44                                             # тут какие-то действия
    45     31.8 MiB     -5.2 MiB           1       del arr
'''

'''
В первой функции test_1 ничего не меняла, переворот числа там самый медленнный.
Всё сделала через циклы. Прибавка времени: 4.2

Во второй функции test_2 добавила array, списковое включение и удаления ярлыка
Использую самый быстрый переворот строки. Прибавка времени: 0.1

В третьей функции test_3 добавила так же  array, списковое включение и удаления ярлыка
Использую второй по скорости способ переворота строки. Прибавка времени: 0.7
'''
