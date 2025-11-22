def fibo(n: int) -> int:
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
    if n <= 2:
        return 1

    return fibo_recursive(n-1) + fibo_recursive(n-2)