"""
Documentation for namedtuple
https://docs.python.org/3/library/collections.html#collections.namedtuple

Documentation for typing.NamedTuple
https://docs.python.org/3/library/typing.html#typing.NamedTuple
"""
from collections import namedtuple
from typing import NamedTuple


def test_named_tuple():
    Point = namedtuple('Point', ['x', 'y'])
    p1 = Point(1, 2)
    assert p1.x == 1
    assert p1.y == 2


def test_unpacking():
    Point = namedtuple('Point', ['x', 'y'])
    p1 = Point(1, 2)
    x, y = p1
    assert x == 1
    assert y == 2

    x, z = p1
    assert x == 1
    assert z == 2


def test_typed_named_tuples():
    # 1
    class Employee(NamedTuple):
        name: str
        age: int

    e1 = Employee(name='Bob', age=40)
    assert e1.name == 'Bob'
    assert e1.age == 40

    # 2
    Employee = NamedTuple('Employee', [('name', str), ('age', int)])

    e2 = Employee(name='Alice', age=30)
    assert e2.name == 'Alice'
    assert e2.age == 30

    # 3 (without typing)
    Employee = namedtuple('Employee', 'name age')

    e3 = Employee(name='Charlie', age=25)
    assert e3.name == 'Charlie'
    assert e3.age == 25

    # 4 (without typing)
    Employee = namedtuple('Employee', ['name', 'age'])

    e4 = Employee(name='David', age=27)
    assert e4.name == 'David'
    assert e4.age == 27


def test_typed_named_tuple_methods():
    # 1
    class Employee(NamedTuple):
        name: str
        age: int

        @property
        def next_year_age(self):
            return self.age + 1

    e1 = Employee(name='Bob', age=40)
    assert e1.next_year_age == 41

