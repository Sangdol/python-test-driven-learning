"""Dunder/Magic Methods tests
"""


def test_str_to_string():
    class Test:
        def __str__(self):
            return "Test"

    assert str(Test()) == "Test"
