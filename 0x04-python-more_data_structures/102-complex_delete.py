#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is None:
        return
    for x, y in list(a_dictionary.items()):
        if y == value:
            del a_dictionary[x]
    return a_dictionary
