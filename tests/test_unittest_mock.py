"""
https://docs.python.org/3/library/unittest.mock.html#module-unittest.mock
"""
from unittest.mock import MagicMock
from unittest.mock import Mock, call, patch, create_autospec

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


def test_mock_method_return_value():
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
    empty.abc = MagicMock(return_value="abc")  # type: ignore

    assert empty.abc("hi") == "abc"  # type: ignore
    empty.abc.assert_called_with("hi")  # type: ignore


def test_mock_methods():
    mock = Mock()

    def abc(a):
        return a

    mock.abc = abc

    assert mock.abc(1) == 1

    with pytest.raises(AttributeError):
        # No assert_called_with in abc()
        mock.abc.assert_called_with(1)


class MyClass:
    attr = 10

    def __init__(self):
        self.init_attribute = 1

    def abc(self):
        return 'abc'


def test_spec_autospec():
    #
    # Rationale: mock can ignore typos and changes of APIs of the code under test.
    #
    mock = Mock(name='A', return_value=None)
    mock.assetrrr_with_typo(1)  # This doesn't break the test.

    with pytest.raises(AttributeError):
        # The typo starts with `assert_` throws an error though.
        mock.assert_with_typo(1)

    #
    # spec
    #
    mock = Mock(spec=MyClass)

    # Fixes the issue of ignoring typos
    with pytest.raises(AttributeError):
        mock.assetr_with_typo()

    # But the issue still remains for the methods
    mock.abc.assetrrr_with_typo()

    #
    # autospec
    #
    print('global', globals())
    patcher = patch('tests.test_unittest_mock.MyClass', autospec=True)
    mock = patcher.start()
    with pytest.raises(AttributeError):
        mock.abc.assetrrr_with_typo()

    # But autospec doesn't know about the attributes
    # that are created in __init__()
    with pytest.raises(AttributeError):
        mock.init_attribute


def test_create_autospec():
    # This is a simpler version of patcher(..., autospec=True)
    mock = create_autospec(MyClass)
    with pytest.raises(AttributeError):
        mock.abc.assetrrr_with_typo()
