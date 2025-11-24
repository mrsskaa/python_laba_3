from src.fibonacci import fibo, fibo_recursive
from src.factorial import factorial, factorial_recursive
from src.sorting import bubble_sort, quick_sort, counting_sort,radix_sort, bucket_sort, heap_sort
from typing import List, Union, cast


def main() -> None:
    n = int(input())


    print(fibo(n))
    print(fibo_recursive(n))


    print(factorial(n))
    print(factorial_recursive(n))


    a = list(map(int, input().split()))

    a_union = cast(List[Union[int, float, str]], a)
    print(bubble_sort(a_union))

    start = int(input())
    finish = int(input())

    print(quick_sort(a_union, start, finish))
    a_num = cast(List[Union[int, float]], a)
    print(counting_sort(a_num))
    print(radix_sort(a))

    buckets = int(input())

    print(bucket_sort(a_num, buckets))
    print(heap_sort(a_num))


if __name__ == '__main__':
    main()
