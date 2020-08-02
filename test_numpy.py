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


def test_indexing():
    names = np.array(['a', 'b', 'a'])
    arr = np.array([
        [1],
        [2],
        [3]
    ])

    assert_array_equal(names == 'a', [True, False, True])
    assert_array_equal(arr[names == 'a'], [[1], [3]])
    assert_array_equal(arr[~(names == 'a')], [[2]])


def test_slicing():
    np_arr = np.arange(5)
    part = np_arr[0:2]
    part[0] = 100

    # slices are views on the original array
    assert np_arr[0] == 100

    # "bare" slice
    part[:] = 10
    assert_array_equal(np_arr, [10, 10, 2, 3, 4])


def test_full():
    tens = np.full((2, 3), 10)

    assert (tens == 10).all()
    assert tens.shape == (2, 3)


def test_clip():
    assert_array_equal(np.clip([-1, 0, 1, 2, 3], 0, 2), [0, 0, 1, 2, 2])


# horizontal (column wise) concatenation
def test_hstack():
    assert_array_equal(np.hstack(([1, 2, 3], [4, 5])), [1, 2, 3, 4, 5])
    assert_array_equal(np.hstack(([[1], [2]], [[3], [4]])), [[1, 3], [2, 4]])


def test_argmax():
    arr = np.array([1, 0, 3])

    assert np.argmax(arr) == 2


def test_argsort():
    # 0 is on the 1st index so 1 is the first element, etc.
    arr = np.array([1, 0, 3])
    sorted_indices = [1, 0, 2]

    assert_array_equal(np.argsort(arr), sorted_indices)
    assert_array_equal(arr[sorted_indices], [0, 1, 3])


def test_transpose():
    r = np.random.rand(2, 3)

    assert_array_equal(r.T, np.transpose(r))

    m = np.ones((2, 3, 4))
    assert np.transpose(m, axes=[1, 2, 0]).shape == (3, 4, 2)


def test_split():
    splited = np.split(np.arange(9), 3)

    assert len(splited) == 3
    assert_array_equal(splited[0], [0, 1, 2])

    try:
        splited = np.split(np.arange(8), 3)
        pytest.fail()
    except ValueError:
        # ValueError: array split does not result in an equal division
        pass


# Two dimensions are compatible when they are equal, or one of them is 1
# https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html
def test_broadcast():
    d5 = np.arange(5)
    d3 = np.arange(3)
    d13 = np.arange(3)[np.newaxis]
    d31 = np.arange(3)[:, np.newaxis]
    d33 = np.arange(9).reshape(3, 3)
    d511 = d5[:, np.newaxis, np.newaxis]

    assert (d511 * d3).shape == (5, 1, 3)
    assert (d511 * d33).shape == (5, 3, 3)
    assert (d13 + d3).shape == (1, 3)
    assert (d31 + d3).shape == (3, 3)
    assert (d31 * d3).shape == (3, 3)


# https://docs.scipy.org/doc/numpy/reference/constants.html#numpy.newaxis
def test_newaxis():
    assert np.newaxis is None

    x = np.arange(3)
    assert x.shape == (3,)
    assert x[:, np.newaxis].shape == (3, 1)
    assert x[:, np.newaxis].shape == x.reshape(3, -1).shape
    assert x[np.newaxis].shape == (1, 3)


def test_argmin_argmax():
    a = [[5, 4, 3], [10, 0, 5]]

    assert np.argmin(a) == 4
    assert_array_equal(np.argmin(a, axis=0), [0, 1, 0])
    assert_array_equal(np.argmin(a, axis=1), [2, 1])

    assert np.argmax(a) == 3


def test_amax():
    a = [[0, 1], [2, 3]]

    assert np.amax(a) == 3
    assert_array_equal(np.amax(a, axis=0), [2, 3])  # np.maximum() is faster
    assert_array_equal(np.amax(a, axis=1), [1, 3])

    a[0][0] = np.nan
    assert np.isnan(np.amax(a))
    assert np.nanmax(a) == 3

    b = [[-1], [2]]
    assert_array_equal(np.amax(b, axis=0), [2])
    assert_array_equal(np.amax(b, axis=1), [-1, 2])

    # -1: last dimension
    # https://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.stack.html
    assert_array_equal(np.amax(b, axis=-1), [-1, 2])

    assert np.amax([5], initial=6) == 6
    assert max([5], default=6) == 5


