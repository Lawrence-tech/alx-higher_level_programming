#!/usr/bin/python3
"""
    function that returns a class's serializable dict elements.
    """


def class_to_json(obj):
    """Function that returns the dictionary description with dict elements"""
    return (obj.__dict__)
