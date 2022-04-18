import pytest


def test_dict_list():
    l = [('a', 1), ('b', 2)]

    assert dict(l) == {'a': 1, 'b': 2}


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

    if 'hello' not in x:
        pytest.fail()

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
