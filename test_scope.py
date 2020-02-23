global_abc = 1


def test_global_error():
    try:
        global_abc += 2
    except UnboundLocalError as e:
        assert str(e) == "local variable 'global_abc' referenced before assignment"


def test_global_keyword():
    global global_abc
    global_abc += 2

    assert global_abc == 3


def test_non_local():
    local_var = 1

    def no_nonlocal():
        local_var = 2
        return local_var

    no_nonlocal()
    assert local_var == 1

    def with_nonlocal():
        nonlocal local_var
        local_var = 2
        return local_var

    with_nonlocal()
    assert local_var == 2


def test_for_var():
    a = [1, 2, 3]

    for i, n in enumerate(a):
        pass

    assert i == 2   # interesting. it's not 3.
    assert n == 3
