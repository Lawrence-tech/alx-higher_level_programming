#!/usr/bin/python3
"""
Module that sorts a list int
"""


class my_list(list):
    """Class that inherits from list """
    def print_sorted(self):
        """ prints the list, but sorted (ascending sort) """
        n_list = self[:]
        n_list.sort()
        print(n_list)
