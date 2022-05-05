"""
https://docs.python.org/3/library/unittest.mock.html#module-unittest.mock
"""
from unittest.mock import MagicMock
from unittest.mock import Mock, call

import pytest


def test_mock_side_effect():
    """Mock is mock.

    https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
    """
    mock = Mock(side_effect=KeyError("foo"))

    try:
        mock()
        pytest.fail()
    except KeyError:
        pass

    mock = Mock(side_effect=lambda: "hallo")
    assert mock() == "hallo"

    mock = Mock(side_effect=lambda a: a)
    assert mock("hallo") == "hallo"


def test_mock_methods():
    mock = Mock()
    mock.test.return_value = "hello"
    assert mock.test() == "hello"


def test_mock_assert_called():
    """
    https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called
    """
    mock = Mock()
    mock.method()
    mock.method.assert_called()
    mock.method.assert_called_once()

    mock = Mock()
    mock.method(1, 2, 3, test="test")
    mock.method.assert_called_with(1, 2, 3, test="test")
    mock.method.assert_called_once_with(1, 2, 3, test="test")

    mock = Mock()
    mock.method(1, 2, 3, test="test")
    mock.method(100)
    mock.method.assert_any_call(1, 2, 3, test="test")
    mock.method.assert_any_call(100)

    mock = Mock()
    mock(1)
    mock(2)
    mock.assert_has_calls([call(1), call(2)])


def test_magic_mock():
    """MagicMock is a subclass of Mock with all the magic methods pre-created.

    https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock
    """

    class Empty:
        pass

    empty = Empty()
    empty.abc = MagicMock(return_value="abc")

    assert empty.abc("hi") == "abc"
    empty.abc.assert_called_with("hi")
