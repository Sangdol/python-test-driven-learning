
def test_list_comprehension():
    assert list(map(lambda x: x ** 2, range(3))) == [0, 1, 4]
    assert [x ** 2 for x in range(3)] == [0, 1, 4]

    comb = [(x, y) for x in [1, 2] for y in [2, 3] if x != y]
    assert comb == [(1, 2), (1, 3), (2, 3)]

def test_for_if_any():
    numbers = ['1', '11', '111', '2', '22', '222']
    keys = ['1', '2']

    s = set()
    for n in numbers:
        for k in keys:
            if n.count(k) == 3:
                s.add(n)

    ss = {n for n in numbers if any(n.count(k) == 3 for k in keys)}

    assert s == ss