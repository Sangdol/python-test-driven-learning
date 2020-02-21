"""
https://docs.python.org/3/library/bisect.html
"""


from bisect import bisect, bisect_left, bisect_right, insort_left, insort_right


def test_bisect_left():
    """Locate the insertion point for x in a to maintain sorted order.
    """
    assert bisect_left([10, 20, 30], 5) == 0
    assert bisect_left([10, 20, 30], 15) == 1
    assert bisect_left([10, 20, 30], 30) == 2


def test_bisect_right():
    """Similar to bisect_left(), but returns an insertion point
    which comes after (to the right of) any existing entries of x in a.

    bisect == bisect_right
    """
    assert bisect_right([10, 20, 30], 5) == 0
    assert bisect_right([10, 20, 30], 15) == 1
    assert bisect_right([10, 20, 30], 30) == 3
    assert bisect([10, 20, 30], 30) == 3


def test_insort_left():
    """Insert x in a in sorted order.

    insort_left(a, 5) == a.insert(bisect.bisect_left(a, x, lo, hi), x)
    """
    a = [10, 20, 30]
    insort_left(a, 5)
    assert a == [5, 10, 20, 30]

    a = [10, 20, 30]
    insort_left(a, 30)
    assert a == [10, 20, 30, 30]


def test_insort_right():
    """Similar to insort_left(), but inserting x in a after any existing entries of x.

    insort == insort_right
    """
    a = [10, 20, 30]
    insort_right(a, 30)
    assert a == [10, 20, 30, 30]
