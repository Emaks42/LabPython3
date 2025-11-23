from src.sortings import bubble_sort, quick_sort, counting_sort, heap_sort, radix_sort, bucket_sort
from src.generators import reverse_sorted, rand_int_array, rand_float_array, nearly_sorted, many_duplicates
import pytest


@pytest.mark.parametrize("inp,expected", [(many_duplicates(100, 20, 42), sorted(many_duplicates(100, 20, 42))),
                                          (reverse_sorted(100, 42), sorted(reverse_sorted(100, 42))),
                                          (rand_int_array(100, 40, 120, seed=42),
                                           sorted(rand_int_array(100, 40, 120, seed=42))),
                                          (rand_int_array(10, 40, 120, True, seed=42),
                                           sorted(rand_int_array(10, 40, 120, True, seed=42))),
                                          (rand_float_array(100, 0, 1, 42), sorted(rand_float_array(100, 0, 1, 42))),
                                          (nearly_sorted(100, 20, 42), sorted(nearly_sorted(100, 20, 42)))])
def test_bubble(inp, expected):
    assert bubble_sort(inp) == expected


@pytest.mark.parametrize("inp,expected", [(many_duplicates(100, 20, 42), sorted(many_duplicates(100, 20, 42))),
                                          (reverse_sorted(100, 42), sorted(reverse_sorted(100, 42))),
                                          (rand_int_array(100, 40, 120, seed=42),
                                           sorted(rand_int_array(100, 40, 120, seed=42))),
                                          (rand_float_array(100, 0, 1, 42), sorted(rand_float_array(100, 0, 1, 42))),
                                          (nearly_sorted(100, 20, 42), sorted(nearly_sorted(100, 20, 42)))])
def test_quick(inp, expected):
    assert quick_sort(inp) == expected


@pytest.mark.parametrize("inp,expected", [(many_duplicates(100, 20, 42), sorted(many_duplicates(100, 20, 42))),
                                          (reverse_sorted(100, 42), sorted(reverse_sorted(100, 42))),
                                          (rand_int_array(100, 40, 120, seed=42),
                                           sorted(rand_int_array(100, 40, 120, seed=42))),
                                          (rand_float_array(100, 0, 1, 42), sorted(rand_float_array(100, 0, 1, 42))),
                                          (nearly_sorted(100, 20, 42), sorted(nearly_sorted(100, 20, 42)))])
def test_heap(inp, expected):
    assert heap_sort(inp) == expected


@pytest.mark.parametrize("inp,expected", [(many_duplicates(100, 20, 42), sorted(many_duplicates(100, 20, 42))),
                                          (reverse_sorted(100, 42), sorted(reverse_sorted(100, 42))),
                                          (rand_int_array(100, 40, 120, seed=42),
                                           sorted(rand_int_array(100, 40, 120, seed=42))),
                                          (nearly_sorted(100, 20, 42), sorted(nearly_sorted(100, 20, 42)))])
def test_counting(inp, expected):
    assert counting_sort(inp) == expected


@pytest.mark.parametrize("inp,expected", [(many_duplicates(100, 20, 42), sorted(many_duplicates(100, 20, 42))),
                                          (reverse_sorted(100, 42), sorted(reverse_sorted(100, 42))),
                                          (rand_int_array(100, 40, 120, seed=42),
                                           sorted(rand_int_array(100, 40, 120, seed=42))),
                                          (nearly_sorted(100, 20, 42), sorted(nearly_sorted(100, 20, 42)))])
def test_radix(inp, expected):
    assert radix_sort(inp) == expected


@pytest.mark.parametrize("inp,expected", [(rand_float_array(100, 0, 1, 42), sorted(rand_float_array(100, 0, 1, 42)))])
def test_bucket(inp, expected):
    assert bucket_sort(inp) == expected


def test_sort_errors():
    with pytest.raises(ValueError):
        bucket_sort([1000])
    with pytest.raises(ValueError):
        counting_sort([1.000])
    with pytest.raises(ValueError):
        radix_sort([1.000])
    with pytest.raises(ValueError):
        radix_sort([1, 2, 4, 1], -1)
