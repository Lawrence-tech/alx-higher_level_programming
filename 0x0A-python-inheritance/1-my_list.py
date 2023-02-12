#!/usr/bin/python3
"""
Module that sorts a list int
"""


class Mylist(list):
    """
    Class that inherits from list
    """
    def print_sorted(self):
        """ prints the list, but sorted (ascending sort) """
        new_list = self[:]
        new_list.sort()
        print(new_list)
