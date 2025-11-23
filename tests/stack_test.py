from src.stack import Stack
import pytest


def test_base_stack_work():
    stack = Stack()
    for i in range(100):
        stack.push(i)
    for i in range(100):
        assert 100 - 1 - i == stack.pop()


def test_stack_min():
    stack = Stack()
    for i in range(100):
        stack.push(i)
    assert stack.min() == 0
    stack.push(-10)
    assert stack.min() == -10
    stack.pop()
    assert stack.min() == 0


def test_stack_peek():
    stack = Stack()
    for i in range(100):
        stack.push(i)
        assert stack.peek() == i


def test_stack_len_and_empty():
    stack = Stack()
    assert stack.is_empty()
    for i in range(100):
        stack.push(i)
    assert len(stack) == 100
    stack.pop()
    assert len(stack) == 99


def test_stack_errors():
    stack = Stack()
    with pytest.raises(IndexError):
        stack.min()
    with pytest.raises(IndexError):
        stack.pop()
    with pytest.raises(IndexError):
        stack.peek()
    with pytest.raises(ValueError):
        stack.push(10/6)
