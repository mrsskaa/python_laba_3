import pytest
from src.errors import EmptyError
from src.stack_on_list import Stack


class TestStack:
    def test_new_stack_is_empty(self):
        stack = Stack()
        assert stack.is_empty()
        assert len(stack) == 0

    def test_push_adds_element_to_top(self):
        stack = Stack()
        stack.push(1)
        assert not stack.is_empty()
        assert len(stack) == 1
        assert stack.peek() == 1

    def test_push_multiple_elements(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        assert len(stack) == 2
        assert stack.peek() == 2

    def test_pop_removes_from_top(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1

    def test_pop_updates_size(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)

        stack.pop()
        assert len(stack) == 1

        stack.pop()
        assert len(stack) == 0
        assert stack.is_empty()

    def test_pop_on_empty_raises_error(self):
        stack = Stack()
        with pytest.raises(EmptyError):
            stack.pop()

    def test_peek_returns_top_element(self):
        stack = Stack()
        stack.push(1)
        assert stack.peek() == 1

        stack.push(2)
        assert stack.peek() == 2

    def test_peek_on_empty_raises_error(self):
        stack = Stack()
        with pytest.raises(EmptyError):
            stack.peek()

    def test_peek_does_not_remove_element(self):
        stack = Stack()
        stack.push(1)

        top_value = stack.peek()
        assert top_value == 1
        assert len(stack) == 1
        assert not stack.is_empty()

    def test_len_returns_correct_size(self):
        stack = Stack()
        assert len(stack) == 0

        stack.push(1)
        assert len(stack) == 1

        stack.push(2)
        assert len(stack) == 2

        stack.pop()
        assert len(stack) == 1

    def test_is_empty_returns_correct_state(self):
        stack = Stack()
        assert stack.is_empty()

        stack.push(1)
        assert not stack.is_empty()

        stack.pop()
        assert stack.is_empty()

    def test_handles_different_data_types(self):
        stack = Stack()
        stack.push(1)
        stack.push(2.5)
        stack.push("string")
        stack.push([1, 2, 3])

        assert stack.pop() == [1, 2, 3]
        assert stack.pop() == "string"
        assert stack.pop() == 2.5
        assert stack.pop() == 1

    def test_lifo_ordering_property(self):
        stack = Stack()

        stack.push("first")
        stack.push("second")
        stack.push("third")

        assert stack.pop() == "third"
        assert stack.pop() == "second"
        assert stack.pop() == "first"

    def test_push_pop_alternating(self):
        stack = Stack()

        stack.push(1)
        stack.push(2)
        assert stack.pop() == 2

        stack.push(3)
        assert stack.pop() == 3
        assert stack.pop() == 1

    def test_stack_becomes_empty_after_all_pops(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)

        stack.pop()
        stack.pop()

        assert stack.is_empty()
        with pytest.raises(EmptyError):
            stack.peek()

    def test_peek_after_multiple_operations(self):
        stack = Stack()
        stack.push(10)
        assert stack.peek() == 10

        stack.push(20)
        assert stack.peek() == 20

        stack.pop()
        assert stack.peek() == 10
