def test_bytes_to_string():
    assert b'abc' != 'abc'
    assert str(b'abc', 'utf-8') == 'abc'


# https://docs.python.org/2/library/string.html#formatstrings
def test_format():
    n = 0.123

    assert '{:.2%}'.format(n) == '12.30%'
    assert '{:.2}'.format(n) == '0.12'


# https://stackoverflow.com/questions/1823058/how-to-print-number-with-commas-as-thousands-separators
def test_number_to_comma_str():
    assert "{:,}".format(1000000.1234) == '1,000,000.1234'
    assert "{:,}".format(1000000) == '1,000,000'


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
