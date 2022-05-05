import sys

from unittest.mock import Mock
from unittest.mock import patch

import stub.package_test_math as test_math


def test_patch_object():
    class Person:
        def hi(self, target):
            return "hi, {}".format(target)

    with patch.object(Person, "hi", return_value="hello") as mock_method:
        person = Person()
        assert person.hi("any") == "hello"
        mock_method.assert_called_once_with("any")


def test_patch_function():
    with patch("builtins.print") as mock_print:
        mock_print.side_effect = lambda _: "hello"
        assert print("hi") == "hello"
        mock_print.assert_called_with("hi")

    # can't I mock str?
    with patch("builtins.str") as mock_str:
        mock_str.side_effect = lambda _: "hello"
        try:
            assert str("hi") == "hello"
            pytest.fail()
        except TypeError:
            pass


# Bottom-up order
# https://docs.python.org/3/library/unittest.mock.html#quick-guide
@patch("builtins.abs")
@patch("builtins.print")
def test_multiple_patch_decorator(mock_print, mock_abs):
    assert mock_print is print
    assert mock_abs is abs


def test_patch():
    class Clazz:
        def method(self, number):
            pass

    # Why do we need 'with'? to patch only in the scope
    # https://docs.python.org/3/library/unittest.mock.html#the-patchers
    with patch.object(Clazz, "method", return_value=None) as mock_method:
        empty = Clazz()
        empty.method(1)

        mock_method.assert_called_once_with(1)


@patch("stub.package_test_math.package_test_subtract")
def test_mocked_subtract(mocked_subtract):
    mocked_subtract.subtract.return_value = 5
    assert test_math.subtract(2, 3) == 5
