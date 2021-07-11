import pytest
from heapq import heappush, heappop, heappushpop, heapreplace, heapify


# https://docs.python.org/3/library/heapq.html
def test_heapq():
    """
    This implementation uses arrays for which heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2] for all k, counting elements from zero.

    heapq, aka priority queue.
    It's a min heap.
    heapsort is not stable.
    """
    h = []
    heappush(h, 3)
    heappush(h, 2)
    heappush(h, 1)

    assert h == [1, 3, 2]
    assert heappop(h) == 1

    assert h == [2, 3]
    assert heappushpop(h, 0) == 0

    assert h == [2, 3]
    assert heapreplace(h, -1) == 2

    assert h == [-1, 3]


def test_heapq_tuples():
    """
    heap APIs will use the first element of tuples for sorting.
    https://stackoverflow.com/questions/3954530/how-to-make-heapq-evaluate-the-heap-off-of-a-specific-attribute
    """
    h = [(1, 'a'), (2, 'b'), (3, 'c')]
    heapify(h)

    assert heappop(h) == (1, 'a')
    assert heappop(h) == (2, 'b')


def test_difference_set():
    a = {1, 2, 3}
    b = {2, 3, 4}

    assert a.difference(b) == {1}
    assert a - b == {1}


def test_intersection_of_sets():
    a = {1, 2, 3}
    b = {2, 3, 4}

    assert a.intersection(b) == {2, 3}
    assert a & b == {2, 3}


def test_union_of_sets():
    a = {1, 2, 3}
    b = {2, 3, 4}

    assert a.union(b) == {1, 2, 3, 4}
    assert a | b == {1, 2, 3, 4}


def test_symmetric_difference_of_sets():
    a = {1, 2}
    b = {2, 3}

    assert a.symmetric_difference(b) == {1, 3}
    assert a ^ b == {1, 3}


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
