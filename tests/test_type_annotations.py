"""
Some code is from the book Robust Python.
"""
from dataclasses import dataclass
from typing import TypeVar, List, Optional, Union, Literal, Set, Tuple, Final, TypedDict
from decimal import Decimal


def test_method():
    def simple(i: int, j: int = 0) -> int:
        return i + j

    assert simple(1) == 1
    assert simple(10, 1) == 11

    def lst(i: int, j: int) -> List[int]:
        return [i, j]

    assert lst(1, 2) == [1, 2]


def test_type_var():
    T = TypeVar('T')

    # Generics - T has to be the same type.
    def half(l: List[T]) -> List[T]:
        return l[:len(l) // 2]

    assert half([1, 2]) == [1]


def test_optional():
    maybe_a_string: Optional[str] = 'abc'
    maybe_an_int: Optional[int] = None

    assert maybe_a_string == 'abc'
    assert maybe_an_int is None

    # This can return None thanks to Optional.
    def optional_str() -> Optional[str]:
        return None

    assert optional_str() is None


def test_union():
    def union(flag: bool) -> Union[str, int]:
        if flag:
            return '1'
        else:
            return 1

    assert union(True) == '1'


def test_literal():

    @dataclass
    class Error:
        error_code: Literal[1,2,3]

    @dataclass
    class Snack:
        name: Literal['Pretzel', 'Hotdog']
        condiments: Set[Literal['Mustard', 'Ketchup']]

    # 0 is not possible
    assert Error(1).error_code == 1

    # These are okay with mypy but not okay with IntelliJ type checker.
    assert Snack('Pretzel', set(['Mustard', 'Ketchup']))
    assert Snack('Pretzel', {'Mustard', 'Ketchup'})


def test_func():

    def tuple() -> Tuple[str, int]:
        return 'a', 1

    assert tuple() == ('a', 1)


def test_final():
    NAME: Final = 'Sang'

    assert NAME == 'Sang'


def test_typed_dict():
    class Person(TypedDict):
        name: str
        age: int

    assert Person(name='Sang', age=30) == {'name': 'Sang', 'age': 30}


def test_decimal_sum():
    def return_decimal() -> Decimal:
        # Need to wrap with Decimal again
        # since sum() returns Decimal | Literal[0]
        return Decimal(sum([Decimal(1), Decimal(2)]))

    assert return_decimal() == Decimal(3)

