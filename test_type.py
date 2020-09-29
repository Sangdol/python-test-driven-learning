from typing import TypeVar, List


def test_type_var():
    X = TypeVar('X')

    def generic(l: List[X]) -> List[X]:
        return l[:len(l) // 2]

