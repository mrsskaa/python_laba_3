import pytest
from src.factorial import factorial, factorial_recursive
from src.errors import DigitIsNotNaturalNumberError


class TestFactorialIterative:
    def test_factorial_returns_1_for_n_equals_1(self):
        result = factorial(1)
        assert result == 1

    def test_factorial_returns_correct_value_for_n_5(self):
        result = factorial(5)
        assert result == 120

    def test_factorial_returns_correct_value_for_n_10(self):
        result = factorial(10)
        assert result == 3628800

    def test_factorial_returns_1_for_n_0(self):
        result = factorial(0)
        assert result == 1

    def test_factorial_returns_2_for_n_2(self):
        result = factorial(2)
        assert result == 2

    def test_factorial_returns_6_for_n_3(self):
        result = factorial(3)
        assert result == 6

    def test_factorial_returns_24_for_n_4(self):
        result = factorial(4)
        assert result == 24

    def test_factorial_raises_error_for_negative_number(self):
        with pytest.raises(DigitIsNotNaturalNumberError):
            factorial(-1)

    def test_factorial_raises_error_for_float(self):
        with pytest.raises(DigitIsNotNaturalNumberError):
            factorial(0.5)

    def test_factorial_raises_error_for_string(self):
        with pytest.raises(DigitIsNotNaturalNumberError):
            factorial("tralaleylotralala")


class TestFactorialRecursive:
    def test_factorial_recursive_returns_1_for_n_equals_1(self):
        result = factorial_recursive(1)
        assert result == 1

    def test_factorial_recursive_returns_correct_value_for_n_5(self):
        result = factorial_recursive(5)
        assert result == 120

    def test_factorial_recursive_returns_correct_value_for_n_10(self):
        result = factorial_recursive(10)
        assert result == 3628800

    def test_factorial_recursive_returns_1_for_n_0(self):
        result = factorial_recursive(0)
        assert result == 1

    def test_factorial_recursive_returns_2_for_n_2(self):
        result = factorial_recursive(2)
        assert result == 2

    def test_factorial_recursive_returns_6_for_n_3(self):
        result = factorial_recursive(3)
        assert result == 6

    def test_factorial_recursive_raises_error_for_negative_number(self):
        with pytest.raises(DigitIsNotNaturalNumberError):
            factorial_recursive(-1)

    def test_factorial_recursive_raises_error_for_float(self):
        with pytest.raises(DigitIsNotNaturalNumberError):
            factorial_recursive(0.5)

    def test_factorial_recursive_raises_error_for_string(self):
        with pytest.raises(DigitIsNotNaturalNumberError):
            factorial_recursive("tralaleylotralala")

    def test_both_functions_return_same_values(self):
        test_cases = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        for n in test_cases:
            iterative = factorial(n)
            recursive = factorial_recursive(n)
            assert iterative == recursive, f"Mismatch for n={n}"
