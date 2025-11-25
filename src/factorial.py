from src.errors import DigitIsNotNaturalNumberError


def factorial(n: int) -> int:
    """
    Функция считает n! итеративно
    :param n: число, факториал которого надо посчитать
    :return: n!
    """
    if n < 0 or type(n) is float or type(n) is str:
        raise DigitIsNotNaturalNumberError("n must be int")

    elif n == 0:
        return 1

    else:
        ans = 1
        while n > 0:
            ans = ans * n
            n -= 1
        return ans

def factorial_recursive(n: int) -> int:
    """
    Функция считает n! рекурсивно
    :param n: число, факториал которого надо посчитать
    :return: n!
    """
    if n < 0 or type(n) is float or type(n) is str:
        raise DigitIsNotNaturalNumberError("n must be int")

    elif n == 0:
        return 1

    else:
        return n * factorial(n-1)
