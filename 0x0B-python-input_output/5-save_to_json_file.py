#!/usr/bin/python3

"""
This file contains one function
The function writes an Object to a text file using JSON represantation
"""

import json


def save_to_json_file(my_obj, filename):
    """
    This function writes an object to a text file using json represantation

    Args:
        my_obj (str): object to be written to text file
        filename (str): the name of the file
    """
    with open(filename, 'w', encoding='UTF8') as file_d:
        json.dump(my_obj, file_d)
