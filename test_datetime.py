"""
https://docs.python.org/3/library/datetime.html
"""
import datetime as dt
import time as tm


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


def test_datetime():
    assert tm.time() > 0  # epoch in float e.g., 1544707185.613296

    dtnow = dt.datetime.fromtimestamp(tm.time(), dt.timezone.utc)
    assert dtnow.year > 2017

    delta = dt.timedelta(days=100)
    today = dt.date.today()

    assert today > today - delta

