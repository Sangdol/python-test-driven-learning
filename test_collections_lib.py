from collections import Counter, deque, OrderedDict


def test_deque():
    """
    deque (pronoune "deck") is good at pop(0) (leftpop()) but worse at random access compared to list.
    https://docs.python.org/3/library/collections.html#collections.deque
    https://stackoverflow.com/questions/6256983/how-are-deques-in-python-implemented-and-when-are-they-worse-than-lists
    https://stackoverflow.com/questions/39522787/time-complexity-of-random-access-in-deque-in-python
    """

    d = deque('abcd')

    assert d[0] == 'a'
    assert d.popleft() == 'a'
    assert len(d) == 3

    d.extend('efg')
    assert len(d) == 6
    assert d.pop() == 'g'

    d.appendleft('a')
    assert d[0] == 'a'

    d.append('g')
    assert d[-1] == 'g'

    d.extendleft('h')
    d.rotate(-1)
    assert d[0] == 'a'
    assert d[-1] == 'h'


def test_counter():
    c = Counter(['a', 'a', 'b'])

    assert c['a'] == 2
    assert c['c'] == 0
    assert list(c.elements()) == ['a', 'a', 'b']
    assert c.most_common() == [('a', 2), ('b', 1)]
    assert c.most_common(1) == [('a', 2)]

    c2 = Counter('ab')

    assert c2['a'] == 1
    assert c2['c'] == 0

    c3 = Counter('aaabbc')
    c3.subtract(Counter('aabbcc'))

    assert c3['a'] == 1
    assert c3['b'] == 0
    assert c3['c'] == -1
    assert list(c3.elements()) == ['a']

    c3.update('aa')
    assert c3['a'] == 3
    assert list(c3.elements()) == ['a', 'a', 'a']


def test_ordered_dict():
    # LIFO / Stack

    d = OrderedDict.fromkeys('abc')
    assert list(d.items()) == [('a', None), ('b', None), ('c', None)]

    d.move_to_end('b')
    assert list(d.items()) == [('a', None), ('c', None), ('b', None)]

    e = d.popitem()
    assert e == ('b', None)

    d['d'] = None
    assert list(d.items()) == [('a', None), ('c', None), ('d', None)]

    e = d.popitem()
    assert e == ('d', None)

    # FIFO / Queue

    e = d.popitem(last=False)
    assert e == ('a', None)
