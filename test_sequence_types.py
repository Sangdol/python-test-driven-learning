def test_tuple():
    t = (1, 'a', 2, 'b')
    assert len(t) == 4

    # unpacking
    a, b = ('a', 'b')
    assert a == 'a'


def test_list():
    l = [1, 2, 3]
    assert len(l) == 3

    l.append(4)
    assert len(l) == 4

    assert [1] + [2] == [1, 2]
    assert [1] * 3 == [1, 1, 1]
    assert 1 in [1, 2]

    # slice
    assert 'hello'[0:2] == 'he'
    assert 'hello'[-4:-2] == 'el'
    assert 'hello'[-2:] == 'lo'
    assert 'hello'[:3] == 'hel'
    assert 'hello'[3:] == 'lo'

    # string
    assert 'he' in 'hello'
    assert 'he' * 3 == 'hehehe'
    assert 'hello world'.split(' ')[-1] == 'world'


# https://docs.python.org/3/library/stdtypes.html#dictionary-view-objects
def test_dictionary_view_objects():
    x = {'a': 1, 'b': 2}

    assert list(x) == ['a', 'b']
    assert list(x.keys()) == ['a', 'b']
    assert list(x.values()) == [1, 2]
    assert list(x.items()) == [('a', 1), ('b', 2)]


def test_dictionary_functions():
    x = {'hello': 'world'}

    assert x.get('hi', 'default') == 'default'


def test_dictionary():
    x = {'hello': 'world'}
    assert x['hello'] == 'world'

    x['hallo'] = 'welt'
    assert x['hallo'] == 'welt'

    keys = ''
    for key in x:
        keys += key

    assert keys == 'hellohallo'

    values = ''
    for value in x.values():
        values += value

    assert values == 'worldwelt'

    key_value = ''
    for key, value in x.items():
        key_value += (key + value)

    assert key_value == 'helloworldhallowelt'
