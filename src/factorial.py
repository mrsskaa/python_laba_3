def factorial(n: int) -> int:
    """
    Функция считает n! с помощью цикла while
    :param n: число, факториал которого надо посчитать
    :return: n!
    """
    if n == 0:
        return 1
    else:
        ans = 1
        while n > 0:
            ans = ans * n
            n -= 1
        return ans

def factorial_recursive(n: int) -> int:
    """
    Функция считает n! с помощью рекурсии
    :param n: число, факториал которого надо посчитать
    :return: n!
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
