import pandas as pd
from numpy.testing import assert_array_equal


def test_timestamp():
    assert pd.Timestamp('9/17/2018 22:09').day == 17


def test_period():
    pp = pd.Period('9/2018')
    assert type(pp.freq).__name__ == 'MonthEnd'
    assert pp.day == 30

    pp = pd.Period('9/17/2018')
    assert type(pp.freq).__name__ == 'Day'
    assert pp.day == 17


def test_to_datetime():
    assert pd.to_datetime('4/7/2017', dayfirst=True).day == 4


def test_time_delta():
    td = pd.Timestamp('9/17/18') - pd.Timestamp('9/15/18')
    assert td.days == 2

    ts = pd.Timestamp('9/15/18') + pd.Timedelta('2D 3H')
    assert ts.day == 17
    assert ts.hour == 3


def test_date_range():
    dates = pd.date_range('9/1/2018', periods=3, freq='D')
    assert_array_equal(dates.astype(str), ['2018-09-01', '2018-09-02', '2018-09-03'])
    assert_array_equal(dates.weekday_name, ['Saturday', 'Sunday', 'Monday'])
