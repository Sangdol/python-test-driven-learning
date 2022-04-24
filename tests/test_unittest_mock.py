"""
https://docs.python.org/3/library/unittest.mock.html#module-unittest.mock
"""
from unittest.mock import MagicMock
from unittest.mock import Mock
from unittest.mock import patch

import pytest


def test_patch_object():
    class Person:
        def hi(self, target):
            return 'hi, {}'.format(target)

    with patch.object(Person, 'hi', return_value='hello') as mock_method:
        person = Person()
        assert person.hi('any') == 'hello'
        mock_method.assert_called_once_with('any')


def test_patch_function():
    with patch('builtins.print') as mock_print:
        mock_print.side_effect = lambda _: 'hello'
        assert print('hi') == 'hello'
        mock_print.assert_called_with('hi')

    # can't I mock str?
    with patch('builtins.str') as mock_str:
        mock_str.side_effect = lambda _: 'hello'
        try:
            assert str('hi') == 'hello'
            pytest.fail()
        except TypeError:
            pass


@patch('builtins.abs')
@patch('builtins.print')
def test_multiple_patch_decorator(mock_print, mock_abs):
    assert mock_print is print
    assert mock_abs is abs


class PatchTest:
    pass


@patch('test_unittest_mock.PatchTest')
def test_patch_decorator(patch_test_class):
    assert patch_test_class is PatchTest


def test_patch():
    class Clazz:
        def method(self, number):
            pass

    # Why do we need 'with'? to patch only in the scope
    # https://docs.python.org/3/library/unittest.mock.html#the-patchers
    with patch.object(Clazz, 'method', return_value=None) as mock_method:
        empty = Clazz()
        empty.method(1)

        mock_method.assert_called_once_with(1)


def test_mock_side_effect():
    """Mock is mock.

    https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
    """
    mock = Mock(side_effect=KeyError('foo'))

    try:
        mock()
        pytest.fail()
    except KeyError:
        pass

    mock = Mock(side_effect=lambda: 'hallo')
    assert mock() == 'hallo'

    mock = Mock(side_effect=lambda a: a)
    assert mock('hallo') == 'hallo'


def test_mock_methods():
    mock = Mock()
    mock.test.return_value = 'hello'
    assert mock.test() == 'hello'


def test_magic_mock():
    """MagicMock is a subclass of Mock with all the magic methods pre-created.

    https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock
    """
    class Empty:
        pass

    empty = Empty()
    empty.abc = MagicMock(return_value='abc')

    assert empty.abc('hi') == 'abc'
    empty.abc.assert_called_with('hi')
