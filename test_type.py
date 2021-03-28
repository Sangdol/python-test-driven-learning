"""
Some code is from the book Robust Python.
"""
from dataclasses import dataclass
from typing import TypeVar, List, Optional, Union, Literal, Set, Tuple


def test_type_var():
    X = TypeVar('X')

    # TODO add more explanation
    def generic(l: List[X]) -> List[X]:
        return l[:len(l) // 2]


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