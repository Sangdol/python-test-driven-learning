import pandas as pd
from numpy.testing import assert_array_equal


def test_timestamp():
    assert pd.Timestamp('9/17/2018 22:09').day == 17


# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
def test_strftime():
    d = pd.to_datetime('2018-10-21')
    assert d.strftime('%m%d') == '1021'


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

