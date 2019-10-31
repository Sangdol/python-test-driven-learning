import traceback
import sys


# https://docs.python.org/3/library/traceback.html#traceback-examples
def test_exc_info():
    """
    sys.exc_info() returns (type, value, traceback)
    """
    try:
        1 / 0
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()

        assert exc_type.__name__ == 'ZeroDivisionError'
        assert type(exc_value).__name__ == 'ZeroDivisionError'
        assert traceback.format_exception(
            exc_type, exc_value, exc_traceback)[0] == 'Traceback (most recent call last):\n'

    """
    traceback.format_exc() returns stacktrace
    """
    try:
        1 / 0
    except:
        formatted_lines = traceback.format_exc().splitlines()
        line1 = 'Traceback (most recent call last):'
        line2 = 'python-test-driven-learning/test_exception.py", line 24, in test_exc_info'
        line3 = '    1 / 0'
        line4 = 'ZeroDivisionError: division by zero'

        print(formatted_lines)

        assert formatted_lines[0] == line1
        assert line2 in formatted_lines[1]
        assert formatted_lines[2] == line3
        assert formatted_lines[3] == line4


def test_exception():
    try:
        1 / 0
    except Exception as e:
        assert '{}'.format(e) == 'division by zero'
        assert type(e).__module__ == 'builtins'
        assert type(e).__name__ == 'ZeroDivisionError'


def test_else():
    try:
        msg = 'hello'
    except IOError:
        msg = 'not this'
    else:
        msg = 'else'

    assert msg == 'else'
