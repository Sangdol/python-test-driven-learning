from string import Template


# f-string is introduced at Python 3.6
def test_fstring():
    assert ('%s %d' % ('a', 1)) == 'a 1'
    assert (('%(name)s: %(age)d') % {'name': 'sang', 'age': 36}) == 'sang: 36'


def test_template():
    s = Template('$who likes $what')
    assert s.substitute(who='Sang', what='Template') == 'Sang likes Template'


# https://stackoverflow.com/questions/1504717/why-does-comparing-strings-using-either-or-is-sometimes-produce-a-differe
def test_equal_vs_is():
    assert 'abc' is 'abc'
    assert 'abc' == 'abc'
    assert 'abc' is not ''.join(['a', 'b', 'c'])


# r = raw
# https://docs.python.org/2/reference/lexical_analysis.html#string-literals
def test_r_string():
    assert r'\n' == '\\n'
    assert r'\n' != '\n'


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

    # https://stackoverflow.com/questions/45310254/fixed-digits-after-decimal-with-f-strings
    n = 100000.1234
    assert f'{n:,.2f}' == '100,000.12'


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
