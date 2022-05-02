"""import tests

You can access imported module directly for `import import_test`
but you need `as` to access the imported module in a package.
"""
import stub.package_test_add as test_add
import import_test


def test_global_variable():
    assert import_test.global_variable == 1

    import_test.global_variable = 2
    assert import_test.global_variable == 2


def test_global_variable_2():
    # The global variable is back to 1 after the previous test.
    assert import_test.global_variable == 1


def test_import():
    assert test_add.add(1, 2) == 3


def test_import_in_root():
    assert import_test.hello() == 'hello'
