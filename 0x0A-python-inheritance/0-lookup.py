#!/usr/bin/python3

"""
This module contains one function Lookup
"""


def lookup(obj):
    """
    this function returns the list of available attrubutes and methods
    of an object
    Args:
        obj: the object to find attributes of
    """
    list_new = [attr for attr in dir(obj)]

    return (list_new)
