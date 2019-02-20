def test_f_string():
    ten = 10

    assert f'ten is {ten}' == 'ten is 10'

    f = 1.0

    assert f'float {f}' == 'float 1.0'

    s = 'str'

    assert f'string {s}' == 'string str'


# https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float
def test_is_number():
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    assert is_number('123')
    assert is_number('12.3')
    assert is_number('-12.3')
    assert not is_number('ab1')


def test_isnumeric():
    assert '123'.isnumeric()
    assert not '-123'.isnumeric()
    assert not '12.3'.isnumeric()
    assert not '-12.3'.isnumeric()
    assert not 'a1'.isnumeric()


# https://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method
def test_contains():
    # https://docs.python.org/3/reference/expressions.html#membership-test-details
    assert 'abc' in 'abcde'
    assert '123' not in 'abcde'

    assert 'abc'.find('b') == 1
    assert 'abc'.find('0') == -1
