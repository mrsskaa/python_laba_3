from typing import cast
from src.errors import BucketError, NotStringError, BadTypeError, EmptyError, DigitIsNotNaturalNumberError
from collections import Counter


def different_type(a: list[int | float | str]) -> bool:
    """
    Функция проверяет массив на наличие различных типов
    :param a: исходный массив
    :return: True (в массиве разные типы), False (нет)
    """
    if isinstance(a[0], str):
        for i in a:
            if not isinstance(i, str):
                return True
    else:
        for i in a:
            if isinstance(i, str):
                return True

    return False

def string_in_array(a: list[int | float | str]) -> bool:
    """
    Функция проверяет массив на наличие элемента типа str
    :param a: исходный массив
    :return: True (в массиве есть str), False (нет)
    """
    for i in a:
        if isinstance(i, str):
            return True

    return False


def float_in_array(a: list[int | float | str]) -> bool:
    """
    Функция проверяет массив на наличие элемента типа float
    :param a: исходный массив
    :return: True (в массиве есть float), False (нет)
    """
    for i in a:
        if isinstance(i, float):
            return True

    return False


def bubble_sort(a: list[int | float | str]) -> list[int | float | str]:
    """
    Функция реализует сортировку пузырьком
    :param a: исходный массив
    :return: отсортированный массив
    """
    if len(a) == 0:
        raise EmptyError("Empty Array")


    if different_type(a):
        raise BadTypeError("there are different types in the same array")


    for i in range(len(a)):
        swap = False
        for j in range(1, len(a)-i):
            if cast(float, a[j]) < cast(float, a[j-1]):
                a[j], a[j-1] = a[j-1], a[j]
                swap = True

        if not swap:
            break

    return a


def quick_sort(a: list[int | float | str], start: int, finish: int) ->  list[int | float | str]:
    """
    Функция реализует быструю сортировку
    :param a: исходный массив
    :param start: граница начала рассмотрения массива
    :param finish: граница конца рассмотрения массива
    :return: отсортированный массив
    """
    if len(a) == 0:
        raise EmptyError("Empty Array")


    if different_type(a):
        raise BadTypeError("there are different types in the same array")

    if start < finish:
        pivot = a[finish]
        i = start - 1

        for j in range(start, finish):
            if cast(float, a[j]) <= cast(float, pivot):
                i += 1
                a[i], a[j] = a[j], a[i]

        a[i + 1], a[finish] = a[finish], a[i + 1]

        quick_sort(a, start, i)
        quick_sort(a, i+1, finish)

    return a


def counting_sort(a:  list[int]) -> list[int]:
    """
    Функция реализует сортировку подсчетом
    :param a: исходный массив
    :return: отсортированный массив
    """
    if len(a) == 0:
        raise EmptyError("Empty Array")


    if string_in_array(cast(list[int | float | str], a)) or float_in_array(cast(list[int | float | str], a)):
        raise DigitIsNotNaturalNumberError("all must be natural")

    ans = []
    mn = min(a)
    mx = max(a)
    d = Counter(a)
    for i in range(mn, mx):
        if i in d.keys():
            for j in range(d[i]):
                ans.append(i)

    return ans


def radix_sort(a: list[int], base: int = 10) -> list[int]:
    """
    Функция реализует поразрядную сортировку
    :param a: исходный массив
    :param base: система счисления
    :return: отсортированный массив
    """
    if len(a) == 0:
        raise EmptyError("Empty Array")


    if string_in_array(cast(list[int | float | str], a)) or float_in_array(cast(list[int | float | str], a)):
        raise DigitIsNotNaturalNumberError("all must be natural")

    for i in a:
        if i < 0:
            raise DigitIsNotNaturalNumberError("all must be natural")

    mx = len(str(max(a)))

    for x in range(mx):
        bucket = cast(list[list[int]], [[] for _ in range(base)])
        for i in range(len(a)):
            bucket[(a[i] // base**x)%base].append(a[i])

        cnt = 0
        for bucket_list in bucket:
            if bucket_list != []:
                for j in bucket_list:
                    a[cnt] = j
                    cnt += 1

    return a

def bucket_sort(a: list[int | float], buckets: int | None = None) -> list[int | float]:
    """
    Функция реализует блочную сортировку
    :param a: исходный массив
    :param buckets: количество "блоков", на которые следует разбить массив
    :return: отсортированный массив
    """
    if len(a) == 0:
        raise EmptyError("Empty Array")


    if string_in_array(cast(list[int | float | str], a)):
        raise NotStringError("You can't input string")


    if buckets is None:
        buckets = len(a)

    if buckets >= 1:
        bucket = cast(list[list[int | float]], [[] for _ in range(buckets)])
        mx = max(a)
        mn = min(a)

        for i in range(len(a)):
            if mx-mn == 0:
                digit = 0
            else:
                digit = int((a[i]-mn)/(mx-mn) * buckets)

                if digit == buckets:
                    digit = buckets - 1

            bucket[digit].append(a[i])

        cnt = 0
        for current_bucket in bucket:
            if current_bucket != []:
                sorted_bucket = cast(list[int | float], bubble_sort(cast(list[int | float | str], current_bucket)))
                for j in sorted_bucket:
                    a[cnt] = j
                    cnt += 1
        return a

    else:
        raise BucketError("Bucket must be >0")


def sift_down(a:  list[int | float], start: int, heap_size: int) -> None:
    """
    Функция спускает элемент вниз по бинарной куче для восстановления ее свойства
    :param a: исходный массив
    :param start: индекс элемента, который нужно спустить вниз
    :param heap_size: размер кучи на данный момент
    :return: None (функция меняет массив)
    """
    while 2 * start + 1 < heap_size:
        left = 2 * start + 1
        right = 2 * start + 2
        largest = left

        if right < heap_size and a[right] > a[left]:
            largest = right

        if a[start] >= a[largest]:
            break

        a[start], a[largest] = a[largest], a[start]
        start = largest


def build_max_heap(a: list[int | float]) -> None:
    """
    Функция строит максимальную кучу
    :param a: исходный массив
    :return: None
    """
    for i in range(len(a) // 2 - 1, -1, -1):
        sift_down(a, i, len(a))


def heap_sort(a: list[int | float]) -> list[int | float]:
    """
    Функция реализует сортировку кучей
    :param a: исходный массив
    :return: отсортированный массив
    """
    if len(a) == 0:
        raise EmptyError("Empty Array")

    if string_in_array(cast(list[int | float | str], a)):
        raise NotStringError("You can't input string")

    build_max_heap(a)

    for i in range(len(a) - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        sift_down(a, 0, i)

    return a
