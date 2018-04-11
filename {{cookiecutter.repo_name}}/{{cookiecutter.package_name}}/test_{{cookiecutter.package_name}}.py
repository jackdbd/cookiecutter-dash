import pytest
import dash_html_components as html
from app import app
from exceptions import ImproperlyConfigured


def f():
    raise ImproperlyConfigured('TODO')

def test_exception_is_raised():
    with pytest.raises(ImproperlyConfigured):
        f()

def test_debug_is_disabled():
    assert app.server.debug == False

def test_layout_is_a_function_that_returns_a_div_element():
    assert isinstance(app.layout(), html.Div)
