#!/usr/bin/python3
""" Module that open, read and write a file """


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns the number of char"""
    with open(filename, 'w', encoding='utf-8') as f:
        return (f.write(text))
