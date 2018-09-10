import unittest
from datetime import datetime

import pandas as pd
import numpy as np


class PandaTest(unittest.TestCase):

    def assertArrayEqual(self, arr1, arr2):
        if not np.array_equal(arr1, arr2):
            self.fail("{} is not {}".format(arr1, arr2))

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

    def test_boolean_mask(self):
        item1 = pd.Series({'Name': 'note', 'Cost': 10})
        item2 = pd.Series({'Name': 'pen', 'Cost': 5})
        item3 = pd.Series({'Name': 'phone', 'Cost': 500})
        df = pd.DataFrame([item1, item2, item3], index=['store1', 'store1', 'store2'])

        # using where
        only_cheap = df.where(df['Cost'] < 50)
        self.assertEqual(len(only_cheap), 3)
        self.assertTrue(np.isnan(only_cheap.loc['store2', 'Name']))
        self.assertEqual(only_cheap['Cost'].count(), 2)  # NaN is ignored

        # using direct access
        only_cheap = df[df['Cost'] < 50]
        self.assertEqual(len(only_cheap), 2)

        only_cheap_note = df[(df['Cost'] < 50) & (df['Name'] == 'note')]
        self.assertEqual(len(only_cheap_note), 1)

    def test_data_frame_rename(self):
        item1 = pd.Series({'Name': 'note', 'Cost': 10})
        item2 = pd.Series({'Name': 'pen', 'Cost': 5})
        item3 = pd.Series({'Name': 'phone', 'Cost': 500})
        df = pd.DataFrame([item1, item2, item3], index=['store1', 'store1', 'store2'])
        df.rename(columns={'Name': 'New Name'}, inplace=True)
        self.assertArrayEqual(list(df), ['New Name', 'Cost'])

    def test_data_frame_data_structure(self):
        item1 = pd.Series({'Name': 'note', 'Cost': 10})
        item2 = pd.Series({'Name': 'pen', 'Cost': 5})
        item3 = pd.Series({'Name': 'phone', 'Cost': 500})
        df = pd.DataFrame([item1, item2, item3], index=['store1', 'store1', 'store2'])

        self.assertEqual(df.loc['store2', 'Cost'], 500)
        self.assertEqual(str(type(df.loc['store2'])),
                         "<class 'pandas.core.series.Series'>")

        self.assertEqual(len(df.loc['store1']), 2)
        self.assertArrayEqual(df.loc['store1', 'Cost'], [10, 5])

        self.assertArrayEqual(df.T.loc['Cost'], [10, 5, 500])
        self.assertArrayEqual(df['Cost'], [10, 5, 500])

        # chaining is not recommended because
        # 1. it copies the origin so the behavior is unexpected
        # 2. as it copies it could be slow
        # why it could be unexpected? there can be no action between anyway.(??)
        self.assertArrayEqual(df.loc['store1']['Cost'], [10, 5])

        # drop doesn't change the origin
        self.assertEqual(len(df.drop('store1')), 1)

        copy_df = df.copy()
        del copy_df['Cost']
        self.assertEqual(len(copy_df.columns), 1)

        # Getting column headers
        # https://stackoverflow.com/questions/19482970/get-list-from-pandas-dataframe-column-headers
        self.assertArrayEqual(df.columns.values, ['Name', 'Cost'])
        self.assertArrayEqual(list(df), ['Name', 'Cost'])

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
