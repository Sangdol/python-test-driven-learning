import unittest
from datetime import datetime

import pandas as pd
import numpy as np


class PandasTest(unittest.TestCase):

    def assertArrayEqual(self, arr1, arr2):
        if not np.array_equal(arr1, arr2):
            self.fail("{} is not {}".format(arr1, arr2))

    def test_cut(self):
        s = pd.Series([0, 1, 2])
        s_labeled = pd.cut(s, 3, labels=['S', 'M', 'L'])

        self.assertArrayEqual(s_labeled, ['S', 'M', 'L'])

    def test_series_category(self):
        s = pd.Series(['A', 'B', 'C'], index=['A', 'B', 'C']).astype(
            'category', categories=['C', 'B', 'A'], ordered=True)

        self.assertEqual(len(s[s > 'B']), 1)

    # https://datascience.stackexchange.com/questions/12645/how-to-count-the-number-of-missing-values-in-each-row-in-pandas-dataframe
    def test_counting_null(self):
        s = pd.Series([0, np.nan, None])

        self.assertEqual(s.isnull().sum(), 2)
        self.assertEqual(s.isnull().sum(), s.isna().sum())  # isnull is an alias of isna
        self.assertEqual(s.notna().sum(), 1)

    # https://stackoverflow.com/questions/22825349/converting-between-datetime-and-pandas-timestamp-objects
    def test_timestamp_to_datetime(self):
        ts = pd.Timestamp('2018-09-14 00:00:00', tz=None)
        self.assertEqual(ts.to_pydatetime(), datetime(2018, 9, 14, 0, 0))

    # https://pandas.pydata.org/pandas-docs/version/0.23.4/text.html
    def test_str(self):
        df = pd.DataFrame({'a': [10, 11, 12], 'b': ['A', 'B', 'C']})

        self.assertArrayEqual(df['b'].str.lower(), ['a', 'b', 'c'])
        self.assertArrayEqual(df['b'].str[0], ['A', 'B', 'C'])
        self.assertArrayEqual(df.columns.str.upper().str.replace('A', 'B'), ['B', 'B'])

        self.assertEqual(df['b'].str.cat(), 'ABC')
        self.assertEqual(df['b'].str.cat(sep=','), 'A,B,C')

    def test_to_datetime(self):
        date_strs = ['2018/01/30', '2018/02/28']
        dates = pd.to_datetime(date_strs, format='%Y/%m/%d')
        self.assertEqual(dates[0], datetime(2018, 1, 30))

    # np.newaxis is an axis for 'None' and is used to increase the dimension
    # https://stackoverflow.com/questions/29241056/how-does-numpy-newaxis-work-and-when-to-use-it
    def test_new_axis(self):
        x = np.array([1, 2, 3])
        self.assertArrayEqual(x[:, np.newaxis], [[1], [2], [3]])
        self.assertArrayEqual(x[np.newaxis, :], [[1, 2, 3]])

    def test_series_dtype(self):
        self.assertEqual(str(pd.Series([1]).dtype), 'int64')
        self.assertEqual(str(pd.Series([1, None]).dtype), 'float64')
        self.assertEqual(str(pd.Series(['a', None]).dtype), 'object')

    def test_series_nan(self):
        nan = pd.Series([1, None])[1]
        self.assertEqual(str(nan), 'nan')
        self.assertNotEqual(nan, np.nan)
        self.assertTrue(np.isnan(nan))

    def test_series_dictionary(self):
        numbers = {'one': 1, 'two': 2}
        s = pd.Series(numbers)
        self.assertArrayEqual(s.index.values, ['one', 'two'])
        self.assertArrayEqual(s.values, [1, 2])

        s = pd.Series([1, 2], index=['one', 'two'])
        self.assertArrayEqual(s.index.values, ['one', 'two'])
        self.assertArrayEqual(s.values, [1, 2])

        s = pd.Series(s, index=['one', 'three'])
        self.assertEqual(s[0], 1)
        self.assertEqual(s.index[0], 'one')
        self.assertTrue(np.isnan(s[1]))
        self.assertEqual(s.index[1], 'three')

    def test_series_name(self):
        s = pd.Series([1, 2], name='numbers')
        self.assertEqual(s.name, 'numbers')

    def test_querying_series(self):
        numbers = {'one': 1, 'two': 2}
        s = pd.Series(numbers)

        self.assertEqual(s.iloc[1], 2)
        self.assertEqual(s.loc['one'], 1)

        # not recommended as labels can be number
        self.assertEqual(s[1], 2)
        self.assertEqual(s['one'], 1)

        # vectorized calculation is much faster
        self.assertEqual(np.sum(s), 3)

        s += 2
        self.assertEqual(np.sum(s), 7)

        # append doesn't change the original object
        new_s = s.append(pd.Series({'three': 3}))
        self.assertEqual(len(s), 2)
        self.assertEqual(len(new_s), 3)


if __name__ == '__main__':
    unittest.main()
