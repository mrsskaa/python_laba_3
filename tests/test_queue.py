import pytest
from src.errors import EmptyError
from src.queue_on_list import Queue


class TestQueue:
    def test_new_queue_is_empty(self):
        queue = Queue()
        assert queue.is_empty()
        assert len(queue) == 0

    def test_enqueue_adds_element(self):
        queue = Queue()
        queue.enqueue(1)
        assert not queue.is_empty()
        assert len(queue) == 1
        assert queue.front() == 1

    def test_enqueue_multiple_elements(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        assert len(queue) == 2
        assert queue.front() == 1

    def test_dequeue_removes_in_fifo_order(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        assert queue.dequeue() == 1
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3

    def test_dequeue_updates_size(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)

        queue.dequeue()
        assert len(queue) == 1

        queue.dequeue()
        assert len(queue) == 0
        assert queue.is_empty()

    def test_dequeue_on_empty_raises_error(self):
        queue = Queue()
        with pytest.raises(EmptyError):
            queue.dequeue()

    def test_front_peeks_first_element(self):
        queue = Queue()
        queue.enqueue(1)
        assert queue.front() == 1

        queue.enqueue(2)
        assert queue.front() == 1

    def test_front_on_empty_raises_error(self):
        queue = Queue()
        with pytest.raises(EmptyError):
            queue.front()

    def test_front_does_not_remove_element(self):
        queue = Queue()
        queue.enqueue(1)

        front_value = queue.front()
        assert front_value == 1
        assert len(queue) == 1
        assert not queue.is_empty()

    def test_len_returns_correct_size(self):
        queue = Queue()
        assert len(queue) == 0

        queue.enqueue(1)
        assert len(queue) == 1

        queue.enqueue(2)
        assert len(queue) == 2

        queue.dequeue()
        assert len(queue) == 1

    def test_is_empty_returns_correct_state(self):
        queue = Queue()
        assert queue.is_empty()

        queue.enqueue(1)
        assert not queue.is_empty()

        queue.dequeue()
        assert queue.is_empty()

    def test_handles_different_data_types(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2.5)
        queue.enqueue("string")
        queue.enqueue([1, 2, 3])

        assert queue.dequeue() == 1
        assert queue.dequeue() == 2.5
        assert queue.dequeue() == "string"
        assert queue.dequeue() == [1, 2, 3]

    def test_fifo_ordering_property(self):
        queue = Queue()

        queue.enqueue("first")
        queue.enqueue("second")
        queue.enqueue("third")

        assert queue.dequeue() == "first"
        assert queue.dequeue() == "second"
        assert queue.dequeue() == "third"

    def test_enqueue_dequeue_alternating(self):
        queue = Queue()

        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.dequeue() == 1

        queue.enqueue(3)
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3

    def test_queue_becomes_empty_after_all_dequeues(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)

        queue.dequeue()
        queue.dequeue()

        assert queue.is_empty()
        with pytest.raises(EmptyError):
            queue.front()
