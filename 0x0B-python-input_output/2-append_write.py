#!/usr/bin/python3

"""
this file contains one function
the function appends a string at the end of the file
It returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    This function appends a string to the end of a text file
    It returns the number of characters added

    Args:
        filename (str): the file to appent the text to
        text (str): the text to append to the file
    Return:
        Number of characters appended
    """
    with open(filename, 'a', encoding='UTF8') as file_c:
        pos_1 = file_c.tell()
        file_c.write(text)
        pos_2 = file_c.tell()

    return (pos_2 - pos_1)
