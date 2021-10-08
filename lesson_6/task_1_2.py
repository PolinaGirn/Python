from random import randint
from memory_profiler import profile


@profile
def func_1():
    result = []
    nums = []
    for i in range(100000):
        nums.append(randint(0, 100))

    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            result.append(i)
    # print(result)


@profile
def func_2():
    nums = [randint(0, 100) for i in range(100000)]
    result = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    # print(result)
    del nums
    del result


func_1()
'''
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     5     18.9 MiB     18.9 MiB           1   @profile
     6                                         def func_1():
     7     18.9 MiB      0.0 MiB           1       result = []
     8     18.9 MiB      0.0 MiB           1       nums = []
     9     20.9 MiB  -3821.0 MiB      100001       for i in range(100000):
    10     20.9 MiB  -3819.1 MiB      100000           nums.append(randint(0, 100))
    11                                         
    12     22.4 MiB      0.0 MiB      100001       for i in range(len(nums)):
    13     22.4 MiB      1.5 MiB      100000           if nums[i] % 2 == 0:
    14     22.4 MiB      0.0 MiB       50029               result.append(i)
    15                                             # print(result)
'''


func_2()
'''
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    18     20.4 MiB     20.4 MiB           1   @profile
    19                                         def func_2():
    20     21.1 MiB -53783.7 MiB      100003       nums = [randint(0, 100) for i in range(100000)]
    21     22.4 MiB      1.3 MiB      100003       result = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    22                                             # print(result)
    23     20.9 MiB     -1.4 MiB           1       del nums
    24     19.2 MiB     -1.7 MiB           1       del result
'''

'''
Пришлось немного переделать файл с домашкой, чтобы опыт удался
заменила итераторы на генераторы (или списковое включение, так и не поняла разницу),
добавила удаление ссылок
в первом варианте прибавка памяти: 3.5
во втором варианте прибавки вообще нет.. там -1.2, то есть память стала чище чем была (?)
'''
