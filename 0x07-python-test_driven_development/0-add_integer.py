#!/usr/bin/python3

def add_integer(a, b=98):
    """ function that adds two integers
    Args:
        a (int or float): The first number.
        b (int or float, optional): the second number. Defaults to 98

    Raises:
        TypeError: If 'a' or 'b' is not an integer of float

    Return:
        int: The sum of 'a' anb 'b'
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return int(a + b)
