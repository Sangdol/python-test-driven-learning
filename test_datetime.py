import unittest
import datetime as dt
import time as tm


class DatetimeTest(unittest.TestCase):

    def test_datetime(self):
        # epoch
        self.assertTrue(tm.time() > 0)

        dtnow = dt.datetime.fromtimestamp(tm.time())
        self.assertTrue(dtnow.year > 2017)

        delta = dt.timedelta(days=100)
        today = dt.date.today()

        self.assertTrue(today > today - delta)


if __name__ == '__main__':
    unittest.main()
