"""
https://docs.python.org/3/library/datetime.html
"""
import datetime as dt
import time as tm


def test_add_str_day():
    def add_days(date, days):
        """
        Take a string date and add the days to it,
        and returns the date string.
        """

        datetime = dt.datetime.strptime(date, '%Y-%m-%d')
        added = datetime + dt.timedelta(days=days)
        return added.strftime('%Y-%m-%d')

    assert add_days('2019-08-30', 1) == '2019-08-31'
    assert add_days('2019-08-30', 2) == '2019-09-01'
    assert add_days('2019-08-30', 0) == '2019-08-30'
    assert add_days('2019-08-30', 10) == '2019-09-09'


# Parse a string representing a time according to a format.
# https://docs.python.org/3/library/time.html#time.strptime
def test_strptime():
    assert dt.datetime.strptime('2019-06-07', '%Y-%m-%d').strftime('%m') == '06'


def test_time_comparison():
    assert dt.datetime.now().time() >= dt.time(hour=0)
    assert dt.datetime.now().time() <= dt.time(hour=23)


def test_timezone():
    d = dt.datetime(2007, 12, 6, 15, 29, 43, 79060, tzinfo=dt.timezone.utc)
    assert d.isoformat() == '2007-12-06T15:29:43.079060+00:00'

    d = dt.datetime.now(dt.timezone.utc)
    assert d.strftime('%Z') == 'UTC'


# Format codes
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
def test_datetime_format():
    d = dt.datetime(2007, 12, 6, 15, 29, 43, 79060)

    assert d.strftime('%Y-%m-%d %H:%M:%S') == '2007-12-06 15:29:43'
    assert d.strftime('%y %B %b') =='07 December Dec'

    # https://en.wikipedia.org/wiki/ISO_8601
    assert d.isoformat() == '2007-12-06T15:29:43.079060'
    assert d.isoformat(' ') == '2007-12-06 15:29:43.079060'


def test_timedelta():
    assert tm.time() > 0  # epoch in float e.g., 1544707185.613296

    dtnow = dt.datetime.fromtimestamp(tm.time(), dt.timezone.utc)
    assert dtnow.year > 2017

    delta = dt.timedelta(days=100)
    today = dt.date.today()

    assert today > today - delta

