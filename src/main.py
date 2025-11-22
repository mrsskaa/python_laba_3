from src.fibonacci import fibo
from src.fibonacci import fibo_recursive
from src.factorial import factorial
from src.factorial import factorial_recursive
from src.sorting import bubble_sort
from src.sorting import quick_sort


if __name__ == '__main__':
    print(fibo(5))
    print(fibo_recursive(5))


    print(factorial(5))
    print(factorial_recursive(5))


    print(bubble_sort([1, 4, 2, 1, 5, 8]))
    print(quick_sort([1, 4, 2, 1, 5, 8], 0, 5))