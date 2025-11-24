from warnings import warn
from src.heap import Heap
from typing import Any, Callable


def fish_func(x): return x
def fish_cmp(x, y): return -1 if x < y else (0 if x == y else 1)


def bubble_sort(a: list[Any], key: Callable[[Any], Any] | None = None, cmp: Callable[[Any, Any], int] | None = None) \
        -> list[Any]:
    """
        Функция, реализующая алгоритм сортировки пузырьком
        :param a: сортируемый массив
        :param key: ключ сортировки
        :param cmp: компаратор
        :return: Возвращает отсортированный массив
    """
    if len(a) == 0:
        return a
    if not key:
        key = fish_func
    if not cmp:
        cmp = fish_cmp
    for index_1 in range(len(a)):
        for index_2 in range(index_1, len(a)):
            if cmp(key(a[index_1]), key(a[index_2])) == 1:
                a[index_1], a[index_2] = a[index_2], a[index_1]
    return a


def quick_sort(a: list[Any], key: Callable[[Any], Any] | None = None, cmp: Callable[[Any, Any], int] | None = None) \
        -> list[Any]:
    """
        Функция, реализующая алгоритм быстрой сортировки
        :param a: сортируемый массив
        :param key: ключ сортировки
        :param cmp: компаратор
        :return: Возвращает отсортированный массив
    """
    if len(a) == 0:
        return a
    if not key:
        key = fish_func
    if not cmp:
        cmp = fish_cmp
    if len(a) <= 1:
        return a
    elif len(a) == 2:
        return a if cmp(key(a[0]), key(a[1])) == -1 else a[::-1]
    core_elem = len(a) // 2
    left = []
    right = []
    middle = []
    for obj_index in range(len(a)):
        if cmp(key(a[core_elem]), key(a[obj_index])) == 1:
            left.append(a[obj_index])
        elif cmp(key(a[core_elem]), key(a[obj_index])) == -1:
            right.append(a[obj_index])
        else:
            middle.append(a[obj_index])
    left = quick_sort(left)
    right = quick_sort(right)
    return left + middle + right


def counting_sort(a: list[int]) -> list[int]:
    """
        Функция, реализующая алгоритм сортировки подсчётом
        :param a: сортируемый массив
        :return: Возвращает отсортированный массив
    """
    if not isinstance(a[0], int):
        raise ValueError("не целые числа в counting sort")
    if len(a) == 0:
        return a
    max_ = a[0]
    min_ = a[0]
    for obj in a:
        if max_ < obj:
            max_ = obj
        if min_ > obj:
            min_ = obj
    if max_ - min_ > 10 ** 6:
        warn("Внимание, разница между максимумом и минимумом слишком большая, может быть ошибка памяти")
    counter_: list[list[int]] = [[num, 0] for num in range(min_, max_+1)]

    for obj in a:
        counter_[obj-min_][1] += 1

    answer = []

    for num, count in counter_:
        answer += [num] * count

    return answer


def radix_sort(a: list[int], base: int = 10) -> list[int]:
    """
        Функция, реализующая алгоритм сортировки Radix LSD
        :param a: сортируемый массив
        :param base: осонование для распределния чисел
        :return: Возвращает отсортированный массив
    """
    if base < 2:
        raise ValueError("некорректное основание в radix sort")
    if len(a) == 0:
        return a
    if not isinstance(a[0], int):
        raise ValueError("не целые числа в radix sort")
    current_digit = 0
    max_ = max(a)
    while base ** current_digit < max_:
        sub_arrays: list[list[int]] = list()
        for arr_ind in range(base):
            sub_arrays.append([])
        for obj in a:
            sub_arrays[obj // (base ** current_digit) % base].append(obj)
        current_digit += 1
        a_ = []
        for arr in sub_arrays:
            a_.extend(arr)
        a = a_
    return a


def bucket_sort(a: list[float], buckets: int | None = None) -> list[float]:
    """
        Функция, реализующая алгоритм вёдерной сортировки
        :param a: сортируемый массив
        :param buckets: количество "вёдер" для сортировки
        :return: Возвращает отсортированный массив
    """
    if len(a) == 0:
        return a
    if max(a) > 1.0:
        raise ValueError("числа больше 1 в bucket_sort")
    buckets_list: list[list[float]] = []
    if not buckets:
        buckets = 10
    for buck in range(buckets):
        buckets_list.append([])

    for obj in a:
        buckets_list[int(obj * buckets)].append(obj)

    answer = []
    for bucket in buckets_list:
        if len(bucket) != 0:
            bucket = quick_sort(bucket)
            answer.extend(bucket)
    return answer


def heap_sort(a: list[Any], key: Callable[[Any], Any] | None = None, cmp: Callable[[Any, Any], int] | None = None) \
        -> list[Any]:
    """
        Функция, реализующая алгоритм сортировки кучей
        :param a: сортируемый массив
        :param key: ключ сортировки
        :param cmp: компаратор
        :return: Возвращает отсортированный массив
    """
    if len(a) == 0:
        return a
    if not key:
        key = fish_func
    if not cmp:
        cmp = fish_cmp
    heap = Heap(key, cmp)
    for obj in a:
        heap.add(obj)
    heap.heapify(0)

    answer = []

    for ind in range(len(a)):
        answer.append(heap.get_max())

    return answer[::-1]


def lenin_sort(a: list[Any], key: Callable[[Any], Any] | None = None, cmp: Callable[[Any, Any], int] | None = None) \
        -> list[Any]:
    """
        Функция, реализующая алгоритм сортировки "Ленин" (название временное)
        :param a: сортируемый массив
        :param key: ключ сортировки
        :param cmp: компаратор
        :return: Возвращает отсортированный массив
    """
    if not key:
        key = fish_func
    if not cmp:
        cmp = fish_cmp
    stalin_a: list[Any] = []
    sav_a = []
    max_ = a[0]
    for obj_index in range(len(a)):
        if cmp(key(a[obj_index]), key(max_)) != -1:
            stalin_a.append(a[obj_index])
            max_ = a[obj_index]
        else:
            sav_a.append(a[obj_index])
    for obj in sav_a:
        if obj < stalin_a[0]:
            stalin_a.insert(0, obj)
            continue
        left = 0
        right = len(stalin_a) - 1
        while left != right and abs(left - right) != 1:
            if cmp(key(obj), key(stalin_a[(left + right) // 2])) == -1:
                right = (left + right) // 2
            elif cmp(key(obj), key(stalin_a[(left + right) // 2])) == 1:
                left = (left + right) // 2
            elif cmp(key(obj), key(stalin_a[(left + right) // 2])) == 0:
                left = (left + right) // 2
                right = left
        if right < left:
            left, right = right, left
        stalin_a.insert(left+1, obj)
    return stalin_a
