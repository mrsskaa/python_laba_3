import pytest
from src.fibonacci import fibo, fibo_recursive
from src.errors import DigitIsNotNaturalNumberError


def test_fibo():
    assert fibo(1) == 1
    assert fibo(10) == 55
    assert fibo(20) == 6765

    with pytest.raises(DigitIsNotNaturalNumberError):
        fibo(-1)
        fibo(0.5)
        fibo("tralaleylotralala")


def test_fibo_recursive():
    assert fibo_recursive(1) == 1
    assert fibo_recursive(10) == 55
    assert fibo_recursive(20) == 6765

    with pytest.raises(DigitIsNotNaturalNumberError):
        fibo_recursive(-1)
        fibo_recursive(0.5)
        fibo_recursive("tralaleylotralala")
