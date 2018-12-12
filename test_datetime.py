import datetime as dt
import time as tm


def test_datetime():
    # epoch
    assert tm.time() > 0

    dtnow = dt.datetime.fromtimestamp(tm.time())
    assert dtnow.year > 2017

    delta = dt.timedelta(days=100)
    today = dt.date.today()

    assert today > today - delta

