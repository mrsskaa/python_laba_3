import pytest
from src.fibonacci import fibo, fibo_recursive
from src.errors import DigitIsNotNaturalNumberError


class TestFibonacciIterative:
    def test_fibo_returns_1_for_n_equals_1(self):
        result = fibo(1)
        assert result == 1

    def test_fibo_returns_correct_value_for_n_10(self):
        result = fibo(10)
        assert result == 55

    def test_fibo_returns_correct_value_for_n_20(self):
        result = fibo(20)
        assert result == 6765

    def test_fibo_raises_error_for_negative_number(self):
        with pytest.raises(DigitIsNotNaturalNumberError):
            fibo(-1)

    def test_fibo_raises_error_for_float(self):
        with pytest.raises(DigitIsNotNaturalNumberError):
            fibo(0.5)

    def test_fibo_raises_error_for_string(self):
        with pytest.raises(DigitIsNotNaturalNumberError):
            fibo("tralaleylotralala")

    def test_fibo_returns_0_for_n_0(self):
        result = fibo(0)
        assert result == 0

    def test_fibo_returns_1_for_n_2(self):
        result = fibo(2)
        assert result == 1

    def test_fibo_returns_2_for_n_3(self):
        result = fibo(3)
        assert result == 2


class TestFibonacciRecursive:
    def test_fibo_recursive_returns_1_for_n_equals_1(self):
        result = fibo_recursive(1)
        assert result == 1

    def test_fibo_recursive_returns_correct_value_for_n_10(self):
        result = fibo_recursive(10)
        assert result == 55

    def test_fibo_recursive_returns_correct_value_for_n_20(self):
        result = fibo_recursive(20)
        assert result == 6765

    def test_fibo_recursive_raises_error_for_negative_number(self):
        with pytest.raises(DigitIsNotNaturalNumberError):
            fibo_recursive(-1)

    def test_fibo_recursive_raises_error_for_float(self):
        with pytest.raises(DigitIsNotNaturalNumberError):
            fibo_recursive(0.5)

    def test_fibo_recursive_raises_error_for_string(self):
        with pytest.raises(DigitIsNotNaturalNumberError):
            fibo_recursive("tralaleylotralala")

    def test_fibo_recursive_returns_0_for_n_0(self):
        result = fibo_recursive(0)
        assert result == 0

    def test_fibo_recursive_returns_1_for_n_2(self):
        result = fibo_recursive(2)
        assert result == 1

    def test_fibo_recursive_returns_2_for_n_3(self):
        result = fibo_recursive(3)
        assert result == 2

    def test_both_functions_return_same_values(self):
        test_cases = [0, 1, 2, 3, 5, 10, 15]
        for n in test_cases:
            iterative = fibo(n)
            recursive = fibo_recursive(n)
            assert iterative == recursive, f"Мismatch for n={n}"
