def factorial(n: int) -> int:
    """
    Функция, вычисляющая факториал числа
    :param n: число
    :return: Возвращает факториал числа
    """
    if n < 0:
        raise ValueError("введено число меньше нуля, тут вам не гамма-функция! ")
    answer = 1
    for iter_ in range(n):
        answer *= iter_ + 1
    return answer


def factorial_recursive(n: int) -> int:
    """
    Функция, рекурсивно вычисляющая факториал числа
    :param n: число
    :return: Возвращает факториал числа
    """
    if n < 1:
        raise ValueError("введено число меньше единицы, тут вам не гамма-функция! ")
    elif n == 1:
        return n
    else:
        return n * factorial_recursive(n-1)


def fibo(n: int) -> int:
    """
    Функция, вычисляющая n-ое число Фибоначчи (используется
    формула, полученная решением рекуррентного соотношения чисел Фибоначчи)
    :param n: число
    :return: Возвращает n-ое число Фибоначчи
    """
    if n < 0:
        raise ValueError("Попытка расширить последовательность Фибоначчи на отрицательные индексы")
    n = int(1 / (5 ** 0.5) * (((1 + 5 ** 0.5)/2) ** n - ((1 - 5 ** 0.5)/2) ** n))
    return n


def fibo_recursive(n: int) -> int:
    """
    Функция, рекурсивно вычисляющая n-ое число Фибоначчи
    :param n: число
    :return: Возвращает n-ое число Фибоначчи
    """
    if n < 0:
        raise ValueError("Попытка расширить последовательность Фибоначчи на отрицательные индексы")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_recursive(n - 1) + fibo_recursive(n - 2)
