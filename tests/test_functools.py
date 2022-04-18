import functools


def test_reduce():
    ab = 'ab'
    cd = 'cd'

    # product
    assert functools.reduce(
        lambda acc, ch: [a + c for a in acc for c in ch],
        [ab, cd]) == ['ac', 'ad', 'bc', 'bd']

    # It's okay to not passing the initial value
    assert functools.reduce(
        lambda acc, ch: [a + c for a in acc for c in ch],
        [ab, cd], ['']) == ['ac', 'ad', 'bc', 'bd']

    # This is unexpected.
    assert functools.reduce(
        lambda acc, ch: [a + c for a in acc for c in ch],
        [ab]) == 'ab'

    # This is better.
    assert functools.reduce(
        lambda acc, ch: [a + c for a in acc for c in ch],
        [ab], ['']) == ['a', 'b']