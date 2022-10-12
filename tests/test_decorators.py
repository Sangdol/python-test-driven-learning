from typing import NamedTuple

import functools


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


# https://book.pythontips.com/en/latest/decorators.html#writing-your-first-decorator
def test_naive_decorator():
    def naive_decorator(f):

        def wrapper(n):
            return f(n * 2)

        return wrapper

    @naive_decorator
    def pass_number(n):
        return n

    assert pass_number(1) == 2
    assert pass_number.__name__ == 'wrapper'

    
def test_wraps_decorator():
    def nice_decorator(f):
        @functools.wraps(f)
        def wrapper(n):
            return f(n * 2)

        return wrapper

    @nice_decorator
    def pass_number(n):
        return n 

    assert pass_number(1) == 2
    assert pass_number.__name__ == 'pass_number'
