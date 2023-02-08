#!/usr/bin/python3
""" Module that writes a string to a text file  and return written char no """


def write_file(filename="", text=""):
    """ returns number of lines of a text file """
    count = 0
    with open(filename) as f:
        for line in f:
            count += 1
    return (count)
