import stub.package_test_add as test_add
import import_test


def test_global_variable():
    assert import_test.global_variable == 1

    import_test.global_variable = 2
    assert import_test.global_variable == 2


# importing correctly with pytest
# https://stackoverflow.com/questions/25827160/importing-correctly-with-pytest
def test_import():
    assert test_add.add(1, 2) == 3


def test_import_in_root():
    assert import_test.hello() == 'hello'
