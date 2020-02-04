def test_max():
    assert max(1, 2) == 2
    assert max([1, 2]) == 2

    d = {
        'a': 1,
        'b': 2
    }

    assert max(d, key=d.get) == 'b'

    d = {
        'a': {
            'aa': 1
        },
        'b': {
            'aa': 2
        }
    }

    assert max(d, key=lambda key: d[key]['aa']) == 'b'


def test_map():
    names = ['sanghyun lee', 'hyunji kim']

    def lastname(name):
        return name.split(' ')[1]

    assert list(map(lastname, names)) == ['lee', 'kim']
