import pandas as pd
import numpy as np


def assert_array_equal(arr1, arr2):
    if not np.array_equal(arr1, arr2):
        raise ValueError("{} is not {}".format(arr1, arr2))


#
def test_to_records():
    df = pd.DataFrame({'num': [0, 1], 'str': ['hello', 'dict']}, index=['a', 'b'])

    assert_array_equal(df.to_records(), np.array([('a', 0, 'hello'), ('b', 1, 'dict')],
                                                 dtype=[('index', 'O'), ('num', '<i8'), ('str', 'O')]))

    assert_array_equal(df.to_records(index=False), np.array([(0, 'hello'), (1, 'dict')],
                                                            dtype=[('num', '<i8'), ('str', 'O')]))


# Orient options: dict, list, series, split, records, index
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_dict.html#pandas.DataFrame.to_dict
def test_to_dict_orient():
    df = pd.DataFrame({'num': [0, 1], 'str': ['hello', 'dict']}, index=['a', 'b'])

    # default orient is 'dict'
    assert df.to_dict() == {'num': {'a': 0, 'b': 1}, 'str': {'a': 'hello', 'b': 'dict'}}

    # list
    assert df.to_dict('list') == {'num': [0, 1], 'str': ['hello', 'dict']}

    # series
    actual = df.to_dict('series')
    expected = {'num': pd.Series([0, 1], index=['a', 'b']),
                'str': pd.Series(['hello', 'dict'], index=['a', 'b'])}

    assert actual.get('num').equals(expected.get('num'))
    assert actual.get('str').equals(expected.get('str'))

    # split
    assert df.to_dict('split') == {'index': ['a', 'b'],
                                   'columns': ['num', 'str'],
                                   'data': [[0, 'hello'], [1, 'dict']]}

    # records (no index)
    assert df.to_dict('records') == [{'num': 0, 'str': 'hello'}, {'num': 1, 'str': 'dict'}]

    # index
    assert df.to_dict('index') == {'a': {'num': 0, 'str': 'hello'}, 'b': {'num': 1, 'str': 'dict'}}


def test_isnull():
    df = pd.DataFrame({
        'count': [None, None],
        'group': [None, None]
    })

    assert df.isnull().all().to_dict() == {'count': True, 'group': True}
    assert df.isnull().all().all()


# https://stackoverflow.com/questions/28218698/how-to-iterate-over-columns-of-pandas-dataframe-to-run-regression
def test_column_iteration():
    df = pd.DataFrame({
        'count': [1, 2, 3, 4],
        'group': ['a', 'a', 'b', 'b']
    })

    columns = []
    for column in df:
        columns.append(column)

    assert_array_equal(columns, ['count', 'group'])


# https://stackoverflow.com/questions/15705630/python-getting-the-row-which-has-the-max-value-in-groups-using-groupby
def test_max_min_in_group():
    df = pd.DataFrame({
        'count': [1, 2, 3, 4],
        'group': ['a', 'a', 'b', 'b']
    })

    df = df.sort_values('count', ascending=False).drop_duplicates(['group'])

    assert len(df) == 2
    assert_array_equal(df.iloc[0, :].tolist(), [4, 'b'])
    assert_array_equal(df.iloc[1, :].tolist(), [2, 'a'])


def test_assign():
    item1 = pd.Series({'Name': 'note', 'Cost': 10})
    item2 = pd.Series({'Name': 'pen', 'Cost': 5})
    item3 = pd.Series({'Name': 'phone', 'Cost': 500})
    df = pd.DataFrame([item1, item2, item3], index=['store1', 'store1', 'store2'])

    name_cost = df.assign(NameCost=lambda x: x.Name + x.Cost.astype(str))['NameCost']

    assert type(name_cost).__name__ == 'Series'
    assert name_cost.iloc[0] == 'note10'


# https://stackoverflow.com/questions/9758450/pandas-convert-dataframe-to-array-of-tuples
def test_data_frame_to_tuples():
    df = pd.DataFrame({'a': range(2), 'b': range(2)}, index=['i0', 'i1'])

    tuples = [tuple(x) for x in df.values]
    assert_array_equal(tuples, [(0, 0), (1, 1)])


