from typing import NamedTuple


def test_property_and_setter():
    class Foo:
        def __init__(self):
            self.__x = 1

        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, value):
            self.__x = value

    foo = Foo()
    assert foo.x == 1
    foo.x = 2
    assert foo.x == 2


def test_property_duplicated_name():
    class Bar(NamedTuple):
        x: int

        @property
        def x(self):
            return self.x + 1


    bar = Bar(1)
    # This returns 1 instead of 2
    assert bar.x == 1
