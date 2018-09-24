import unittest
import pandas as pd
import numpy as np


class PandasDataFrameTest(unittest.TestCase):

    def assertArrayEqual(self, arr1, arr2):
        if not np.array_equal(arr1, arr2):
            self.fail("{} is not {}".format(arr1, arr2))

    def test_reset_index(self):
        df = pd.DataFrame({'a': range(3)})

        self.assertArrayEqual(df.index, [0, 1, 2])
        self.assertArrayEqual(df[1:3].index, [1, 2])

        drop_df = df.drop(0)
        self.assertArrayEqual(drop_df.index, [1, 2])
        self.assertArrayEqual(drop_df.columns, ['a'])

        reset_index_df = df.drop(0).reset_index()
        self.assertArrayEqual(reset_index_df.index, [0, 1])
        self.assertArrayEqual(reset_index_df.columns, ['index', 'a'])

        reset_index_df = df.drop(0).reset_index(drop=True)
        self.assertArrayEqual(reset_index_df.columns, ['a'])

    def test_dropna(self):
        df = pd.DataFrame({'a': [np.nan, 11, np.nan], 'b': ['A', np.nan, 'C']})

        self.assertEqual(len(df.dropna()), 0)
        self.assertEqual(len(df.dropna(subset=['a'])), 1)
        self.assertEqual(len(df.dropna(subset=['b'])), 2)

    def test_sum(self):
        df = pd.DataFrame({'a': [1, 2, 3], 'b': ['A', 'B', 'C']})
        s = df.sum()

        self.assertEqual(type(s).__name__, 'Series')
        self.assertArrayEqual(s.index, ['a', 'b'])
        self.assertEqual(s['a'], 6)
        self.assertEqual(s['b'], 'ABC')

    def test_idxmax(self):
        df = pd.DataFrame({'a': [10, 11, 12]})
        self.assertEqual(df['a'].idxmax(), 2)

    def test_groupby_dict(self):
        df = pd.DataFrame({'a': [1, 2, 3]}, index=['A', 'B', 'C'])
        d = {'A': '1', 'B': '1', 'C': '2'}
        
        sums_df = df.groupby(d).agg({'a': sum})
        self.assertArrayEqual(sums_df.index, ['1', '2'])
        self.assertArrayEqual(sums_df['a'], [3, 3])

        size_of_sums_s = df.groupby(d)['a'].agg('size')
        self.assertArrayEqual(size_of_sums_s, [2, 1])
        self.assertArrayEqual(size_of_sums_s.index, ['1', '2'])
        self.assertEqual(size_of_sums_s.name, 'a')

    def test_groupby_agg(self):
        df = pd.DataFrame({'a': [1, 2, 3], 'b': ['A', 'A', 'B']})
        sums_df = df.groupby('b').agg({'a': sum})
        self.assertEqual(sums_df.loc['A', 'a'], 3)
        self.assertEqual(sums_df.loc['B', 'a'], 3)

    def test_groupby_apply(self):
        df = pd.DataFrame({'a': [1, 2, 3], 'b': ['A', 'A', 'B']})

        sums_s = df.groupby('b').apply(lambda df, a: sum(df[a]), 'a')
        self.assertEqual(sums_s['A'], 3)
        self.assertEqual(sums_s['B'], 3)

    #
    # "In the current implementation apply calls func twice
    # on the first group to decide whether it can take a fast or slow code path.
    # This can lead to unexpected behavior if func has side-effects,
    # as they will take effect twice for the first group."
    #
    # https://github.com/pandas-dev/pandas/issues/7739
    # http://pandas.pydata.org/pandas-docs/stable/groupby.html#flexible-apply
    #
    def test_groupby_apply_warning(self):
        df = pd.DataFrame({'a': [0]})

        i = 0

        # a function with a side-effect
        def inc(g):
            nonlocal i
            i += 1
            # we can know that
            # this g is not a reference but a copied value
            # from the final result: df['a'][0] == 1
            g['a'] = g['a'] + 1
            return g

        df = df.groupby('a').apply(inc)

        self.assertEqual(df['a'][0], 1)
        self.assertEqual(i, 2)

    def test_indexing(self):
        item1 = pd.Series({'Name': 'note', 'Cost': 10})
        item2 = pd.Series({'Name': 'pen', 'Cost': 5})
        item3 = pd.Series({'Name': 'phone', 'Cost': 500})
        df = pd.DataFrame([item1, item2, item3], index=['store1', 'store1', 'store2'])

        df['Location'] = df.index
        df = df.set_index('Name')
        self.assertArrayEqual(df.index, ['note', 'pen', 'phone'])

        df = df.reset_index()
        self.assertArrayEqual(df.index, [0, 1, 2])

        df = df.set_index(['Location', 'Name'])
        self.assertEqual(df.loc['store1', 'note']['Cost'], 10)

        df = df.append(pd.Series(data={'Cost': 3.00}, name=('store2', 'eraser')))
        self.assertEqual(len(df), 4)

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
        self.assertEqual(type(df.loc['store2']).__name__, "Series")

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
