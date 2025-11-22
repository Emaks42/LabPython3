from warnings import warn
from src.heap import Heap


def bubble_sort(a: list[int]) -> list[int]:
    """
        Функция, реализующая алгоритм сортировки пузырьком
        :param a: сортируемый массив
        :return: Возвращает отсортированный массив
    """
    for index_1 in range(len(a)):
        for index_2 in range(index_1, len(a)):
            if a[index_1] > a[index_2]:
                a[index_1], a[index_2] = a[index_2], a[index_1]
    return a


def quick_sort(a: list[int]) -> list[int]:
    """
        Функция, реализующая алгоритм быстрой сортировки
        :param a: сортируемый массив
        :return: Возвращает отсортированный массив
    """
    if len(a) <= 1:
        return a
    elif len(a) == 2:
        return a if a[0] < a[1] else a[::-1]
    core_elem = a[len(a) // 2]
    left = []
    right = []
    for obj in a:
        if obj < core_elem:
            left.append(obj)
        elif obj > core_elem:
            right.append(obj)
    left = quick_sort(left)
    right = quick_sort(right)
    return left + [core_elem] + right


def counting_sort(a: list[int]) -> list[int]:
    """
        Функция, реализующая алгоритм сортировки подсчётом
        :param a: сортируемый массив
        :return: Возвращает отсортированный массив
    """
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
        :return: Возвращает отсортированный массив
    """
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
        :return: Возвращает отсортированный массив
    """
    buckets_list: list[list[float]] = []
    if not buckets:
        buckets = 10
    for buck in range(buckets):
        buckets_list.append([])

    for obj in a:
        buckets_list[int(obj * buckets)].append(obj)
    print(buckets_list)

    answer = []
    for bucket in buckets_list:
        if len(bucket) != 0:
            bucket = quick_sort_float(bucket)
            answer.extend(bucket)
    return answer


def heap_sort(a: list[int]) -> list[int]:
    """
        Функция, реализующая алгоритм сортировки кучей
        :param a: сортируемый массив
        :return: Возвращает отсортированный массив
    """
    heap = Heap()
    for obj in a:
        heap.add(obj)
    heap.heapify(0)

    answer = []

    for ind in range(len(a)):
        answer.append(heap.get_max())

    return answer[::-1]


def quick_sort_float(a: list[float]) -> list[float]:
    """
        Функция, реализующая алгоритм быстрой сортировки для чисел с плавающей точкой
        является вспомогательной для bucket_sort
        :param a: сортируемый массив
        :return: Возвращает отсортированный массив
    """
    if len(a) <= 1:
        return a
    elif len(a) == 2:
        return a if a[0] < a[1] else a[::-1]
    core_elem = a[len(a) // 2]
    left = []
    right = []
    for obj in a:
        if obj < core_elem:
            left.append(obj)
        elif obj > core_elem:
            right.append(obj)
    left = quick_sort_float(left)
    right = quick_sort_float(right)
    return left + [core_elem] + right
