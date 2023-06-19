#!/usr/bin/python3

"""
This module contains one class Base
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the Json string represantion of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string represantion of list_objs"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string(
            [obj.to_dictionary() for obj in list_objs]
            )
        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by json_string"""
        if json_string is None or json_string == '':
            return ([])
        return (json.loads(json_string))
