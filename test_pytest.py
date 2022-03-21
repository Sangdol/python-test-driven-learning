import numpy as np
import pytest
from numpy.testing import assert_array_equal


# setup / teardown
# https://docs.pytest.org/en/latest/xunit_setup.html
def setup_module():  # class / method / function
    pass


def teardown_module():  # class / method / function
    pass


def test_simple():
    assert 3 == 3


def test_assert_array_equal():
    assert_array_equal(np.arange(0, 3), np.array([0, 1, 2]))


# https://docs.pytest.org/en/latest/skipping.html
@pytest.mark.skip(reason="No need to test.")
def test_skip():
    pass


# https://docs.pytest.org/en/6.2.x/parametrize.html
@pytest.mark.parametrize("test_input, expected",
                         [([], [])])
def test(test_input, expected):
    assert test_input == expected


# https://stackoverflow.com/questions/23337471/how-to-properly-assert-that-an-exception-gets-raised-in-pytest
def test_fails():
    with pytest.raises(Exception):
        _ = 1 / 0


@pytest.mark.xfail(raises=ZeroDivisionError)
def test_fails_with_annotation():
    _ = 1 / 0

