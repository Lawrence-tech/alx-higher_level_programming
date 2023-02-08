#!/usr/bin/python3
""" Program that read a text file """


def read_file(filename=""):
    """ function that reads a text file (UTF*) and prints it to stdout """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')
