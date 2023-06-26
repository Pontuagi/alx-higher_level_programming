#!/usr/bin/python3

"""
this module contains one class MyList
"""


class MyList(list):
    """
    this class inherits from list
    """
    def print_sorted(self):
        """
        this method prints the list
        """
        sorted_list = sorted(self)
        print(sorted_list)
