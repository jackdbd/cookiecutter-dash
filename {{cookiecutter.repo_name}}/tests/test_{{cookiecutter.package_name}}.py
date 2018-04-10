import pytest
from {{cookiecutter.package_name}}.exceptions import ImproperlyConfigured


def f():
    raise ImproperlyConfigured('TODO')

def test_exception_is_raised():
    with pytest.raises(ImproperlyConfigured):
        f()

def func(x):
    return x + 1

def test_basic():
    assert func(3) == 4