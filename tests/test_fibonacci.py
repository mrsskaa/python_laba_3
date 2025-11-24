import pytest
from src.fibonacci import fibo, fibo_recursive
from src.errors import DigitisNotNaturalNumberError


def test_fibo():
    assert fibo(1) == 1
    assert fibo(10) == 5
    assert fibo(100) == 55

    with pytest.raises(DigitisNotNaturalNumberError):
        fibo(-1)
        fibo(0.5)
        fibo("tralaleylotralala")


def test_fibo_recursive():
    assert fibo_recursive(1) == 1
    assert fibo_recursive(10) == 5
    assert fibo_recursive(100) == 55

    with pytest.raises(DigitisNotNaturalNumberError):
        fibo_recursive(-1)
        fibo_recursive(0.5)
        fibo_recursive("tralaleylotralala")
