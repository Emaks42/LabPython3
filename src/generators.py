import random
import time


def rand_int_array(n: int, lo: int, hi: int, distinct=False, seed=None) -> list[int]:
    """
        Функция, генерирующая случайный массив целых чисел
        :param n: количество элементов
        :param lo: минимальная велична элемента массива
        :param hi: максимальная велична элемента массива
        :param distinct: должен ли массив состоять только из уникальных элементов
        :param seed: семя генерации массива
        :return: Возвращает отсортированный массив
    """
    if seed:
        random.seed(seed)
    else:
        random.seed(time.time())
    if distinct:
        answer_: set[int] = set()
        while len(answer_) != n:
            answer_.add(random.randint(lo, hi))
        answer__ = list(answer_)
        random.shuffle(answer__)
        return answer__
    else:
        answer: list[int] = []
        for index in range(n):
            answer.append(random.randint(lo, hi))
        return answer


def nearly_sorted(n: int, swaps: int, seed=None) -> list[int]:
    """
        Функция, генерирующая случайный массив целых чисел, почти отсортированный
        :param n: количество элементов
        :param swaps: количество обменов местами элементов
        :param seed: семя генерации массива
        :return: Возвращает отсортированный массив
    """
    if seed:
        random.seed(seed)
    else:
        random.seed(time.time())
    start = random.randint(1, 100)
    arr = []
    for index in range(n):
        start += random.randint(0, 10)
        arr.append(start)
    for swap_num in range(swaps):
        ind_first = random.randint(0, n-1)
        ind_second = random.randint(0, n-1)
        while ind_second == ind_first:
            ind_second = random.randint(0, n - 1)
        arr[ind_first], arr[ind_second] = arr[ind_second], arr[ind_first]
    return arr


def many_duplicates(n: int, k_unique: int = 5, seed=None) -> list[int]:
    """
        Функция, генерирующая случайный массив целых чисел, в котором много дубликатов
        :param n: количество элементов
        :param k_unique: количество уникальных элементов
        :param seed: семя генерации массива
        :return: Возвращает отсортированный массив
    """
    if seed:
        random.seed(seed)
    else:
        random.seed(time.time())
    arr_unique = []
    for index in range(k_unique):
        arr_unique.append(random.randint(1, 1000))
    arr = []
    for obj in range(k_unique):
        arr += [arr_unique[obj]] * (n // k_unique+1)
    arr = arr[:n]
    random.shuffle(arr)
    return arr


def reverse_sorted(n: int, seed=None) -> list[int]:
    """
        Функция, генерирующая случайный массив целых чисел, отсортированный в обратном порядке
        :param n: количество элементов
        :param seed: семя генерации массива
        :return: Возвращает отсортированный массив
    """
    if seed:
        random.seed(seed)
    else:
        random.seed(time.time())
    start = random.randint(1, 100)
    arr = []
    for index in range(n):
        start += random.randint(0, 10)
        arr.append(start)
    return arr[::-1]


def rand_float_array(n: int, lo: float, hi: float, seed=None) -> list[float]:
    """
        Функция, генерирующая случайный массив вещественных чисел
        :param n: количество элементов
        :param lo: минимальная велична элемента массива
        :param hi: максимальная велична элемента массива
        :param seed: семя генерации массива
        :return: Возвращает отсортированный массив
    """
    if seed:
        random.seed(seed)
    else:
        random.seed(time.time())
    answer = []
    for index in range(n):
        answer.append(random.uniform(lo, hi))
    return answer
