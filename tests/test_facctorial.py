import pytest
from src.factorial import factorial, factorial_recursive
from src.errors import DigitIsNotNaturalNumberError


def test_factorial():
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800

    with pytest.raises(DigitIsNotNaturalNumberError):
        factorial(-1)
        factorial(0.5)
        factorial("tralaleylotralala")


def test_factorial_recursive():
    assert factorial_recursive(1) == 1
    assert factorial_recursive(5) == 120
    assert factorial_recursive(10) == 3628800

    with pytest.raises(DigitIsNotNaturalNumberError):
        factorial_recursive(-1)
        factorial_recursive(0.5)
        factorial_recursive("tralaleylotralala")
