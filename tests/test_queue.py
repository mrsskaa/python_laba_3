import pytest
import importlib
from src.errors import EmptyError
queue_module = importlib.import_module('src.queue on list')
Queue = queue_module.Queue


def test_queue_init():
    queue = Queue()
    assert queue.is_empty()
    assert len(queue) == 0


def test_queue_enqueue():
    queue = Queue()
    queue.enqueue(1)
    assert not queue.is_empty()
    assert len(queue) == 1
    assert queue.front() == 1

    queue.enqueue(2)
    assert len(queue) == 2
    assert queue.front() == 1

    queue.enqueue("test")
    assert len(queue) == 3
    assert queue.front() == 1


def test_queue_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.dequeue() == 1
    assert len(queue) == 2
    assert queue.dequeue() == 2
    assert len(queue) == 1
    assert queue.dequeue() == 3
    assert len(queue) == 0
    assert queue.is_empty()

    with pytest.raises(EmptyError):
        queue.dequeue()


def test_queue_front():
    queue = Queue()
    queue.enqueue(1)
    assert queue.front() == 1
    assert len(queue) == 1

    queue.enqueue(2)
    assert queue.front() == 1
    assert len(queue) == 2

    with pytest.raises(EmptyError):
        empty_queue = Queue()
        empty_queue.front()


def test_queue_len():
    queue = Queue()
    assert len(queue) == 0

    queue.enqueue(1)
    assert len(queue) == 1

    queue.enqueue(2)
    assert len(queue) == 2

    queue.dequeue()
    assert len(queue) == 1

    queue.dequeue()
    assert len(queue) == 0


def test_queue_is_empty():
    queue = Queue()
    assert queue.is_empty()

    queue.enqueue(1)
    assert not queue.is_empty()

    queue.dequeue()
    assert queue.is_empty()


def test_queue_different_types():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2.5)
    queue.enqueue("string")

    assert queue.dequeue() == 1
    assert queue.dequeue() == 2.5
    assert queue.dequeue() == "string"


def test_queue_fifo_order():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.front() == 1
    assert queue.dequeue() == 1
    assert queue.front() == 2
    assert queue.dequeue() == 2
    assert queue.front() == 3
    assert queue.dequeue() == 3
