"""
https://docs.python.org/3/library/re.html
"""
import re


def test_findall():
    assert re.findall('\d+', 'abc123abc') == ['123']

    # default string
    assert re.findall('\d+|$', 'abc') == ['']

    pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
    regex = re.compile(pattern, flags=re.IGNORECASE)
    res = regex.findall('abc@d.com,abc2@d.com')
    assert res == [('abc', 'd', 'com'), ('abc2', 'd', 'com')]


def test_split():
    text = 'a\t b  c'

    assert re.split('\s+', text) == ['a', 'b', 'c']

    regex = re.compile('\s+')
    assert regex.split(text) == ['a', 'b', 'c']


def test_match():
    # should match starting part
    assert re.match('\s', ' a')
    assert not re.match('\s', 'a')
    assert re.match('\d\d', '11')
    assert not re.match('\d\d', 'a11')

    #
    pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
    regex = re.compile(pattern, flags=re.IGNORECASE)
    m = regex.match('abc@d.com')
    assert m.groups() == ('abc', 'd', 'com')
