"""Dunder/Magic Methods tests

https://docs.python.org/3/reference/datamodel.html#customization
"""


def test_str_to_string():
    class Test:
        def __str__(self):
            return "Test"

    assert str(Test()) == "Test"
