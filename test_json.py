import json


def test_export_and_import_json():
    d = {'a': 1, 'b': 2, 'c': '3'}
    FILE_PATH = 'stub/test_json.json'

    # write
    with open(FILE_PATH, 'w') as jf:
        json.dump(d, jf)

    # read
    with open(FILE_PATH) as jf:
        dd = json.loads(jf.read())

        print(dd)
        assert dd['a'] == 1
        assert dd['b'] == 2
        assert dd['c'] == '3'
