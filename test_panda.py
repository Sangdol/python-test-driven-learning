import unittest

import pandas as pd
import numpy as np


class PandaTest(unittest.TestCase):

    def assertArrayEqual(self, arr1, arr2):
        self.assertTrue(np.array_equal(arr1, arr2))

    def test_series(self):
        self.assertEqual(str(pd.Series([1]).dtype), 'int64')
        self.assertEqual(str(pd.Series([1, None]).dtype), 'float64')
        self.assertEqual(str(pd.Series(['a', None]).dtype), 'object')

        # NAN
        nan = pd.Series([1, None])[1]
        self.assertEqual(str(nan), 'nan')
        self.assertNotEqual(nan, np.nan)
        self.assertTrue(np.isnan(nan))

        # dictionary
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

    def test_read_csv_and_data_frame(self):
        df = pd.read_csv('stub/test_panda.csv')
        self.assertEqual(df.size, 4);
        self.assertEqual(df.at[0, 'name'], 'sang')
        self.assertEqual(df.loc[1].at['name'], 'kim')
        self.assertEqual(df.iat[0, 1], 36)

    def test_data_frame_merge(self):
        df1 = pd.read_csv('stub/test_panda.csv')
        df2 = pd.read_csv('stub/test_panda_join.csv')

        merged = pd.merge(df1, df2)
        self.assertEqual(merged.at[0, 'name'], 'sang')
        self.assertEqual(merged.at[0, 'age'], 36)
        self.assertEqual(merged.at[0, 'gender'], 'male')
        self.assertEqual(merged.at[1, 'name'], 'kim')
        self.assertEqual(merged.at[1, 'age'], 35)
        self.assertEqual(merged.at[1, 'gender'], 'female')


if __name__ == '__main__':
    unittest.main()
