#!/usr/bin/python3

"""
Integers ``addition`` module.
"""


def add_integer(a, b=98):
    """Calculate the sum of ``a`` and ``b``.

    Args:
        a: First parameter
        b: Second parameter
    Raises:
        TypeError: If a or b is neither integer nor float.
    Notes:
        Float parameters are cast into integers.
    """
    if type(a) is not int:
        if type(a) is float:
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    if type(b) is not int:
        if type(b) is float:
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    return a + b
