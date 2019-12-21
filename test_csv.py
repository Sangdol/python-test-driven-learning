import csv


def test_reader():
    with open('stub/test_csv.csv') as f:
        reader = csv.reader(f)
        row = reader.__next__()

        assert type(row) == list
        assert row[0] == 'a'

        row = reader.__next__()
        assert row[0] == '1'


def test_dict_reader():
    with open('stub/test_csv.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        row = reader.__next__()
        a, b = row['a'], row['b']

        assert a == '1'
        assert b == '2'
