"""
https://docs.python.org/3/library/unittest.mock.html#module-unittest.mock
"""
from unittest.mock import MagicMock
from unittest.mock import Mock
from unittest.mock import patch
import pytest


class PatchTest:
    pass


@patch('test_mock.PatchTest')
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


def test_mock():
    mock = Mock(side_effect=KeyError('foo'))

    try:
        mock()
        pytest.fail()
    except KeyError:
        pass


def test_magic_mock():
    class Empty:
        pass

    empty = Empty()
    empty.abc = MagicMock(return_value='abc')

    assert empty.abc('hi') == 'abc'
    empty.abc.assert_called_with('hi')
