"""
>>> three()
3
"""


def three():
    """
    >>> three()
    3
    """
    return 3


if __name__ == "__main__":
    import doctest
    doctest.testmod()
