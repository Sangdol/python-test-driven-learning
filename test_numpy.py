import numpy as np
import pandas as pd
import collections
import pytest


def assert_array_equal(arr1, arr2):
    if not np.array_equal(arr1, arr2):
        raise ValueError("{} is not {}".format(arr1, arr2))


def assert_array_not_equal(arr1, arr2):
    if np.array_equal(arr1, arr2):
        raise ValueError("{} is {}".format(arr1, arr2))


def test_reshape():
    arr = np.array([1, 2, 3])

    assert_array_equal(arr.reshape(1, 3), [[1, 2, 3]])
    assert_array_equal(arr.reshape(1, -1), [[1, 2, 3]])

    arr = np.array([1, 2, 3, 4, 5, 6])
    assert_array_equal(arr.reshape(2, 3), [[1, 2, 3], [4, 5, 6]])
    assert_array_equal(arr.reshape(2, -1), [[1, 2, 3], [4, 5, 6]])


# Data Type Objects - https://docs.scipy.org/doc/numpy-1.10.1/reference/arrays.dtypes.html
# The Array Interface - https://docs.scipy.org/doc/numpy-1.10.1/reference/arrays.interface.html#arrays-interface
def test_dtypes():
    dt = np.dtype('>i4')

    assert dt.byteorder == '>'
    assert dt.itemsize == 4
    assert dt.name == 'int32'
    assert dt.type is np.int32
    assert dt.str == '>i4'


# https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.r_.html
def test_r_():
    assert_array_equal(np.array([1, 2, 3, 4, 5]), np.r_[[1], 2, 3, [4, 5]])


# https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.c_.html
def test_c_():
    N = 3
    A = np.eye(N)

    assert_array_equal(np.c_[A, np.ones(N)], [[1., 0., 0., 1.],
                                              [0., 1., 0., 1.],
                                              [0., 0., 1., 1.]])


def test_close_comparison():
    assert np.isclose(1.00000001, 1)
    assert np.allclose([1.00000001, 2.0000000001], [1, 2])


def test_shape():
    assert_array_equal(np.array([1, 2]).shape, (2,))
    assert_array_equal(np.array([[1, 2]]).shape, (1, 2))
    assert_array_equal(np.array([[1, 2, 3], [1, 2, 3]]).shape, (2, 3))


def test_array_comparison():
    assert_array_not_equal(np.array(1, dtype=object), [1])  # dtype matters
    assert_array_equal(np.array([1]), [1])
    assert_array_equal(np.array([1], dtype=int), [1])


# Cannot get 'day' from datetime64. Use pd.to_datetime('') instead
def test_date_comparison():
    assert np.datetime64('2018-01-01') < np.datetime64('2018-01-02')
    assert np.datetime64('2018-01-01') == np.datetime64('2018-01-01')


# https://stackoverflow.com/questions/41550746/error-using-astype-when-nan-exists-in-a-dataframe
def test_nan_type():
    assert type(np.nan).__name__ == 'float'

    arr = np.array([np.nan, 0])

    assert str(arr.dtype) == 'float64'
    assert_array_equal(arr.astype(int), [-9223372036854775808, 0])  # ??

    try:
        """
        cannot cast to int as nan is float
        """
        pd.Series(arr).astype(int)
        pytest.fail()
    except ValueError:
        pass


# https://stackoverflow.com/questions/36000993/numpy-isnan-fails-on-an-array-of-floats-from-pandas-dataframe-apply
def test_isnan_type_error():
    arr = np.array([np.nan, 0], dtype=object)
    try:
        """
        np.isnan can be applied to NumPy arrays of native dtype (such as np.float64):
        """
        np.isnan(arr)
        pytest.fail()
    except TypeError:
        assert_array_equal(pd.isnull(arr), [True, False])


def test_argwhere():
    arr = np.array([0, 0, np.nan, 1, 1, 1])

    assert_array_equal(np.argwhere(arr == 0), [[0], [1]])
    assert_array_equal(np.argwhere(np.isnan(arr)), [[2]])


# https://stackoverflow.com/questions/28663856/how-to-count-the-occurrence-of-certain-item-in-an-ndarray-in-python
def test_counting():
    y = np.array([0, 0, 1, 1, 1])
    assert np.sum(y) == 3
    assert np.count_nonzero(y) == 3
    assert collections.Counter(y) == {0: 2, 1: 3}
    assert len(y[y == 1]) == 3
    assert (y == 1).sum() == 3
    assert list(y).count(1) == 3


# For conditional (ternary) operation
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.where.html
def test_where():
    x = np.array([1, 2, 3])
    assert_array_equal(np.where(x >= 2, x, 0), [0, 2, 3])


def test_transpose():
    assert_array_equal(np.transpose([1, 2]), [1, 2])
    assert_array_equal(np.transpose([[1, 2]]), [[1], [2]])


# https://docs.scipy.org/doc/numpy/reference/generated/numpy.arange.html
def test_arange():
    assert_array_equal(np.arange(3), [0, 1, 2])

    # start, stop, step
    assert_array_equal(np.arange(10, 16, 2), [10, 12, 14])

    # https://stackoverflow.com/questions/10580676/comparing-two-numpy-arrays-for-equality-element-wise
    assert_array_equal(np.arange(3, 5) == [3, 4], [True, True])
    assert (np.arange(3, 5) == [3, 4]).all()
