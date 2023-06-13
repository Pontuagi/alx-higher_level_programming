#!/usr/bin/python3

"""
This file contains one function
The function writes a string to a text file
it returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    This function writes a string to a text file(UTf8)
    It return the characters written

    Args:
        filename (file): the file to write into
        text (str): the text to write to the file

    Return:
        Characters written
    """
    with open(filename, 'w', encoding='UTF8') as file_b:
        file_b.write(text)
        characters = file_b.tell()

    return (characters)
