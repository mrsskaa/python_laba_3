from src.fibonacci import fibo, fibo_recursive
from src.factorial import factorial, factorial_recursive
from src.sorting import bubble_sort, quick_sort, counting_sort,radix_sort, bucket_sort, heap_sort
from typing import List, Union, cast


def main() -> None:
    n = int(input())

    try:
        print("n-й член Фибоначчи итерационно:", fibo(n))
    except Exception as error:
        print(error)


    try:
        print("n-й член Фибоначчи рекурсивно:", fibo_recursive(n))
    except Exception as error:
        print(error)


    try:
        print("Факториал числа n итерационно:", factorial(n))
    except Exception as error:
        print(error)


    try:
        print("Факториал числа n рекурсивно:", factorial_recursive(n))
    except Exception as error:
        print(error)




    a = list(map(int, input().split()))
    a_union = cast(List[Union[int, float, str]], a)

    try:
        print("Сортировка пузырьком:", bubble_sort(a_union))
    except Exception as error:
        print(error)

    start = int(input())
    finish = int(input())

    try:
        print("Быстрая сортировка:", quick_sort(a_union, start, finish))
    except Exception as error:
        print(error)

    a_num = cast(List[Union[int, float]], a)

    try:
        print("Сортировка подсчетом:", counting_sort(a_num))
    except Exception as error:
        print(error)

    try:
        print("Поразрядная сортировка:", radix_sort(a))
    except Exception as error:
        print(error)

    buckets = int(input())

    try:
        print("Блочная сортировка:", bucket_sort(a_num, buckets))
    except Exception as error:
        print(error)

    try:
        print("Сортировка кучей:", heap_sort(a_num))
    except Exception as error:
        print(error)



if __name__ == '__main__':
    main()
