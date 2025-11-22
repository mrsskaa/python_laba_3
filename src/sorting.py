def bubble_sort(a: list[int]) -> list[int]:
    for i in range(len(a)):
        swap = False
        for j in range(1, len(a)-i-1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
                swap = True

        if not swap:
            break

    return a


def quick_sort(a: list[int], start: int, finish: int) -> list[int]:
    if start < finish:
        pivot = a[finish]
        i = start - 1

        for j in range(start, finish):
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]

        a[i + 1], a[finish] = a[finish], a[i + 1]

        quick_sort(a, start, i)
        quick_sort(a, i+2, finish)

    return a


def counting_sort(a: list[int]) -> list[int] :
    ...






