from src.errors import DigitisNotNaturalNumberError


def fibo(n: int) -> int:
    """
    Функция считает n-й член последовательности Фибоначчи итеративно
    :param n: индекс члена последовательности
    :return: n-й член последовательности
    """
    if n < 0 or type(n) is float or type(n) is str:
        raise DigitisNotNaturalNumberError("n must be int")

    elif n<=2:
        return n

    else:
        first = 1
        second = 1
        ans = 1

        while(n>2):
            ans = first + second
            first = second
            second = ans
            n-=1

        return ans




def fibo_recursive(n: int) -> int:
    """
    Функция считает n-й член последовательности Фибоначчи рекурсивно
    :param n: индекс члена последовательности
    :return: n-й член последовательности
    """
    if n < 0 or type(n) is float or type(n) is str:
        raise DigitisNotNaturalNumberError("n must be int")

    elif n <= 2:
        return 1

    else:
        return fibo_recursive(n-1) + fibo_recursive(n-2)
