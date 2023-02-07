#!/usr/bin/python3
"""
Module that validates if an object belongs to a subclass
"""


def inherits_from(obj, a_class):
    """
    returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False.
    """
    if (type(obj) == a_class):
        return False
    return isinstance(obj, a_class)
