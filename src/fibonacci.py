from src.errors import DigitIsNotNaturalNumberError


def fibo(n: int) -> int:
    """
    Функция считает n-й член последовательности Фибоначчи итеративно
    :param n: индекс члена последовательности
    :return: n-й член последовательности
    """
    if n < 0 or not isinstance(n, int):
        raise DigitIsNotNaturalNumberError("n must be int")

    elif n <= 2:
        return n

    first, second = 1, 1
    for i in range(2, n):
        first, second = second, first + second

    return second




def fibo_recursive(n: int) -> int:
    """
    Функция считает n-й член последовательности Фибоначчи рекурсивно
    :param n: индекс члена последовательности
    :return: n-й член последовательности
    """
    if n < 0 or not isinstance(n, int):
        raise DigitIsNotNaturalNumberError("n must be int")

    elif n <= 2:
        return 1

    else:
        return fibo_recursive(n-1) + fibo_recursive(n-2)
