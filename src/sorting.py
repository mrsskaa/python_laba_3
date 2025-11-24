from src.errors import BucketError, NotString, BadType, Empty
from collections import Counter
from typing import Union, List, cast, Optional

def bubble_sort(a: List[Union[int, float, str]]) -> Optional[List[Union[int, float, str]]]:
    """
    Функция реализует сортировку пузырьком
    :param a: исходный массив
    :return: отсортированный массив или None (если ошибка)
    """
    if len(a) == 0:
        raise Empty("Empty Array")


    if type(a[0]) is str:
        for i in a:
            if type(i) is not str:
                raise BadType("there are different types in the same array")
        a_str = cast(List[str], a)
        for i in range(len(a_str)):
            swap = False
            for j in range(1, len(a_str)-i):
                if a_str[j] < a_str[j-1]:
                    a_str[j], a_str[j-1] = a_str[j-1], a_str[j]
                    swap = True
            if not swap:
                break
        return cast(List[Union[int, float, str]], a_str)
    else:
        for i in a:
            if type(i) is str:
                raise BadType("there are different types in the same array")
        a_num = cast(List[Union[int, float]], a)

    for i in range(len(a_num)):
        swap = False
        for j in range(1, len(a_num)-i):
            if a_num[j] < a_num[j-1]:
                a_num[j], a_num[j-1] = a_num[j-1], a_num[j]
                swap = True

        if not swap:
            break

    return cast(List[Union[int, float, str]], a_num)


def quick_sort(a: List[Union[int, float, str]], start: int, finish: int) -> Optional[List[Union[int, float, str]]]:
    """
    Функция реализует быструю сортировку
    :param a: исходный массив
    :param start: граница начала рассмотрения массива
    :param finish: граница конца рассмотрения массива
    :return: отсортированный массив или None (если ошибка)
    """
    if len(a) == 0:
        raise Empty("Empty Array")


    if type(a[0]) is str:
        for i in a:
            if type(i) is not str:
                raise BadType("there are different types in the same array")
        a_str = cast(List[str], a)
        if start < finish:
            pivot_str = a_str[finish]
            i = start - 1

            for j in range(start, finish):
                if a_str[j] <= pivot_str:
                    i += 1
                    a_str[i], a_str[j] = a_str[j], a_str[i]

            a_str[i + 1], a_str[finish] = a_str[finish], a_str[i + 1]

            quick_sort(cast(List[Union[int, float, str]], a_str), start, i)
            quick_sort(cast(List[Union[int, float, str]], a_str), i+2, finish)

        return cast(List[Union[int, float, str]], a_str)
    else:
        for i in a:
            if type(i) is str:
                raise BadType("there are different types in the same array")
        a_num = cast(List[Union[int, float]], a)

        if start < finish:
            pivot_num: Union[int, float] = a_num[finish]
            i = start - 1

            for j in range(start, finish):
                if a_num[j] <= pivot_num:
                    i += 1
                    a_num[i], a_num[j] = a_num[j], a_num[i]

            a_num[i + 1], a_num[finish] = a_num[finish], a_num[i + 1]

            quick_sort(cast(List[Union[int, float, str]], a_num), start, i)
            quick_sort(cast(List[Union[int, float, str]], a_num), i+2, finish)

        return cast(List[Union[int, float, str]], a_num)


def counting_sort(a: List[Union[int, float]]) -> Optional[List[Union[int, float]]]:
    """
    Функция реализует сортировку подсчетом
    :param a: исходный массив
    :return: отсортированный массив или None (если ошибка)
    """
    if len(a) == 0:
        raise Empty("Empty Array")


    for i in a:
        if type(i) is str:
            raise NotString("You can't input string")


    d = Counter(a)
    ans = []

    for i in sorted(d.keys()):
        for j in range(d[i]):
            ans.append(i)

    return ans


def radix_sort(a: List[int], base: int = 10) -> Optional[List[int]]:
    """
    Функция реализует поразрядную сортировку
    :param a: исходный массив
    :param base: система счисления
    :return: отсортированный массив или None (если ошибка)
    """
    if len(a) == 0:
        raise Empty("Empty Array")


    for i in a:
        if type(i) is str:
            raise NotString("You can't input string")


    mx = len(str(max(a)))

    for x in range(mx):
        backet: List[List[int]] = [[] for _ in range(base)]
        for i in range(len(a)):
            backet[(a[i] // base**x)%base].append(a[i])

        cnt = 0
        for bucket_list in backet:
            if bucket_list != []:
                for j in bucket_list:
                    a[cnt] = j
                    cnt += 1

    return a

def bucket_sort(a: List[Union[int, float]], buckets: Optional[int] = None) -> Optional[List[Union[int, float]]]:
    """
    Функция реализует блочную сортировку
    :param a: исходный массив
    :param buckets: количество "блоков", на которые следует разбить массив
    :return: отсортированный массив или None (если ошибка)
    """
    if len(a) == 0:
        raise Empty("Empty Array")


    for i in a:
        if type(i) is str:
            raise NotString("You can't input string")


    if buckets is None:
        buckets = len(a)

    if buckets >= 1:
        bucket: List[List[Union[int, float]]] = [[] for _ in range(buckets)]
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
        for bucket_list in bucket:
            if bucket_list != []:
                sorted_bucket = bubble_sort(cast(List[Union[int, float, str]], bucket_list))
                if sorted_bucket is not None:
                    sorted_bucket_num = cast(List[Union[int, float]], sorted_bucket)
                    for j in sorted_bucket_num:
                        a[cnt] = j
                        cnt += 1

        return a

    else:
        raise BucketError("Bucket must be >0")


def sift_down(a: List[Union[int, float]], start: int, heap_size: int) -> None:
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


def build_max_heap(a: List[Union[int, float]]) -> None:
    """
    Функция строит максимальную кучу
    :param a: исходный массив
    :return: None
    """
    for i in range(len(a) // 2 - 1, -1, -1):
        sift_down(a, i, len(a))


def heap_sort(a: List[Union[int, float]]) -> Optional[List[Union[int, float]]]:
    """
    Функция реализует сортировку кучей
    :param a: исходный массив
    :return: отсортированный массив или None (если ошибка)
    """
    if len(a) == 0:
        raise Empty("Empty Array")

    for i in a:
        if type(i) is str:
            raise NotString("You can't input string")

    build_max_heap(a)

    for i in range(len(a) - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        sift_down(a, 0, i)

    return a
