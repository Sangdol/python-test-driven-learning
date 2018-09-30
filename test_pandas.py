from datetime import datetime

import pandas as pd
import numpy as np


def assert_array_equal(arr1, arr2):
    if not np.array_equal(arr1, arr2):
        raise ValueError("{} is not {}".format(arr1, arr2))


def test_period_index():
    quarter_period = pd.PeriodIndex(['2010-01', '2010-02', '2010-04', '2010-10'], freq='Q')

    # https://stackoverflow.com/questions/34800343/python-pandas-convert-type-from-pandas-period-to-string
    assert_array_equal(quarter_period.strftime('%YQ%q'), ['2010Q1', '2010Q1', '2010Q2', '2010Q4'])
    assert_array_equal(quarter_period.map(str), ['2010Q1', '2010Q1', '2010Q2', '2010Q4'])
    assert_array_equal(quarter_period.to_series().astype(str), ['2010Q1', '2010Q1', '2010Q2', '2010Q4'])


def test_cut():
    s = pd.Series([0, 1, 2])
    s_labeled = pd.cut(s, 3, labels=['S', 'M', 'L'])

    assert_array_equal(s_labeled, ['S', 'M', 'L'])


# https://datascience.stackexchange.com/questions/12645/how-to-count-the-number-of-missing-values-in-each-row-in-pandas-dataframe
def test_counting_null():
    s = pd.Series([0, np.nan, None])

    assert s.isnull().sum() == 2
    assert s.isnull().sum() == s.isna().sum()  # isnull is an alias of isna
    assert s.notna().sum() == 1


# https://stackoverflow.com/questions/22825349/converting-between-datetime-and-pandas-timestamp-objects
def test_timestamp_to_datetime():
    ts = pd.Timestamp('2018-09-14 00:00:00', tz=None)
    assert ts.to_pydatetime(), datetime(2018, 9, 14, 0 == 0)


# https://pandas.pydata.org/pandas-docs/version/0.23.4/text.html
def test_str():
    df = pd.DataFrame({'a': [10, 11, 12], 'b': ['A', 'B', 'C']})

    assert_array_equal(df['b'].str.lower(), ['a', 'b', 'c'])
    assert_array_equal(df['b'].str[0], ['A', 'B', 'C'])
    assert_array_equal(df.columns.str.upper().str.replace('A', 'B'), ['B', 'B'])

    assert df['b'].str.cat() == 'ABC'
    assert df['b'].str.cat(sep=',') == 'A,B,C'


def test_to_datetime():
    date_strs = ['2018/01/30', '2018/02/28']
    dates = pd.to_datetime(date_strs, format='%Y/%m/%d')
    assert dates[0], datetime(2018, 1 == 30)


# np.newaxis is an axis for 'None' and is used to increase the dimension
# https://stackoverflow.com/questions/29241056/how-does-numpy-newaxis-work-and-when-to-use-it
def test_new_axis():
    x = np.array([1, 2, 3])
    assert_array_equal(x[:, np.newaxis], [[1], [2], [3]])
    assert_array_equal(x[np.newaxis, :], [[1, 2, 3]])
