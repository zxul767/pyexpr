import pytest

from src.expression import Variable


@pytest.fixture
def x():
    return Variable("x")


@pytest.fixture
def y():
    return Variable("y")
