import pytest
import importlib
from src.errors import EmptyError
steck_module = importlib.import_module('src.steck on list')
Stack = steck_module.Stack


def test_stack_init():
    stack = Stack()
    assert stack.is_empty()
    assert len(stack) == 0


def test_stack_push():
    stack = Stack()
    stack.push(1)
    assert not stack.is_empty()
    assert len(stack) == 1
    assert stack.peek() == 1

    stack.push(2)
    assert len(stack) == 2
    assert stack.peek() == 2

    stack.push("test")
    assert len(stack) == 3
    assert stack.peek() == "test"


def test_stack_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.pop() == 3
    assert len(stack) == 2
    assert stack.pop() == 2
    assert len(stack) == 1
    assert stack.pop() == 1
    assert len(stack) == 0
    assert stack.is_empty()

    with pytest.raises(EmptyError):
        stack.pop()


def test_stack_peek():
    stack = Stack()
    stack.push(1)
    assert stack.peek() == 1
    assert len(stack) == 1

    stack.push(2)
    assert stack.peek() == 2
    assert len(stack) == 2

    with pytest.raises(EmptyError):
        empty_stack = Stack()
        empty_stack.peek()


def test_stack_len():
    stack = Stack()
    assert len(stack) == 0

    stack.push(1)
    assert len(stack) == 1

    stack.push(2)
    assert len(stack) == 2

    stack.pop()
    assert len(stack) == 1

    stack.pop()
    assert len(stack) == 0


def test_stack_is_empty():
    stack = Stack()
    assert stack.is_empty()

    stack.push(1)
    assert not stack.is_empty()

    stack.pop()
    assert stack.is_empty()


def test_stack_different_types():
    stack = Stack()
    stack.push(1)
    stack.push(2.5)
    stack.push("string")

    assert stack.pop() == "string"
    assert stack.pop() == 2.5
    assert stack.pop() == 1
