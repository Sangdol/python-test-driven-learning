import pytest


# https://docs.python.org/2/library/stdtypes.html#truth-value-testing
def test_false_value():
    assert not None
    assert not False
    assert not 0
    assert not ''
    assert not ()
    assert not []
    assert not {}


# https://stackoverflow.com/questions/132988/is-there-a-difference-between-and-is-in-python
def test_if_equal_vs_is():
    """
    `is` reference equality
    `==` value equality
    """

    a = 1
    assert a is 1  # This is True as Python caches small integer objects
    assert a == 1

    # https://stackoverflow.com/questions/15171695/whats-with-the-integer-cache-inside-python
    b = 1000
    assert a is 10**0
    assert b is not 10**3


def test_if_statement():
    a = 10
    if a > 5:
        assert 'foo'.upper() == 'FOO'
    elif a == 11:
        pytest.fail()
    else:
        pytest.fail()


def test_enumerate():
    items = [1, 2, 3]

    indices = []
    values = []

    for i, v in enumerate(items):
        indices.append(i)
        values.append(v)

    assert indices == [0, 1, 2]
    assert values == items

    indices = []

    for i, v in enumerate(items, 10):
        indices.append(i)

    assert indices == [10, 11, 12]


def test_zip_iteration():
    x = y = range(2)

    zipped = zip(x, y)
    assert list(zipped) == [(0, 0), (1, 1)]
    assert list(zipped) == []


# https://docs.python.org/3.4/library/functions.html#zip
def test_zip_upzip():
    assert list(zip('abc', '12')) == [('a', '1'), ('b', '2')]
    assert list(zip(range(3), (range(3)))) == [(0, 0), (1, 1), (2, 2)]

    # unzip
    x = [1, 2, 3]
    y = [0, 0, 0]

    zipped = zip(x, y)

    assert list(zipped) == [(1, 0), (2, 0), (3, 0)]

    x2, y2 = zip(*zip(x, y))
    assert list(x2) == x
    assert list(y2) == y


# noinspection PyUnreachableCode
# https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python
def test_raise_exception():
    try:
        raise ValueError('hello', 'world', '!')
        pytest.fail()
    except ValueError as err:
        assert err.args == ('hello', 'world', '!')


# stars, asterisks
# https://stackoverflow.com/questions/36901/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters
def test_extra_args():
    def test1(first, *args, **kwargs):
        return first, args, kwargs

    first, args, kwargs = test1(1, 2, 3, a=1, b="b")
    assert first == 1
    assert args == (2, 3)
    assert kwargs == {"a": 1, "b": "b"}

    first, args, kwargs = test1(1, *(2, 3), **{"a": 1, "b": "b"})
    assert first == 1
    assert args == (2, 3)
    assert kwargs == {"a": 1, "b": "b"}


def test_iterable_unpacking():
    head, *body, tail = range(5)
    assert head == 0
    assert body == [1, 2, 3]
    assert tail == 4

    first, _, third, *_ = range(10)
    assert first == 0
    assert third == 2


def test_iterable():
    # https://wiki.python.org/moin/Iterator - in Python3 next() -> __next__()
    class CustomIterable:
        def __init__(self):
            self.list = [1, 2]

        def __iter__(self):
            return self

        def __next__(self):
            if self.list:
                return self.list.pop()
            else:
                raise StopIteration

    it = CustomIterable()
    s = 0
    for i in it:
        s += i

    assert s == 3


def test_iterator():
    # All iterators can only be iterated over once.
    it = iter([1, 2])

    assert sum(it) == 3
    assert sum(it) == 0


def test_yield():
    def generator_yield():
        for i in range(5):
            yield i

    gen = generator_yield()

    assert next(gen) == 0
    assert gen.__next__() == 1
    assert sum(gen) == 9
    assert sum(gen) == 0

    try:
        next(gen)
        pytest.fail()
    except StopIteration:
        pass

    gen2 = generator_yield()
    assert sum(gen2) == 10


def test_walrus_operator():
    """
    https://docs.python.org/3/whatsnew/3.8.html#assignment-expressions
    """
    a = [1, 2, 3]
    if (n := len(a)) > 2:
        assert n == 3, 'Avoiding calling len() twice'
