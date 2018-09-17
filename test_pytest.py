import numpy as np
from numpy.testing import assert_array_equal


def test_simple():
    assert 3 == 3


def test_assert_array_equal():
    assert_array_equal(np.arange(0, 3), np.array([0, 1, 2]))
