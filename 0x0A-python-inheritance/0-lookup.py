#!/usr/bin/python3
"""
Lookup module for all available attributes and methods of an object
"""


def lookup(obj):
    """
        This function returns the list of available attributes and methods
        of an object
    """
    return (dir(obj))