def test_bincount():
    assert_array_equal(np.bincount(np.arange(3)), [1, 1, 1])
    assert_array_equal(np.bincount(np.array([1, 3, 5, 1])), [0, 2, 0, 1, 0, 1])

    # weight
    assert_array_equal(np.bincount(np.array([1, 3, 5, 1]), [.1, .2, .3, .4]), [0, .5, 0, .2, 0, .3])

    try:
        np.bincount(np.arange(5, dtype=float))
        pytest.fail('dtype have to be int')
    except TypeError:
        pass


def test_append():
    """
    Why can't I np.array([]).append([])?
    - np.array() is for matrix. It's not a normal array.
    """
    assert_array_equal(np.append([1, 2], [3]), [1, 2, 3])
    assert_array_equal(np.append([1, 2], [[3], [4]]), [1, 2, 3, 4])
    assert_array_equal(np.append([[1, 2]], [[3, 4]], axis=0), [[1, 2], [3, 4]])
    assert_array_equal(np.append([[1, 2]], [[3, 4]], axis=1), [[1, 2, 3, 4]])


def test_mean():
    arr_1d = np.array([1, 2, 3])

    assert arr_1d.mean() == 2

    arr_2d = np.array([[1, 2], [3, 4]])

    assert arr_2d.mean() == 2.5
    assert_array_equal(arr_2d.mean(axis=1), [1.5, 3.5])
    assert_array_equal(arr_2d.mean(axis=0), [2, 3])


def test_linspace_logspace():
    assert_array_equal(np.linspace(1, 5, 3), [1, 3, 5])
    assert_array_equal(np.logspace(1, 3, 3), [10 ** 1, 10 ** 2, 10 ** 3])


def test_reshape():
    arr = np.array([1, 2, 3])

    assert_array_equal(arr.reshape(1, 3), [[1, 2, 3]])
    assert_array_equal(arr.reshape(1, -1), [[1, 2, 3]])
    assert_array_equal(arr.reshape(-1, 1), [[1], [2], [3]])

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

    try:
        any = np.r_[[[1]], 2, 3, [4, 5]]
        pytest.fail(any)
    except ValueError:
        # ValueError: all the input arrays must have same number of dimensions
        pass


# https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.c_.html
def test_c_():
    N = 3
    A = np.eye(N)

    assert_array_equal(np.c_[A, np.ones(N)], [[1., 0., 0., 1.],
                                              [0., 1., 0., 1.],
                                              [0., 0., 1., 1.]])

    assert_array_equal(np.c_[np.ones(N), A], [[1., 1., 0., 0.],
                                              [1., 0., 1., 0.],
                                              [1., 0., 0., 1.]])

    assert_array_equal(np.c_[A, A], [[1., 0., 0., 1., 0., 0.],
                                     [0., 1., 0., 0., 1., 0.],
                                     [0., 0., 1., 0., 0., 1.]])


def test_close_comparison():
    assert np.isclose(1.00000001, 1)
    assert np.allclose([1.00000001, 2.0000000001], [1, 2])


def test_shape():
    assert_array_equal(np.array([1, 2]).shape, (2,))
    assert_array_equal(np.array([[1, 2]]).shape, (1, 2))
    assert_array_equal(np.array([[1, 2, 3], [1, 2, 3]]).shape, (2, 3))


def test_array_comparison():
    assert_array_equal(np.array([1], dtype=object), [1])  # dtype matters
    assert_array_equal(np.array([1]), [1])
    assert_array_equal(np.array([1], dtype=int), [1])


# Cannot get 'day' from datetime64. Use pd.to_datetime('') instead
def test_date_comparison():
    assert np.datetime64('2018-01-01') < np.datetime64('2018-01-02')
    assert np.datetime64('2018-01-01') == np.datetime64('2018-01-01')


def test_astype():
    arr = np.arange(3)

    assert arr.dtype == np.int64
    assert arr is not arr.astype(np.int32)


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
