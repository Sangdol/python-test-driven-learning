import pytest
from enum import Enum, unique


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

    def describe(self):
        return self.name, self.value


def test_enum():
    assert str(Color.RED) == 'Color.RED'
    assert repr(Color.RED) == '<Color.RED: 1>'
    assert isinstance(Color.RED, Color)
    assert Color.RED.name == 'RED'
    assert Color.RED.value == 1
    assert [color.value for color in Color] == [1, 2, 3]

    assert Color(1) == Color.RED
    assert Color['RED'] == Color.RED


def test_enum_unique():
    try:
        @unique
        class Color(Enum):
            RED = 1
            GREEN = 1

        pytest.fail()
    except ValueError as e:
        pass


def test_enum_iteration():
    assert ([(name, member) for name, member in Color.__members__.items()] ==
            [('RED', Color.RED), ('GREEN', Color.GREEN), ('BLUE', Color.BLUE)])


def test_enum_function_api():
    Animal = Enum('Animal', 'ANT BEE')

    assert Animal.ANT.value == 1
    assert Animal.BEE.value == 2
