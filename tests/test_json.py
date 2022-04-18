import json
import pandas as pd


def test_export_and_import_dict():
    d = {'a': 1, 'b': 2, 'c': '3'}
    FILE_PATH = 'stub/test_json_dict.json'

    # write
    with open(FILE_PATH, 'w') as jf:
        json.dump(d, jf)

    # read
    with open(FILE_PATH) as jf:
        dd = json.loads(jf.read())

        assert dd['a'] == 1
        assert dd['b'] == 2
        assert dd['c'] == '3'


def test_export_and_import_series():
    s = pd.Series([1, 2], index=['a', 'b'])

    FILE_PATH = 'stub/test_json_dataframe.json'

    # write
    with open(FILE_PATH, 'w') as jf:
        json.dump(s.to_dict(), jf)

    # read
    with open(FILE_PATH) as jf:
        dd = json.loads(jf.read())

        assert dd['a'] == 1
        assert dd['b'] == 2