def test_isin():
    df = pd.DataFrame({'a': range(3)}, index=['i0', 'i1', 'i2'])

    assert_array_equal(df['a'].isin([1, 2]), [False, True, True])
    assert_array_equal(df.index.isin(['i0']), [True, False, False])


def test_reset_index():
    df = pd.DataFrame({'a': range(3)})

    assert_array_equal(df.index, [0, 1, 2])
    assert_array_equal(df[1:3].index, [1, 2])

    drop_df = df.drop(0)
    assert_array_equal(drop_df.index, [1, 2])
    assert_array_equal(drop_df.columns, ['a'])

    reset_index_df = df.drop(0).reset_index()
    assert_array_equal(reset_index_df.index, [0, 1])
    assert_array_equal(reset_index_df.columns, ['index', 'a'])

    reset_index_df = df.drop(0).reset_index(drop=True)
    assert_array_equal(reset_index_df.columns, ['a'])


def test_dropna():
    df = pd.DataFrame({'a': [np.nan, 11, np.nan], 'b': ['A', np.nan, 'C']})

    assert len(df.dropna()) == 0
    assert len(df.dropna(subset=['a'])) == 1
    assert len(df.dropna(subset=['b'])) == 2

    # delete column
    # https://stackoverflow.com/questions/10857924/remove-null-columns-in-a-dataframe-pandas
    df = pd.DataFrame({'a': [np.nan, 11, np.nan], 'b': ['A', np.nan, 'C'], 'c': [np.nan, np.nan, np.nan]})
    assert_array_equal(df.dropna(axis=1, how='all').columns, ['a', 'b'])


def test_sum():
    df = pd.DataFrame({'a': [1, 2, 3], 'b': ['A', 'B', 'C']})
    s = df.sum()

    assert type(s).__name__ == 'Series'
    assert_array_equal(s.index, ['a', 'b'])
    assert s['a'] == 6
    assert s['b'] == 'ABC'


def test_idxmax():
    df = pd.DataFrame({'a': [10, 11, 12]})
    assert df['a'].idxmax() == 2


def test_groupby_dict():
    df = pd.DataFrame({'a': [1, 2, 3]}, index=['A', 'B', 'C'])
    d = {'A': '1', 'B': '1', 'C': '2'}

    sums_df = df.groupby(d).agg({'a': sum})
    assert_array_equal(sums_df.index, ['1', '2'])
    assert_array_equal(sums_df['a'], [3, 3])

    size_of_sums_s = df.groupby(d)['a'].agg('size')
    assert_array_equal(size_of_sums_s, [2, 1])
    assert_array_equal(size_of_sums_s.index, ['1', '2'])
    assert size_of_sums_s.name == 'a'


def test_groupby_agg():
    df = pd.DataFrame({'a': [1, 2, 3], 'b': ['A', 'A', 'B']})
    sums_df = df.groupby('b').agg({'a': sum})
    assert sums_df.loc['A', 'a'] == 3
    assert sums_df.loc['B', 'a'] == 3


def test_groupby_apply():
    df = pd.DataFrame({'a': [1, 2, 3], 'b': ['A', 'A', 'B']})

    sums_s = df.groupby('b').apply(lambda ddf, a: sum(ddf[a]), 'a')
    assert sums_s['A'] == 3
    assert sums_s['B'] == 3


#
# "In the current implementation apply calls func twice
# on the first group to decide whether it can take a fast or slow code path.
# This can lead to unexpected behavior if func has side-effects,
# as they will take effect twice for the first group."
#
# https://github.com/pandas-dev/pandas/issues/7739
# http://pandas.pydata.org/pandas-docs/stable/groupby.html#flexible-apply
#
def test_groupby_apply_warning():
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

    assert df['a'][0] == 1
    assert i == 2


