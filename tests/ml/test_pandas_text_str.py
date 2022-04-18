#
# https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html
#
import pandas as pd
import numpy as np


def test_str_cat():
    s = pd.Series(['a', 'b', np.nan, 'd'])

    assert s.str.cat(sep=',') == 'a,b,d'


def test_str_join():
    s = pd.Series([['a', 'b'], [1, 2]])

    joined_s = s.str.join(',')
    assert joined_s[0] == 'a,b'
    assert np.isnan(joined_s[1])

