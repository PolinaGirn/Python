"""
Задание 1.
Выполните профилирование памяти в скриптах.
Проанализируйте результат и определите программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.
Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов
Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)
ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
from memory_profiler import profile


@profile
def func_1():
    words = ['процент', 'процента', 'процентов']
    result = []
    for num in range(1, 20):
        if num == 1:
            result.append(str(num) + ' ' + words[0])
            # print(num, words[0])
        elif 1 < num < 5:
            result.append(str(num) + ' ' + words[1])
            # print(num, words[1])
        elif 5 <= num <= 20:
            result.append(str(num) + ' ' + words[2])
            # print(num, words[2])
    print(result)


@profile
def func_2():
    words = ('процент', 'процента', 'процентов')
    result = []
    for num in range(1, 20):
        if num == 1:
            result.append(str(num) + ' ' + words[0])
            # print(num, words[0])
        elif 1 < num < 5:
            result.append(str(num) + ' ' + words[1])
            # print(num, words[1])
        elif 5 <= num <= 20:
            result.append(str(num) + ' ' + words[2])
            # print(num, words[2])
    print(result)
    del words
    del result
    del num



func_1()
'''
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    24     18.9 MiB     18.9 MiB           1   @profile
    25                                         def func_1():
    26     18.9 MiB      0.0 MiB           1       words = ['процент', 'процента', 'процентов']
    27     19.0 MiB      0.0 MiB          20       for num in range(1, 20):
    28     19.0 MiB      0.0 MiB          19           if num == 1:
    29     19.0 MiB      0.0 MiB           1               print(num, words[0])
    30     19.0 MiB      0.0 MiB          18           elif 1 < num < 5:
    31     19.0 MiB      0.0 MiB           3               print(num, words[1])
    32     19.0 MiB      0.0 MiB          15           elif 5 <= num <= 20:
    33     19.0 MiB      0.0 MiB          15               print(num, words[2])
'''

func_2()
'''
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    36     19.0 MiB     19.0 MiB           1   @profile
    37                                         def func_2():
    38     19.0 MiB      0.0 MiB           1       words = ('процент', 'процента', 'процентов')
    39     19.0 MiB      0.0 MiB          20       for num in range(1, 20):
    40     19.0 MiB      0.0 MiB          19           if num == 1:
    41     19.0 MiB      0.0 MiB           1               print(num, words[0])
    42     19.0 MiB      0.0 MiB          18           elif 1 < num < 5:
    43     19.0 MiB      0.0 MiB           3               print(num, words[1])
    44     19.0 MiB      0.0 MiB          15           elif 5 <= num <= 20:
    45     19.0 MiB      0.0 MiB          15               print(num, words[2])
'''

'''
тут я не смогла придумать ничего, кроме кроме замены массива на кортеж и удаления ссылок, 
но даже это дало небольшой результат. хотя наверное просто так совпало
в первом варианте прибавка к памяти 0.1, а во втором её нет. 
'''









