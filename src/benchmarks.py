import timeit
from typing import Callable, Any
from src.sortings import bubble_sort, quick_sort, counting_sort, radix_sort, bucket_sort, heap_sort
from src.generators import rand_int_array, rand_float_array, reverse_sorted, nearly_sorted, many_duplicates


def timeit_once(func, *args, **kwargs) -> float:
    glob: dict[str, Any] = {
        "func": func,
        "args": args,
        "kwargs": kwargs
    }
    return timeit.timeit('func(*args, **kwargs)', globals=glob, number=1)


def benchmark_sorts(arrays: dict[str, list], algos: dict[str, Callable]) -> dict[str, dict[str, float]]:
    result: dict[str, dict[str, float]] = dict()
    for array_name, array in arrays.items():
        new_dict: dict[str, float] = dict()
        for alg_name, alg in algos.items():
            glob: dict[str, Any] = {
                "alg": alg,
                "array": array,
            }
            try:
                new_dict[alg_name] = timeit.timeit("alg(array)", number=10000, globals=glob)
            except TypeError:
                new_dict[alg_name] = -1
            except ValueError:
                new_dict[alg_name] = -1
        result[array_name] = new_dict
    return result


def print_benchmark_table():
    arrs: dict[str, list] = {
        "common array": rand_int_array(1000, 10, 100, seed=42),
        "nearly sorted array": nearly_sorted(1000, 50, seed=42),
        "reverse sorted array": reverse_sorted(1000, seed=42),
        "many duplicates array": many_duplicates(1000, 20, seed=42),
        "float array": rand_float_array(1000, 0, 1, seed=42)
    }
    sortings: dict[str, Callable] = {
        "bubble": bubble_sort,
        "quick": quick_sort,
        "radix": radix_sort,
        "counting": counting_sort,
        "heap": heap_sort,
        "bucket": bucket_sort
    }
    bench = benchmark_sorts(arrs, sortings)
    print(" " * 25, end="")
    for arr_name in sortings.keys():
        print(f"{arr_name: >20}", end=" | ")
    print()
    for arr_name, times in bench.items():
        print(f"{arr_name: >25}", end="")
        for time in times.values():
            print(f"{str(time)[:20]: >20}", end=" | ")
        print()
