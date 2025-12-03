import pytest
from src.sorting import bubble_sort, quick_sort, bucket_sort, radix_sort, counting_sort, heap_sort
from src.errors import BucketError, EmptyError, BadTypeError, NotStringError, DigitIsNotNaturalNumberError


class TestBubbleSort:
    def test_sorts_integers_correctly(self):
        a = [1, 23, 5, 7, 88, 22, 1, 2, 3, 44]
        result = bubble_sort(a)
        assert result == [1, 1, 2, 3, 5, 7, 22, 23, 44, 88]

    def test_sorts_floats_correctly(self):
        a = [3.5, 1.2, 4.7, 2.1]
        result = bubble_sort(a)
        assert result == [1.2, 2.1, 3.5, 4.7]

    def test_sorts_strings_correctly(self):
        a = ['d', 'q', 'f', 'a', 'y']
        result = bubble_sort(a)
        assert result == ['a', 'd', 'f', 'q', 'y']

    def test_handles_already_sorted_array(self):
        a = [1, 2, 3, 4, 5]
        result = bubble_sort(a)
        assert result == [1, 2, 3, 4, 5]

    def test_handles_single_element(self):
        a = [5]
        result = bubble_sort(a)
        assert result == [5]

    def test_raises_error_on_empty_array(self):
        with pytest.raises(EmptyError):
            bubble_sort([])

    def test_raises_error_on_mixed_types(self):
        with pytest.raises(BadTypeError):
            bubble_sort([1, 2, 'a', 3])


class TestQuickSort:
    def test_sorts_integers_correctly(self):
        a = [1, 23, 5, 7, 88, 22, 1, 2, 3, 44]
        result = quick_sort(a, 0, len(a) - 1)
        assert result == [1, 1, 2, 3, 5, 7, 22, 23, 44, 88]

    def test_sorts_floats_correctly(self):
        a = [3.5, 1.2, 4.7, 2.1]
        result = quick_sort(a, 0, len(a) - 1)
        assert result == [1.2, 2.1, 3.5, 4.7]

    def test_sorts_strings_correctly(self):
        a = ['d', 'q', 'f', 'a', 'y']
        result = quick_sort(a, 0, len(a) - 1)
        assert result == ['a', 'd', 'f', 'q', 'y']

    def test_handles_already_sorted_array(self):
        a = [1, 2, 3, 4, 5]
        result = quick_sort(a, 0, len(a) - 1)
        assert result == [1, 2, 3, 4, 5]

    def test_handles_single_element(self):
        a = [5]
        result = quick_sort(a, 0, 0)
        assert result == [5]

    def test_raises_error_on_empty_array(self):
        with pytest.raises(EmptyError):
            quick_sort([], 0, 0)

    def test_raises_error_on_mixed_types(self):
        with pytest.raises(BadTypeError):
            quick_sort([1, 2, 'a', 3], 0, 3)


class TestCountingSort:
    def test_sorts_integers_correctly(self):
        a = [1, 23, 5, 7, 88, 22, 1, 2, 3, 44]
        result = counting_sort(a)
        assert result == [1, 1, 2, 3, 5, 7, 22, 23, 44, 88]

    def test_sorts_floats_correctly(self):
        a = [3.5, 1.2, 4.7, 2.1]
        result = counting_sort(a)
        assert result == [1.2, 2.1, 3.5, 4.7]

    def test_sorts_array_with_duplicates(self):
        a = [3, 1, 3, 2, 1, 3]
        result = counting_sort(a)
        assert result == [1, 1, 2, 3, 3, 3]

    def test_raises_error_on_empty_array(self):
        with pytest.raises(EmptyError):
            counting_sort([])

    def test_raises_error_with_strings(self):
        with pytest.raises(NotStringError):
            counting_sort([1, 2, 'a', 3])


class TestRadixSort:
    def test_sorts_basic_case(self):
        a = [170, 45, 75, 90, 2, 802, 24, 66]
        result = radix_sort(a)
        assert result == [2, 24, 45, 66, 75, 90, 170, 802]

    def test_sorts_with_custom_base(self):
        a = [170, 45, 75, 90, 2]
        result = radix_sort(a, 10)
        assert result == [2, 45, 75, 90, 170]

    def test_handles_already_sorted_array(self):
        a = [1, 2, 3, 4, 5]
        result = radix_sort(a)
        assert result == [1, 2, 3, 4, 5]

    def test_raises_error_on_empty_array(self):
        with pytest.raises(EmptyError):
            radix_sort([])

    def test_raises_error_with_strings(self):
        with pytest.raises(DigitIsNotNaturalNumberError):
            radix_sort([1, 2, 'tralalaylotralala', 3])

    def test_raises_error_with_floats(self):
        with pytest.raises(DigitIsNotNaturalNumberError):
            radix_sort([3.5, 1.2, 4.7, 2.1])

    def test_raises_error_with_negatives(self):
        with pytest.raises(DigitIsNotNaturalNumberError):
            radix_sort([1, 2, 3, -1])


class TestBucketSort:
    def test_sorts_floats_default_buckets(self):
        a = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
        result = bucket_sort(a)
        assert result == [0.32, 0.33, 0.37, 0.42, 0.47, 0.51, 0.52]

    def test_sorts_floats_with_custom_buckets(self):
        a = [0.42, 0.32, 0.33, 0.52, 0.37]
        result = bucket_sort(a, 5)
        assert result == [0.32, 0.33, 0.37, 0.42, 0.52]

    def test_sorts_integers(self):
        a = [64, 34, 25, 12, 22, 11, 90]
        result = bucket_sort(a)
        assert result == [11, 12, 22, 25, 34, 64, 90]

    def test_handles_all_equal_elements(self):
        a = [5, 5, 5, 5]
        result = bucket_sort(a)
        assert result == [5, 5, 5, 5]

    def test_raises_error_on_empty_array(self):
        with pytest.raises(EmptyError):
            bucket_sort([])

    def test_raises_error_with_strings(self):
        with pytest.raises(NotStringError):
            bucket_sort([1, 2, 'a', 3])

    def test_raises_error_with_zero_buckets(self):
        with pytest.raises(BucketError):
            bucket_sort([0.5, 0.3, 0.7], 0)

    def test_raises_error_with_negative_buckets(self):
        with pytest.raises(BucketError):
            bucket_sort([0.5, 0.3, 0.7], -1)


class TestHeapSort:
    def test_sorts_integers_correctly(self):
        a = [1, 23, 5, 7, 88, 22, 1, 2, 3, 44]
        result = heap_sort(a)
        assert result == [1, 1, 2, 3, 5, 7, 22, 23, 44, 88]

    def test_sorts_floats_correctly(self):
        a = [3.5, 1.2, 4.7, 2.1]
        result = heap_sort(a)
        assert result == [1.2, 2.1, 3.5, 4.7]

    def test_sorts_array_with_duplicates(self):
        a = [3, 1, 3, 2, 1, 3]
        result = heap_sort(a)
        assert result == [1, 1, 2, 3, 3, 3]

    def test_handles_already_sorted_array(self):
        a = [1, 2, 3, 4, 5]
        result = heap_sort(a)
        assert result == [1, 2, 3, 4, 5]

    def test_handles_single_element(self):
        a = [5]
        result = heap_sort(a)
        assert result == [5]

    def test_raises_error_on_empty_array(self):
        with pytest.raises(EmptyError):
            heap_sort([])

    def test_raises_error_with_strings(self):
        with pytest.raises(NotStringError):
            heap_sort([1, 2, 'a', 3])
