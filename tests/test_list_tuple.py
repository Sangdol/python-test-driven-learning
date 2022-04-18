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


# https://stackoverflow.com/questions/12876177/how-to-create-a-tuple-with-only-one-element
def test_single_item_tuple():
    assert (1) == 1
    assert type((1)) == int

    assert type((1,)) == tuple
    assert type(tuple([1])) == tuple


def test_tuple():
    t = (1, 'a', 2, 'b')
    assert len(t) == 4

    # unpacking
    a, b = ('a', 'b')
    assert a == 'a'


def test_list_comprehension():
    assert list(map(lambda x: x ** 2, range(3))) == [0, 1, 4]
    assert [x ** 2 for x in range(3)] == [0, 1, 4]

    comb = [(x, y) for x in [1, 2] for y in [2, 3] if x != y]
    assert comb == [(1, 2), (1, 3), (2, 3)]

def test_for_if_any():
    numbers = ['1', '11', '111', '2', '22', '222']
    keys = ['1', '2']

    s = set()
    for n in numbers:
        for k in keys:
            if n.count(k) == 3:
                s.add(n)

    ss = {n for n in numbers if any(n.count(k) == 3 for k in keys)}

    assert s == ss
