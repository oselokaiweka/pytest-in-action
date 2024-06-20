import pytest

from src.smath import subtract, add

#Implementing setup and teardown without fixtures. 
def setup_function(function):
    print(f" Running setup: {function.__name__}")
    function.x = 10


def teardown_function(function):
    print(f" Running teardown: {function.__name__}")
    del function.x


def test_smath_subtract():
    assert subtract(test_smath_subtract.x) == 9


#Implementing setup and teardown with fixtures. 
@pytest.fixture
def setup_teardown():
    print("Running setup")
    x = 10
    yield x # Yielding x allows it to be used in the test function
    print("Running teardown")


def test_smath_add(setup_teardown):
    assert add(setup_teardown) == 11