import pytest


# No way to get a full name
# https://stackoverflow.com/questions/15165101/how-to-get-full-type-name-in-python
def test_module_and_name():
    assert type({}).__module__ == 'builtins'
    assert type({}).__name__ == 'dict'


# https://stackoverflow.com/questions/1823058/how-to-print-number-with-commas-as-thousands-separators
def test_number_to_comma_str():
    assert "{:,}".format(1000000.1234) == '1,000,000.1234'
    assert "{:,}".format(1000000) == '1,000,000'


# https://stackoverflow.com/questions/2225038/determine-the-type-of-an-object
def test_type_checking():
    assert type([]) is list
    assert type({}) is dict

    # isinstance is working for type inheritance
    assert isinstance({}, dict)


# noinspection PyUnreachableCode
# https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python
def test_raise_exception():
    try:
        raise ValueError('hello', 'world', '!')
        self.fail()
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


