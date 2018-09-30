import pandas as pd
import numpy as np


def assert_array_equal(arr1, arr2):
    if not np.array_equal(arr1, arr2):
        raise ValueError("{} is not {}".format(arr1, arr2))


def test_series_category():
    s = pd.Series(['A', 'B', 'C'], index=['A', 'B', 'C']).astype(
        'category', categories=['C', 'B', 'A'], ordered=True)

    assert len(s[s > 'B']) == 1


def test_series_dtype():
    assert str(pd.Series([1]).dtype) == 'int64'
    assert str(pd.Series([1, None]).dtype) == 'float64'
    assert str(pd.Series(['a', None]).dtype) == 'object'


def test_series_nan():
    nan = pd.Series([1, None])[1]
    assert str(nan) == 'nan'
    assert nan != np.nan
    assert np.isnan(nan)


def test_series_dictionary():
    numbers = {'one': 1, 'two': 2}
    s = pd.Series(numbers)
    assert_array_equal(s.index.values, ['one', 'two'])
    assert_array_equal(s.values, [1, 2])

    s = pd.Series([1, 2], index=['one', 'two'])
    assert_array_equal(s.index.values, ['one', 'two'])
    assert_array_equal(s.values, [1, 2])

    s = pd.Series(s, index=['one', 'three'])
    assert s[0] == 1
    assert s.index[0] == 'one'
    assert np.isnan(s[1])
    assert s.index[1] == 'three'


def test_series_name():
    s = pd.Series([1, 2], name='numbers')
    assert s.name == 'numbers'


def test_querying_series():
    numbers = {'one': 1, 'two': 2}
    s = pd.Series(numbers)

    assert s.iloc[1] == 2
    assert s.loc['one'] == 1

    # not recommended as labels can be number
    assert s[1] == 2
    assert s['one'] == 1

    # vectorized calculation is much faster
    assert np.sum(s) == 3

    s += 2
    assert np.sum(s) == 7

    # append doesn't change the original object
    new_s = s.append(pd.Series({'three': 3}))
    assert len(s) == 2
    assert len(new_s) == 3
