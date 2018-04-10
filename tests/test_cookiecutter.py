import pytest


def f():
    raise KeyError('TODO')

def test_exception_is_raised():
    with pytest.raises(KeyError):
        f()

def func(x):
    return x + 1

def test_basic():
    assert func(3) == 4