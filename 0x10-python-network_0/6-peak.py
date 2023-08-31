#!/usr/bin/python3

"""
This module contain one function
find_peak function
"""


def find_peak(list_of_integers):
    """
    A function that finds a peak on a list of unsorted integers
    """
    lowest = 0
    highest = len(list_of_integers) - 1

    while lowest < highest:
        mid = (lowest + highest) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            lowest = mid + 1
        else:
            highest = mid
    return list_of_integers[lowest] if list_of_integers else None
