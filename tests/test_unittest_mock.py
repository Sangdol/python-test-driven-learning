"""
https://docs.python.org/3/library/unittest.mock.html#module-unittest.mock
"""
from unittest.mock import MagicMock
from unittest.mock import Mock

import pytest


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
