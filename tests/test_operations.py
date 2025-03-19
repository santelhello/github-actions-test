from calculator.operations import add
from calculator.operations import subtract
from calculator.operations import multiply


def test_add():
    assert add(4, 5) == 9


def test_subtract():
    assert subtract(4, 5) == -1


def test_multiply():
    assert multiply(4, 5) == 20
