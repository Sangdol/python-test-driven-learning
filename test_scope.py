def test_closure():
    """Any function that has free variables that are not global vairables is a closure.

    free variable - a variable used in a function, which is neither a formal parameter
        to the function nor defined in the functions body

    Refer to https://stackoverflow.com/questions/4020419/why-arent-python-nested-functions-called-closures
    """
    def counter():
        count = 0

        def increase():
            nonlocal count
            count += 1
            return count

        return increase

    inc = counter()
    assert inc() == 1
    assert inc() == 2

    # about cell and __closure__ https://docs.python.org/3/reference/datamodel.html
    assert not counter.__closure__  # it has the attribute but empty.
    assert inc.__closure__  # tuples of cell
    assert inc.__closure__[0].cell_contents == 2


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
