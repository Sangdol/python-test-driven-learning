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
        assert formatted_lines[0] == 'Traceback (most recent call last):'
        assert formatted_lines[1] == \
               '  File "/Users/slee/projects/python-test-driven-learning/test_exception.py", line 24, in test_exc_info'
        assert formatted_lines[2] == '    1 / 0', 'ZeroDivisionError: division by zero'


def test_exception():
    try:
        1 / 0
    except Exception as e:
        assert '{}'.format(e) == 'division by zero'
        assert type(e).__module__ == 'builtins'
        assert type(e).__name__ == 'ZeroDivisionError'
