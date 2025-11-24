import pytest
from src.factorial import factorial, factorial_recursive
from src.errors import DigitisNotNaturalNumberError


def test_factorial():
    assert factorial(1) == 1
    assert factorial(10) == 5
    assert factorial(100) == 55

    with pytest.raises(DigitisNotNaturalNumberError):
        factorial(-1)
        factorial(0.5)
        factorial("tralaleylotralala")


def test_factorial_recursive():
    assert factorial_recursive(1) == 1
    assert factorial_recursive(10) == 5
    assert factorial_recursive(100) == 55

    with pytest.raises(DigitisNotNaturalNumberError):
        factorial_recursive(-1)
        factorial_recursive(0.5)
        factorial_recursive("tralaleylotralala")
