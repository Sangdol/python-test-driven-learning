"""
https://docs.python.org/3/tutorial/classes.html
"""
import pytest

from dataclasses import dataclass


def test_class_attributes():
    class MyClass:
        i = 10

    m1 = MyClass()
    m2 = MyClass()

    assert MyClass.i == 10
    assert m1.i == 10
    assert m2.i == 10
    assert m1.__class__.i == 10

    MyClass.i = 20
    m3 = MyClass()

    assert MyClass.i == 20
    assert m3.i == 20

    # as 'i' is part of MyClass it's changed.
    assert m1.i == 20
    assert 'i' not in m1.__dict__

    # not 'i' is an attribute of m1
    m1.i = 10
    assert 'i' in m1.__dict__
    assert m1.i == 10

    MyClass.i = 30
    assert m1.i == 10


# https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner
def test_staticmethod_and_classmethod():
    class Person:
        def __init__(self, age, name):
            self.age = age
            self.name = name

        @classmethod
        def baby(cls, name):
            return cls(0, name)

        @staticmethod
        def adult(name):
            return Person(20, name)

        def info(self):
            return f'{self.age}, {self.name}'

    baby = Person.baby('Miyu')
    adult = Person.adult('Sang')

    assert isinstance(baby, Person)
    assert isinstance(adult, Person)
    assert baby.info() == '0, Miyu'

    class Engineer(Person):
        def info(self):
            return f'Engineer: {self.age}, {self.name}'

    engineer_baby = Engineer.baby('Miyu')
    engineer_adult = Engineer.adult('Sang')

    assert engineer_baby.info() == 'Engineer: 0, Miyu'
    # This would be undesirable so @classmethod should have been used.
    assert engineer_adult.info() == '20, Sang'


# https://docs.python.org/3/library/dataclasses.html
def test_dataclass():
    @dataclass
    class Person:
        name: str
        age: int
        alive: bool = True

        def hello(self) -> str:
            return 'Hello ' + self.name

    p = Person('Sang', 36)
    assert p.name == 'Sang'
    assert p.age == 36
    assert p.alive
    assert (
        p.__repr__()
        == "test_dataclass.<locals>.Person(name='Sang', age=36, alive=True)"
    )
    assert (
        p.__str__() == "test_dataclass.<locals>.Person(name='Sang', age=36, alive=True)"
    )
    assert p.hello() == 'Hello Sang'


def test_empty_class():
    class Employee:
        pass

    john = Employee()

    john.name = 'john'
    john.dept = 'computer lab'
    john.salary = 1

    assert john.name == 'john'
    assert john.__dict__ == {'dept': 'computer lab', 'name': 'john', 'salary': 1}


def test_self():
    class Person:
        age = 10

        def hi(self):
            return self

    p = Person()
    assert type(p.hi()).__module__ == 'tests.test_class'
    assert type(p.hi()).__name__ == 'Person'
    assert p.__class__.__module__ == 'tests.test_class'
    assert p.__class__.__name__ == 'Person'
    assert p.hi().__class__.__name__ == 'Person'
    assert p.hi().__module__ == 'tests.test_class'


def test_instance_variables():
    class WrongPerson:
        assets = []

        def add_asset(self, asset):
            self.assets.append(asset)

    a = WrongPerson()
    a.add_asset('phone')
    b = WrongPerson()
    b.add_asset('wallet')

    a.assets.append('wtf')

    assert a.assets == ['phone', 'wallet', 'wtf']
    assert b.assets == ['phone', 'wallet', 'wtf']

    class Person:
        def __init__(self):
            self.assets = []

        def add_asset(self, asset):
            self.assets.append(asset)

    a = Person()
    a.add_asset('phone')
    b = Person()
    b.add_asset('wallet')

    a.assets.append('better')

    assert a.assets == ['phone', 'better']
    assert b.assets == ['wallet']


def test_constructor_init():
    class Init:
        def __init__(self):
            self.data = [1]

    i = Init()
    assert i.data == [1]

    class Init2:
        def __init__(self, number):
            self.data = [number]

    i = Init2(2)
    assert i.data == [2]


def test_simple_class():
    class MyClass:
        """A simple class"""

        i = 123

        def f(self):
            return 'hello class'

    c = MyClass()
    assert c.i == 123
    assert c.__doc__ == 'A simple class'
    assert c.f() == 'hello class'


def test_init_subclass():
    """
    https://docs.python.org/3/reference/datamodel.html#object.__init_subclass__
    """

    class Animal:
        left_finger_count = None
        right_finger_count = None

        def __init_subclass__(cls):
            if cls.left_finger_count != cls.right_finger_count:
                raise ValueError()

    # We can throw an exception when a subclass is defined using __init_subclass__.
    with pytest.raises(ValueError):

        class Dog(Animal):
            left_finger_count = 1
            right_finger_count = 2
