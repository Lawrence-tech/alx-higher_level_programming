#!/usr/bin/python3
"""Program that writes an Object to a text file using json representaion """
import json


def save_to_json_file(my_obj, filename):
    """Function that writes an Object to a text file using json rep """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
