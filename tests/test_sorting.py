import pytest
from src.sorting import bubble_sort, quick_sort, bucket_sort, radix_sort, counting_sort, heap_sort
from src.errors import BucketError, EmptyError, BadTypeError, NotStringError, DigitisNotNaturalNumberError


def test_bubble_sort():
    assert bubble_sort([1, 23, 5, 7, 88, 22, 1, 2, 3, 44]) == [1, 1, 2, 3, 5, 7, 22, 23, 44, 88]
    assert bubble_sort([3.5, 1.2, 4.7, 2.1]) == [1.2, 2.1, 3.5, 4.7]
    assert bubble_sort(['d', 'q', 'f', 'a', 'y']) == ['a', 'd', 'f', 'q', 'y']
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert bubble_sort([5]) == [5]

    with pytest.raises(EmptyError):
        bubble_sort([])

    with pytest.raises(BadTypeError):
        bubble_sort([1, 2, 'a', 3])


def test_quick_sort():
    assert quick_sort([1, 23, 5, 7, 88, 22, 1, 2, 3, 44], 0, 9) == [1, 1, 2, 3, 5, 7, 22, 23, 44, 88]
    assert quick_sort([3.5, 1.2, 4.7, 2.1], 0, 3) == [1.2, 2.1, 3.5, 4.7]
    assert quick_sort(['d', 'q', 'f', 'a', 'y'], 0, 4) == ['a', 'd', 'f', 'q', 'y']
    assert quick_sort([1, 2, 3, 4, 5], 0, 4) == [1, 2, 3, 4, 5]
    assert quick_sort([5], 0, 0) == [5]

    with pytest.raises(EmptyError):
        quick_sort([], 0, 0)

    with pytest.raises(BadTypeError):
        quick_sort([1, 2, 'a', 3], 0, 3)


def test_counting_sort():
    assert counting_sort([1, 23, 5, 7, 88, 22, 1, 2, 3, 44]) == [1, 1, 2, 3, 5, 7, 22, 23, 44, 88]
    assert counting_sort([3.5, 1.2, 4.7, 2.1]) == [1.2, 2.1, 3.5, 4.7]
    assert counting_sort([3, 1, 3, 2, 1, 3]) == [1, 1, 2, 3, 3, 3]

    with pytest.raises(EmptyError):
        counting_sort([])

    with pytest.raises(NotStringError):
        counting_sort([1, 2, 'a', 3])


def test_radix_sort():
    assert radix_sort([170, 45, 75, 90, 2, 802, 24, 66]) == [2, 24, 45, 66, 75, 90, 170, 802]
    assert radix_sort([170, 45, 75, 90, 2], 10) == [2, 45, 75, 90, 170]
    assert radix_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    with pytest.raises(EmptyError):
        radix_sort([])

    with pytest.raises(DigitisNotNaturalNumberError):
        radix_sort([1, 2, 'a', 3])
        radix_sort([3.5, 1.2, 4.7, 2.1])
        radix_sort([1, 2, 3, -1])


def test_bucket_sort():
    assert bucket_sort([0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]) == [0.32, 0.33, 0.37, 0.42, 0.47, 0.51, 0.52]
    assert bucket_sort([0.42, 0.32, 0.33, 0.52, 0.37], 5) == [0.32, 0.33, 0.37, 0.42, 0.52]
    assert bucket_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
    assert bucket_sort([5, 5, 5, 5]) == [5, 5, 5, 5]

    with pytest.raises(EmptyError):
        bucket_sort([])

    with pytest.raises(NotStringError):
        bucket_sort([1, 2, 'a', 3])

    with pytest.raises(BucketError):
        bucket_sort([0.5, 0.3, 0.7], 0)

    with pytest.raises(BucketError):
        bucket_sort([0.5, 0.3, 0.7], -1)


def test_heap_sort():
    assert heap_sort([1, 23, 5, 7, 88, 22, 1, 2, 3, 44]) == [1, 1, 2, 3, 5, 7, 22, 23, 44, 88]
    assert heap_sort([3.5, 1.2, 4.7, 2.1]) == [1.2, 2.1, 3.5, 4.7]
    assert heap_sort([3, 1, 3, 2, 1, 3]) == [1, 1, 2, 3, 3, 3]
    assert heap_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert heap_sort([5]) == [5]

    with pytest.raises(EmptyError):
        heap_sort([])

    with pytest.raises(NotStringError):
        heap_sort([1, 2, 'a', 3])
