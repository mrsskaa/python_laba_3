def fibo(n: int) -> int:
    """
    Функция считает n-й член последовательности Фибоначчи с помощью цикла while
    :param n: индекс члена последовательности
    :return: n-й член последовательности
    """
    if n<=2:
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
    Функция считает n-й член последовательности Фибоначчи с помощью рекурсии
    :param n: индекс члена последовательности
    :return: n-й член последовательности
    """
    if n <= 2:
        return 1

    return fibo_recursive(n-1) + fibo_recursive(n-2)
