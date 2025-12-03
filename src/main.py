from src.fibonacci import fibo, fibo_recursive
from src.factorial import factorial, factorial_recursive
from src.sorting import bubble_sort, quick_sort, counting_sort,radix_sort, bucket_sort, heap_sort
from typing import cast
from src.errors import IncorrectCommandError, IncorrectSortingNameError, IncorrectWayError
from src.stack_on_list import Stack
from src.queue_on_list import Queue

def main() -> None:
    """
    Обязательная составляющая программы. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    print("Введите команду")
    command = str(input())

    match command:
        case "fibonacci":
            print("Введите n")
            n = int(input())
            print("Введите способ подсчета iterations/recursive")
            way = str(input())

            match way:
                case "iterations":
                    try:
                        print("n-й член Фибоначчи итерационно:", fibo(n))
                    except Exception as error:
                        print(error)

                case "recursive":
                    try:
                        print("n-й член Фибоначчи рекурсивно:", fibo_recursive(n))
                    except Exception as error:
                        print(error)

                case _:
                    raise IncorrectWayError("Такого способа подсчета нет")

        case "factorial":
            print("Введите n")
            n = int(input())
            print("Введите способ подсчета iterations/recursive")
            way = str(input())

            match way:
                case "iterations":
                    try:
                        print("Факториал числа n итерационно:", factorial(n))
                    except Exception as error:
                        print(error)

                case "recursive":
                    try:
                        print("Факториал числа n рекурсивно:", factorial_recursive(n))
                    except Exception as error:
                        print(error)

                case _:
                    raise IncorrectWayError("Такого способа подсчета нет")

        case "sorting":
            print("Введите тип сортировки")
            name = str(input())
            print("Введите массив")
            a = list(map(int, input().split()))
            a_union = cast(list[int | float | str], a)

            match name:
                case "bubble":
                    try:
                        print("Сортировка пузырьком:", bubble_sort(a_union))
                    except Exception as error:
                        print(error)

                case "quick":
                    try:
                        print("Быстрая сортировка:", quick_sort(a_union, 0, len(a)-1))
                    except Exception as error:
                        print(error)

                case "count":
                    a_num = cast(list[int | float], a)

                    try:
                        print("Сортировка подсчетом:", counting_sort(a_num))
                    except Exception as error:
                        print(error)

                case "radix":
                    try:
                        print("Поразрядная сортировка:", radix_sort(a))
                    except Exception as error:
                        print(error)

                case "bucket":
                    print("Введите массив")
                    a_num = cast(list[int | float], a)
                    print("Введите количество блоков")
                    buckets = int(input())

                    try:
                        print("Блочная сортировка:", bucket_sort(a_num, buckets))
                    except Exception as error:
                        print(error)

                case "heap":
                    print("Введите массив")
                    a_num = cast(list[int | float], a)

                    try:
                        print("Сортировка кучей:", heap_sort(a_num))
                    except Exception as error:
                        print(error)

                case _:
                    raise IncorrectSortingNameError("Такой тип сортировки не поддерживается")

        case "stack":
            stack = Stack()

            while (choice := str(input("Введите команду стека\n"))) != 'exit':
                match choice:
                    case "push":
                        print("Введите значение для добавления")
                        x = input()
                        stack.push(x)

                    case "pop":
                        try:
                            print(stack.pop())
                        except Exception as e:
                            print(f"Ошибка: {e}")

                    case "peek":
                        try:
                            value = stack.peek()
                            print(f"Последний элемент стека: '{value}'")
                        except Exception as e:
                            print(f"Ошибка: {e}")

                    case "len":
                        print(f"Размер стека: {len(stack)}")

                    case "is_empty":
                        if stack.is_empty():
                            print("Стек пустой")
                        else:
                            print("Стек не пустой")

                    case _:
                        print("Такой команды не существует")

        case "queue":
            queue = Queue()

            while (choice := str(input("Введите команду очереди\n"))) != 'exit':
                match choice:
                    case "enqueue":
                        print("Введите значение для добавления")
                        x = input()
                        queue.enqueue(x)

                    case "dequeue":
                        try:
                            print(queue.dequeue())
                        except Exception as e:
                            print(f"Ошибка: {e}")

                    case "front":
                        try:
                            value = queue.front()
                            print(f"Первый элемент очереди: '{value}'")
                        except Exception as e:
                            print(f"Ошибка: {e}")

                    case "len":
                        print(f"Размер очереди: {len(queue)}")

                    case "is_empty":
                        if queue.is_empty():
                            print("Очередь пустая")
                        else:
                            print("Очередь не пустая")

                    case _:
                        raise IncorrectCommandError("Такой команды не существует")

        case _:
            raise IncorrectCommandError("Такой команды не существует")





if __name__ == '__main__':
    main()
