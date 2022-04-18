"""

pytest doctest: https://docs.pytest.org/en/latest/doctest.html

>>> three()
3
"""

import numpy as np


def arange():
    """
    >>> a = np.arange(10)
    >>> len(a)
    10
    """
    pass


def three():
    """
    >>> three()
    3
    """
    return 3


if __name__ == "__main__":
    import doctest
    doctest.testmod()
