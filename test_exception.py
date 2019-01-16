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


def test_exception():
    try:
        1 / 0
    except Exception as e:
        assert '{}'.format(e) == 'division by zero'
        assert type(e).__module__ == 'builtins'
        assert type(e).__name__ == 'ZeroDivisionError'
