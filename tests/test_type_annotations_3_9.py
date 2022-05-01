"""
https://docs.python.org/3/library/typing.html
"""
from typing import Any


def test_dict_type():
    d: dict[str, int] = {}

    d['a'] = 1

    assert d['a'] == 1


def test_nested_dict_type():
    d: dict[str, dict[str, Any]] = {}

    d['a'] = {}
    d['a']['b'] = 1

    assert d['a']['b'] == 1
