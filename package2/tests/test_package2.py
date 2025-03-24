from src.package2 import multiply
from src.package2 import divide


def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(2, 3) == 6
