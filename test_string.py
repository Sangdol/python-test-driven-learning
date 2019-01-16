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
