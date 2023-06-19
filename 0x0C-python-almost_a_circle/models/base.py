#!/usr/bin/python3

"""
This module contains one class Base
"""


class Base:
    """
    This class Base has one private attribute
    Attrubutes:
        __nb_objects: initialized to 0. counts objects with no Id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        This method initialises id.
        Increment __nb_objects if id is None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