def test_indexing():
    item1 = pd.Series({'Name': 'note', 'Cost': 10})
    item2 = pd.Series({'Name': 'pen', 'Cost': 5})
    item3 = pd.Series({'Name': 'phone', 'Cost': 500})
    df = pd.DataFrame([item1, item2, item3], index=['store1', 'store1', 'store2'])

    df['Location'] = df.index
    df = df.set_index('Name')
    assert_array_equal(df.index, ['note', 'pen', 'phone'])

    df = df.reset_index()
    assert_array_equal(df.index, [0, 1, 2])

    # By doing reset_index() followed by set_index() it can add index.
    df = df.set_index(['Location', 'Name'])
    assert df.loc['store1', 'note']['Cost'] == 10

    df = df.append(pd.Series(data={'Cost': 3.00}, name=('store2', 'eraser')))
    assert len(df) == 4


def test_boolean_mask():
    item1 = pd.Series({'Name': 'note', 'Cost': 10})
    item2 = pd.Series({'Name': 'pen', 'Cost': 5})
    item3 = pd.Series({'Name': 'phone', 'Cost': 500})
    df = pd.DataFrame([item1, item2, item3], index=['store1', 'store1', 'store2'])

    # using where
    only_cheap = df.where(df['Cost'] < 50)
    assert len(only_cheap) == 3
    assert np.isnan(only_cheap.loc['store2', 'Name'])
    assert only_cheap['Cost'].count() == 2  # NaN is ignored

    # using direct access
    only_cheap = df[df['Cost'] < 50]
    assert len(only_cheap) == 2

    # parens are important e.g., (df['Cost'] < 50)
    only_cheap_note = df[(df['Cost'] < 50) & (df['Name'] == 'note')]
    assert len(only_cheap_note) == 1


def test_rename():
    item1 = pd.Series({'Name': 'note', 'Cost': 10})
    item2 = pd.Series({'Name': 'pen', 'Cost': 5})
    item3 = pd.Series({'Name': 'phone', 'Cost': 500})
    df = pd.DataFrame([item1, item2, item3], index=['store1', 'store1', 'store2'])
    df.rename(columns={'Name': 'New Name'}, inplace=True)
    assert_array_equal(list(df), ['New Name', 'Cost'])


def test_data_structure():
    item1 = pd.Series({'Name': 'note', 'Cost': 10})
    item2 = pd.Series({'Name': 'pen', 'Cost': 5})
    item3 = pd.Series({'Name': 'phone', 'Cost': 500})
    df = pd.DataFrame([item1, item2, item3], index=['store1', 'store1', 'store2'])

    assert df.loc['store2', 'Cost'] == 500
    assert type(df.loc['store2']).__name__ == "Series"

    assert len(df.loc['store1']) == 2
    assert_array_equal(df.loc['store1', 'Cost'], [10, 5])

    assert_array_equal(df.T.loc['Cost'], [10, 5, 500])
    assert_array_equal(df['Cost'], [10, 5, 500])

    # chaining is not recommended because
    # 1. it copies the origin so the behavior is unexpected
    # 2. as it copies it could be slow
    # why it could be unexpected? there can be no action between anyway.(??)
    assert_array_equal(df.loc['store1']['Cost'], [10, 5])

    # drop doesn't change the origin
    assert len(df.drop('store1')) == 1

    copy_df = df.copy()
    del copy_df['Cost']
    assert len(copy_df.columns) == 1

    # Getting column headers
    # https://stackoverflow.com/questions/19482970/get-list-from-pandas-dataframe-column-headers
    assert_array_equal(df.columns.values, ['Name', 'Cost'])
    assert_array_equal(list(df), ['Name', 'Cost'])


def test_read_csv():
    df = pd.read_csv('stub/test_panda.csv')
    assert df.size == 4;
    assert df.at[0, 'name'] == 'sang'
    assert df.loc[1].at['name'] == 'kim'
    assert df.iat[0, 1] == 36


def test_merge():
    df1 = pd.read_csv('stub/test_panda.csv')
    df2 = pd.read_csv('stub/test_panda_join.csv')

    merged = pd.merge(df1, df2)
    assert merged.at[0, 'name'] == 'sang'
    assert merged.at[0, 'age'] == 36
    assert merged.at[0, 'gender'] == 'male'
    assert merged.at[1, 'name'] == 'kim'
    assert merged.at[1, 'age'] == 35
    assert merged.at[1, 'gender'] == 'female'
