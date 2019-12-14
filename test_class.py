"""
https://docs.python.org/3/tutorial/classes.html
"""

from dataclasses import dataclass


# https://docs.python.org/3/library/dataclasses.html
def test_dataclass():
    @dataclass
    class Person:
        name: str
        age: int
        alive: bool = True

        def hello(self) -> str:
            return 'world'

    p = Person('Sang', 36)
    assert p.name == 'Sang'
    assert p.age == 36
    assert p.alive
    assert p.__repr__() == "test_dataclass.<locals>.Person(name='Sang', age=36, alive=True)"
    assert p.__str__() == "test_dataclass.<locals>.Person(name='Sang', age=36, alive=True)"
    assert p.hello() == 'world'


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
    assert type(p.hi()).__module__ == 'test_class'
    assert type(p.hi()).__name__ == 'Person'
    assert p.__class__.__module__ == 'test_class'
    assert p.__class__.__name__ == 'Person'
    assert p.hi().__class__.__name__ == 'Person'
    assert p.hi().__module__ == 'test_class'


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
