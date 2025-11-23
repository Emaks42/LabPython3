from src.functions import factorial, factorial_recursive, fibo, fibo_recursive
from src.sortings import bubble_sort, quick_sort, counting_sort, radix_sort, bucket_sort, heap_sort
from src.generators import rand_int_array, rand_float_array, reverse_sorted, nearly_sorted, many_duplicates
from src.benchmarks import timeit_once, print_benchmark_table
from inspect import signature
from src.stack import interactive_stack
from typing import Callable


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    actions: dict[int, Callable] = {
        11: factorial_recursive,
        12: factorial,
        13: fibo_recursive,
        14: fibo,
        21: bubble_sort,
        22: quick_sort,
        23: counting_sort,
        24: radix_sort,
        25: bucket_sort,
        26: heap_sort,
        41: rand_int_array,
        42: rand_float_array,
        43: reverse_sorted,
        44: many_duplicates,
        45: nearly_sorted,
        3: interactive_stack,
    }
    val_transformations: dict[int, list[Callable]] = {
        1: [int, int, int, bool, int],
        2: [int, float, float, int],
        3: [int, int],
        4: [int, int, int],
        5: [int, int, int]
    }
    flag_t = False
    while True:
        print("Выберите действие:")
        print("1 - применить функцию")
        print("2 - использовать соритровку")
        print("3 - запустить интерактивный стек")
        print("4 - сгенерировать массив")
        print("t - замерить время работы следующего вызванного объекта")
        print("multi_t - замерить время работы всех доступных алгоритмов сортировки (внимание, занимает кучу времени!)")
        print("exec - вывести результат работы заданной функции")
        print("exit - завершить работу")
        inp = input()
        if inp == "exit":
            break
        if inp == "exec":
            print("Введите название функции с параметрами (вида func(x, y)):")
            inp = input()
            print("Результат работы функции:", end=" ")
            try:
                exec(f"print(*{inp})")
            except SyntaxError as e:
                print(f"ошибка при выполнении функции: {str(e)}")
            except ValueError as e:
                print(f"ошибка при выполнении функции: {str(e)}")
            except TypeError as e:
                print(f"ошибка при выполнении функции: {str(e)}")
            continue
        if inp == "t":
            flag_t = True
            continue
        elif inp == "multi_t":
            print_benchmark_table()
            continue
        elif inp == "1":
            print("Выберите действие:")
            print("1 - найти рекурсивно факториал")
            print("2 - найти факториал (без рекурсии)")
            print("3 - найти рекурсивно n-ое число Фибоначчи")
            print("4 - найти n-ое число Фибоначчи (без рекурсии)")
            inp += input()
        elif inp == "2":
            print("Выберите действие:")
            print("1 - bubble sort")
            print("2 - quick sort")
            print("3 - counting sort")
            print("4 - radix sort")
            print("5 - bucket sort")
            print("6 - heap sort")
            inp += input()
        elif inp == "4":
            print("Выберите действие:")
            print("1 - массив случайных целых чисел")
            print("2 - массив случайных вещественных чисел")
            print("3 - массив, отсортированный в обратном порядке")
            print("4 - массив с большим количеством дубликатов")
            print("5 - почти отсортированный массив")
            inp += input()
        try:
            int(inp)
        except ValueError:
            print("Вы ввели нечто нечитаемое программой, перезапуск диалогового окна")
            continue
        if int(inp) not in actions.keys():
            print("Некорректный выбор опций, перезапуск диалогового окна")
            continue
        else:
            if 20 < int(inp) < 30:
                print("введите параметры для функции (для сортировки - сначала массив, потом доп параметры):")
                print(f"сигнатура используемой сортировки: {signature(actions[int(inp)])}")
                try:
                    if int(inp) == 25:
                        list_ = list(map(float, input().split()))
                    else:
                        list_ = list(map(int, input().split()))
                    params = list(map(int, input().split()))
                    print("Результат соритровки: ", end="")
                    print(*actions[int(inp)](list_, *params))
                    if flag_t:
                        print("Время работы:", timeit_once(actions[int(inp)], list_))
                        flag_t = False
                except TypeError:
                    print("некорректно введены аргументы")
                except IndexError:
                    print("некорректно введены аргументы")
            elif 10 < int(inp) < 20:
                print("введите целое число:")
                try:
                    n = int(input())
                except ValueError:
                    print("Вы ввели нечто нечитаемое программой, перезапуск диалогового окна")
                    continue
                try:
                    print("Результат работы функции: ", end="")
                    print(actions[int(inp)](n))
                    if flag_t:
                        print("Время работы:", timeit_once(actions[int(inp)], n))
                        flag_t = False
                except ValueError as e:
                    print(f"ошибка при выполнении функции: {str(e)}")
                except OverflowError as e:
                    print(f"ошибка при выполнении функции: {str(e)}")
                except RecursionError as e:
                    print(f"ошибка при выполнении функции: {str(e)}")
            elif int(inp) < 10:
                actions[int(inp)]()
            elif int(inp) > 40:
                print("введите параметры для генератора:")
                print(f"сигнатура используемого генератора: {signature(actions[int(inp)])}")
                try:
                    par = input().split()
                    for par_ in range(len(par)):
                        par[par_] = val_transformations[int(inp) % 10][par_](par[par_])
                    print(*actions[int(inp)](*par))
                except TypeError:
                    print("некорректно введены аргументы")
                except IndexError:
                    print("некорректно введены аргументы")


if __name__ == "__main__":
    main()
