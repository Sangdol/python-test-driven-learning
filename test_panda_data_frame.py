import unittest
import pandas as pd
import numpy as np


class PandaTest(unittest.TestCase):

    def assertArrayEqual(self, arr1, arr2):
        if not np.array_equal(arr1, arr2):
            self.fail("{} is not {}".format(arr1, arr2))

    def test_indexing(self):
        item1 = pd.Series({'Name': 'note', 'Cost': 10})
        item2 = pd.Series({'Name': 'pen', 'Cost': 5})
        item3 = pd.Series({'Name': 'phone', 'Cost': 500})
        df = pd.DataFrame([item1, item2, item3], index=['store1', 'store1', 'store2'])

        df['Location'] = df.index
        df = df.set_index('Name')
        self.assertArrayEqual(df.index, ['note', 'pen', 'phone'])

        df = df.reset_index()
        df = df.set_index(['Location', 'Name'])
        self.assertEqual(df.loc['store1', 'note']['Cost'], 10)

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

    def test_rename(self):
        item1 = pd.Series({'Name': 'note', 'Cost': 10})
        item2 = pd.Series({'Name': 'pen', 'Cost': 5})
        item3 = pd.Series({'Name': 'phone', 'Cost': 500})
        df = pd.DataFrame([item1, item2, item3], index=['store1', 'store1', 'store2'])
        df.rename(columns={'Name': 'New Name'}, inplace=True)
        self.assertArrayEqual(list(df), ['New Name', 'Cost'])

    def test_data_structure(self):
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

    def test_read_csv(self):
        df = pd.read_csv('stub/test_panda.csv')
        self.assertEqual(df.size, 4);
        self.assertEqual(df.at[0, 'name'], 'sang')
        self.assertEqual(df.loc[1].at['name'], 'kim')
        self.assertEqual(df.iat[0, 1], 36)

    def test_merge(self):
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
