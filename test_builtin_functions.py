def test_map():
    names = ['sanghyun lee', 'hyunji kim']

    def lastname(name):
        return name.split(' ')[1]

    assert list(map(lastname, names)) == ['lee', 'kim']
