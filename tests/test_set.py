"""set tests
"""

def test_difference_set():
    a = {1, 2, 3}
    b = {2, 3, 4}

    assert a.difference(b) == {1}
    assert a - b == {1}


def test_intersection_of_sets():
    a = {1, 2, 3}
    b = {2, 3, 4}

    assert a.intersection(b) == {2, 3}
    assert a & b == {2, 3}


def test_union_of_sets():
    a = {1, 2, 3}
    b = {2, 3, 4}

    assert a.union(b) == {1, 2, 3, 4}
    assert a | b == {1, 2, 3, 4}


def test_symmetric_difference_of_sets():
    a = {1, 2}
    b = {2, 3}

    assert a.symmetric_difference(b) == {1, 3}
    assert a ^ b == {1, 3}


def test_contains_set():
    a = {1, 2, 3}
    b = {2, 3}

    assert a >= b
    assert not a <= b

