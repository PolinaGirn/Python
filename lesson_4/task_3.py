"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через cProfile и через timeit
Обязательно предложите еще свой вариант решения и также запрофилируйте!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
Без аналитики задание считается не принятым
"""
from timeit import timeit
import cProfile


# рекурсия. 4е место
def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


# цикл. 3е место
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


# кромсание строки. 1е место
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


# через join и reversed. 2е место
def revers_4(enter_num):
    return ''.join(reversed(str(enter_num)))


def check_1(n, count):
    for i in range(count):
        revers_1(n)


def check_2(n, count):
    for i in range(count):
        revers_2(n)


def check_3(n, count):
    for i in range(count):
        revers_3(n)


def check_4(n, count):
    for i in range(count):
        revers_4(n)


# 4 место
print(f'{"-"*40}revers_1{"-"*40}')
print('timeit: ', timeit('revers_1(12345)', globals=globals()), '\n')       # 1.3335378
cProfile.run('check_1(12345, 1000000)')                                     # 2.055

# 3 место
print(f'{"-"*40}revers_2{"-"*40}')
print('timeit: ', timeit('revers_2(12345)', globals=globals()), '\n')       # 0.9172040999999997
cProfile.run('check_2(12345, 1000000)')                                     # 1.040

# 1 место
print(f'{"-"*40}revers_3{"-"*40}')
print('timeit: ', timeit('revers_3(12345)', globals=globals()), '\n')       # 0.3081391
cProfile.run('check_3(12345, 1000000)')                                     # 0.306

# 2 место
print(f'{"-"*40}revers_4{"-"*40}')
print('timeit: ', timeit('revers_4(12345)', globals=globals()), '\n')       # 0.6248678999999999
cProfile.run('check_4(12345, 1000000)')                                     # 0.794

# самый эффективный вариант через срез списка (revers_3),
# занимает меньше всех остальных времени и выглядит компактно

# мой вариант (revers_4) выглядит меньше и для меня понятнее,
# но тратит немного больше времени. тоже хороший, я считаю
