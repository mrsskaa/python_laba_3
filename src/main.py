from src.fibonacci import fibo, fibo_recursive
from src.factorial import factorial, factorial_recursive
from src.sorting import bubble_sort, quick_sort, counting_sort,radix_sort, bucket_sort, heap_sort
from typing import List, Union, cast
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

    if command == "fibonacci":
        print("Введите n")
        n = int(input())
        print("Введите способ подсчета iterations/recursive")
        way = str(input())

        if way == "iterations":
            try:
                print("n-й член Фибоначчи итерационно:", fibo(n))
            except Exception as error:
                print(error)

        elif way == "recursive":
            try:
                print("n-й член Фибоначчи рекурсивно:", fibo_recursive(n))
            except Exception as error:
                print(error)

        else:
            raise IncorrectWayError("Такого способа подсчета нет")


    elif command == "factorial":
        print("Введите n")
        n = int(input())
        print("Введите способ подсчета iterations/recursive")
        way = str(input())

        if way == "iterations":
            try:
                print("Факториал числа n итерационно:", factorial(n))
            except Exception as error:
                print(error)

        elif way == "recursive":
            try:
                print("Факториал числа n рекурсивно:", factorial_recursive(n))
            except Exception as error:
                print(error)

        else:
            raise IncorrectWayError("Такого способа подсчета нет")


    elif command == "sorting":
        print("Введите тип сортировки")
        name = str(input())
        print("Введите массив")
        a = list(map(int, input().split()))
        a_union = cast(List[Union[int, float, str]], a)

        if name == "bubble":
            try:
                print("Сортировка пузырьком:", bubble_sort(a_union))
            except Exception as error:
                print(error)


        elif name == "quick":
            try:
                print("Быстрая сортировка:", quick_sort(a_union, 0, len(a)-1))
            except Exception as error:
                print(error)


        elif name == "count":
            a_num = cast(List[Union[int, float]], a)

            try:
                print("Сортировка подсчетом:", counting_sort(a_num))
            except Exception as error:
                print(error)


        elif name == "radix":
            try:
                print("Поразрядная сортировка:", radix_sort(a))
            except Exception as error:
                print(error)


        elif name == "bucket":
            print("Введите массив")
            a_num = cast(List[Union[int, float]], a)
            print("Введите количество блоков")
            buckets = int(input())

            try:
                print("Блочная сортировка:", bucket_sort(a_num, buckets))
            except Exception as error:
                print(error)


        elif name == "heap":
            print("Введите массив")
            a_num = cast(List[Union[int, float]], a)

            try:
                print("Сортировка кучей:", heap_sort(a_num))
            except Exception as error:
                print(error)


        else:
            raise IncorrectSortingNameError("Такой тип сортировки не поддерживается")


    elif command == "stack":
        stack = Stack()

        while True:
            print("Введите команду стека")
            choice = str(input())

            if choice == "push":
                print("Введите значение для добавления")
                x = input()
                stack.push(x)

            elif choice == "pop":
                try:
                    print(stack.pop())
                except Exception as e:
                    print(f"Ошибка: {e}")

            elif choice == "peek":
                try:
                    value = stack.peek()
                    print(f"Последний элемент стека: '{value}'")
                except Exception as e:
                    print(f"Ошибка: {e}")

            elif choice == "len":
                print(f"Размер стека: {len(stack)}")

            elif choice == "is_empty":
                if stack.is_empty():
                    print("Стек пустой")
                else:
                    print("Стек не пустой")

            else:
                print("Такой команды не существует")

    elif command == "queue":
        queue = Queue()

        while True:
            print("Введите команду очереди")
            choice = str(input())

            if choice == "enqueue":
                print("Введите значение для добавления")
                x = input()
                queue.enqueue(x)

            elif choice == "dequeue":
                try:
                    print(queue.dequeue())
                except Exception as e:
                    print(f"Ошибка: {e}")

            elif choice == "front":
                try:
                    value = queue.front()
                    print(f"Первый элемент очереди: '{value}'")
                except Exception as e:
                    print(f"Ошибка: {e}")

            elif choice == "len":
                print(f"Размер очереди: {len(queue)}")

            elif choice == "is_empty":
                if queue.is_empty():
                    print("Очередь пустая")
                else:
                    print("Очередь не пустая")

            else:
                raise IncorrectCommandError("Такой команды не существует")

    else:
        raise IncorrectCommandError("Такой команды не существует")





if __name__ == '__main__':
    main()
