import stub.package_test_add as test_add


# importing correctly with pytest
# https://stackoverflow.com/questions/25827160/importing-correctly-with-pytest
def test_import():
    assert test_add.add(1, 2) == 3

