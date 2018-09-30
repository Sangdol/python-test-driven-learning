def file():
    return open('stub/plain.txt', 'r')


# https://www.digitalocean.com/community/tutorials/how-to-handle-plain-text-files-in-python-3
def test_file_read():
    assert file().read() == 'abc\n123\nABC\n'
    assert file().readline() == 'abc\n'
    assert file().readlines() == ['abc\n', '123\n', 'ABC\n']


# https://stackoverflow.com/questions/15233340/getting-rid-of-n-when-using-readlines
def test_file_read_without_newline():
    assert file().read().splitlines() == ['abc', '123', 'ABC']
    assert [line.rstrip() for line in file()] == ['abc', '123', 'ABC']
