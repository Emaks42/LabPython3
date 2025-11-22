from src.functions import factorial, factorial_recursive, fibo, fibo_recursive
from src.sortings import bubble_sort, quick_sort, counting_sort, radix_sort, bucket_sort, heap_sort
from src.stack import interactive_stack
from src.queue import interactive_queue
from typing import  Callable


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
        31: interactive_stack,
        32: interactive_stack,
        33: interactive_stack,
        34: interactive_queue,
        35: interactive_queue,
        36: interactive_queue,
    }
    while True:
        print("Выберите действие:")
        print("1 - применить функцию")
        print("2 - использовать соритровку")
        print("3 - запустить интерактивный объект (стек/очередь)")
        inp = input()
        if inp == "1":
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
        elif inp == "3":
            print("Выберите действие:")
            print("1 - стек через связанный список")
            print("2 - стек через list")
            print("3 - стек на очереди")
            print("4 - очередь через связанный список")
            print("5 - очередь через list")
            print("6 - очередь на стеке")
            inp += input()
        try:
            int(inp)
        except ValueError:
            print("Вы ввели нечто нечитаемое программой, перезапуск диалогового окна")
            continue
        if int(inp) not in actions.keys():
            print("Вы ввели нечто нечитаемое программой, перезапуск диалогового окна")
            continue
        else:
            if 20 < int(inp) < 30:
                print("введите параметры для функции (для сортировки - сначала массив, потом доп параметры):")
                if int(inp) == 25:
                    list_ = list(map(float, input().split()))
                else:
                    list_ = list(map(int, input().split()))
                params = list(map(int, input().split()))
                print("Результат соритровки: ", end="")
                print(*actions[int(inp)](list_, *params))
            elif int(inp) < 20:
                print("введите целое число:")
                try:
                    n = int(input())
                except ValueError:
                    print("Вы ввели нечто нечитаемое программой, перезапуск диалогового окна")
                    continue
                try:
                    print("Результат работы функции: ", end="")
                    print(actions[int(inp)](n))
                except ValueError as e:
                    print(f"ошибка при выполнении функции: {str(e)}")
            elif int(inp) > 30:
                actions[int(inp)](int(inp[-1]) % 3 + 1)
            break


if __name__ == "__main__":
    main()
