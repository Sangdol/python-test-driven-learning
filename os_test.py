import os


# https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
def test_getcwd():
    assert os.getcwd().split('/')[-1] == 'python-test-driven-learning'