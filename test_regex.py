"""
https://docs.python.org/3/library/re.html
"""
import re


def test_findall():
    assert re.findall('\d+', 'abc123abc') == ['123']

    # default string
    assert re.findall('\d+|$', 'abc') == ['']
