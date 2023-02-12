#!/usr/bin/python3
"""a function that returns a class's serializable dict elements"""


def class_to_json(obj):
    """Function that returns the dictionary description with simple data
    structure (list, dictionary, string, integer and boolean) for JSON
    serialization of an object """
    retdict = {}
    objdict = obj.__dict__
    for ele in objdict:
        if type(objdict[ele] in [list, dict, str, int, bool]:
                retdict[ele] = objdict[ele]
    return retdict
