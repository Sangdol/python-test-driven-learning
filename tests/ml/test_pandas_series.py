import pandas as pd
import numpy as np


def assert_array_equal(arr1, arr2):
    if not np.array_equal(arr1, arr2):
        raise ValueError("{} is not {}".format(arr1, arr2))


def test_isin():
    s = pd.Series([1, 2, 2, 3, 3, 3])

    assert_array_equal(s[s.isin([1, 2])].values, [1, 2, 2])
    assert_array_equal(s[~s.isin([1, 2])].values, [3, 3, 3])


def test_replace():
    s = pd.Series(['abc'])

    # str replace
    assert s.str.replace('b', 'a')[0] == 'aac'

    # regex is True by default
    assert s.str.replace(r'\w+', 'a')[0] == 'a'

    # replace
    assert s.replace('abc', 'aaa')[0] == 'aaa'

    # it only replaces when the given value matches exactly
    # when no regex=True is passed.
    assert s.replace('a', 'b')[0] == 'abc'

    # it can replace types other than str
    assert pd.Series([0]).replace(0, 1)[0] == 1


def test_logical_not():
    assert_array_equal(-pd.Series([True, False]), [False, True])
    assert_array_equal(~pd.Series([True, False]), [False, True])


def test_groupby_multi_keys():
    s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8])
    k1 = pd.Series(['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b'])
    k2 = pd.Series(['c', 'c', 'd', 'd', 'e', 'e', 'f', 'f'])

    # a  c    1.5
    #    d    3.5
    # b  e    5.5
    #    f    7.5
    # dtype: float64
    assert_array_equal(s.groupby([k1, k2]).mean(), [1.5, 3.5, 5.5, 7.5])


def test_groupby():
    s = pd.Series(['a', 'b', 'b'])

    # self groupby
    assert s.groupby(s).agg('count').equals(
        pd.Series(data=[1, 2], index=['a', 'b']))
    # count - excluding missing values
    assert s.groupby(s).count().equals(
        pd.Series(data=[1, 2], index=['a', 'b']))
    assert s.groupby(s).size().equals(pd.Series(data=[1, 2], index=['a', 'b']))

    # groupby by other series
    s = pd.Series([1, 1, 2])
    assert s.groupby(pd.Series(['a', 'b', 'b'])).agg('sum').equals(
        pd.Series(data=[1, 3], index=['a', 'b']))
    assert s.groupby(pd.Series(['a', 'b', 'b'])).sum().equals(
        pd.Series(data=[1, 3], index=['a', 'b']))


# https://stackoverflow.com/questions/45338209/filtering-string-float-interger-values-in-columns-pandas
def test_filter_numbers():
    s = pd.Series([1, 'a', '3', '-1.1'])

    assert_array_equal(
        pd.to_numeric(s, errors='coerce').dropna(), [1, 3, -1.1])
    assert_array_equal(s[pd.to_numeric(s, errors='coerce').notnull()],
                       pd.Series([1, '3', '-1.1']))


def test_values_vs_tolist():
    s = pd.Series([1, 'a'])

    assert type(s.values).__module__ == 'numpy'
    assert type(s.values).__name__ == 'ndarray'

    assert type(s.tolist()).__module__ == 'builtins'
    assert type(s.tolist()).__name__ == 'list'


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
