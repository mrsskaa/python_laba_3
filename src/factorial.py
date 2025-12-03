from src.errors import DigitIsNotNaturalNumberError


def factorial(n: int) -> int:
    """
    Функция считает n! итеративно
    :param n: число, факториал которого надо посчитать
    :return: n!
    """
    if n < 0 or not isinstance(n, int):
        raise DigitIsNotNaturalNumberError("n must be int")

    if n == 0:
        return 1

    ans = 1

    for i in range(1, n + 1):
        ans *= i

    return ans

def factorial_recursive(n: int) -> int:
    """
    Функция считает n! рекурсивно
    :param n: число, факториал которого надо посчитать
    :return: n!
    """
    if n < 0 or not isinstance(n, int):
        raise DigitIsNotNaturalNumberError("n must be int")

    elif n == 0:
        return 1

    else:
        return n * factorial(n-1)
