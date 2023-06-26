#!/usr/bin/python3

"""
this module contains one class MyList
it also imports the test file
"""
import doctest


class MyList(list):
    """
    this class inherits from list
    """
    def print_sorted(self):
        """
        this method prints the list in sorted order
        """
        sorted_list = sorted(self)
        print(sorted_list)


"""
This imports the test file for the class
"""
doctest.testfile("tests/1-my_list.txt")
