#!/usr/bin/python3
"""
Module that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    The method to search through the array of integers
    """
    if bool(list_of_integers) is False:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
