from math import factorial as fact_math
from src.functions import factorial, fibo_recursive, factorial_recursive, fibo
import pytest


@pytest.mark.parametrize("inp,expected", [(num, int(fact_math(num))) for num in range(20)])
def test_factorial(inp, expected):
    assert factorial(inp) == expected


@pytest.mark.parametrize("inp,expected", [(num, int(fact_math(num))) for num in range(20)])
def test_factorial_recursive(inp, expected):
    assert factorial_recursive(inp) == expected


@pytest.mark.parametrize("inp,expected", [(1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34)])
def test_fibo(inp, expected):
    assert fibo(inp) == expected


@pytest.mark.parametrize("inp,expected", [(1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34)])
def test_fibo_recursive(inp, expected):
    assert fibo_recursive(inp) == expected


def test_error_less_than_zero():
    with pytest.raises(ValueError):
        fibo_recursive(-1)
    with pytest.raises(ValueError):
        fibo(-1)
    with pytest.raises(ValueError):
        factorial_recursive(-1)
    with pytest.raises(ValueError):
        factorial(-1)
