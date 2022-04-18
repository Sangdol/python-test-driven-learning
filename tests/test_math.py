from fractions import Fraction
import pytest
import math


# https://docs.python.org/3/library/fractions.html
def test_fraction():
    assert Fraction(1, 2) == 0.5
    assert Fraction(2, 4) == 0.5

    assert Fraction('3/7') != 3/7
    assert float(Fraction('3/7')) == 3/7

    # In the __eq__(a, b) implementation, "a == a.from_float(b)".
    assert Fraction(7720456504063707, 18014398509481984) == 3/7

    assert Fraction('3e-2') == Fraction(3, 100)


# https://stackoverflow.com/questions/27946595/how-to-manage-division-of-huge-numbers-in-python
def test_division():
    try:
        2**3000 / 10
        pytest.fail()
    except OverflowError as e:
        assert str(e) == 'integer division result too large for a float'

    # No exception occurs here.
    2**3000 // 10


def test_combination_formula():
    def nCr(n, r):
        f = math.factorial
        return f(n) // f(n - r) // f(r)

    assert nCr(3, 2) == 3
    assert nCr(4, 2) == 6


def test_divmod():
    assert 5 // 2 == 2
    assert 5 % 2 == 1
    assert divmod(5, 2) == (2, 1)
    assert divmod(2, 2) == (1, 0)
    assert divmod(1, 2) == (0, 1)
    assert divmod(10, 2) == (5, 0)


def test_e_number():
    assert 1e3 == 1000
    assert 1e-3 == 0.001
    assert 1.1e3 == 1100
