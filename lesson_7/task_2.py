"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти).
И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...
Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from random import uniform
from timeit import timeit


def merge(left_lst, right_lst):
    # слияние подсписков
    sorted_lst = []
    left_lst_index = right_lst_index = 0

    left_lst_length, right_lst_length = len(left_lst), len(right_lst)

    for _ in range(left_lst_length + right_lst_length):
        if left_lst_index < left_lst_length and \
                right_lst_index < right_lst_length:
            # Сравниваем первые элементы в начале каждого списка
            # Если первый элемент левого подсписка меньше,
            # добавляем его в отсортированный массив
            if left_lst[left_lst_index] <= right_lst[right_lst_index]:
                sorted_lst.append(left_lst[left_lst_index])
                left_lst_index += 1
            # Если первый элемент правого подсписка меньше,
            # добавляем его в отсортированный массив
            else:
                sorted_lst.append(right_lst[right_lst_index])
                right_lst_index += 1

        # Если достигнут конец левого списка,
        # элементы правого списка добавляем в конец результирующего списка
        elif left_lst_index == left_lst_length:
            sorted_lst.append(right_lst[right_lst_index])
            right_lst_index += 1
        # Если достигнут конец правого списка,
        # элементы левого списка добавляем в отсортированный массив
        elif right_lst_index == right_lst_length:
            sorted_lst.append(left_lst[left_lst_index])
            left_lst_index += 1
    return sorted_lst


def merge_sort(nums):
    if len(nums) <= 1:  # Базовый случай
        return nums

    mid = len(nums) // 2  # Ищем середину списка

    # Сортируем и объединяем подсписки
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Объединяем отсортированные списки в результирующий
    return merge(left_list, right_list)


lst = [round(uniform(0, 50), 3) for _ in range(10)]
print(lst)
print(merge_sort(lst))

# сделаем замеры на массивах разной длины
lst_1 = [uniform(0, 50) for _ in range(100)]
print('длинна массива 100: ', timeit('merge_sort(lst_1[:])', globals=globals(), number=100))        # 0.0299991

print('-' * 50)
lst_2 = [uniform(0, 50) for _ in range(1000)]
print('длинна массива 1000: ', timeit('merge_sort(lst_2[:])', globals=globals(), number=100))       # 0.3751135

print('-' * 50)
lst_3 = [uniform(0, 50) for _ in range(10000)]
print('длинна массива 10000: ', timeit('merge_sort(lst_3[:])', globals=globals(), number=100))      # 3.194591

print('-' * 50)
lst_4 = [uniform(0, 50) for _ in range(100000)]
print('длинна массива 100000: ', timeit('merge_sort(lst_4[:])', globals=globals(), number=100))     # 43.3267371


