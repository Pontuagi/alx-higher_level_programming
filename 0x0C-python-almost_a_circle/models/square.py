#!/usr/bin/python3

"""
This module contains a class square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    this class Square inheits from class Rectangle
    Args:
        size: width or height of square
        x: x coordinate of Square
        y: y coordinate of square
        id: id of the instance
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ instantiate the variables"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the string represantation of Square"""
        new_str = f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
        return (new_str)

    @property
    def size(self):
        """getter for size"""
        return (self.width)

    @size.setter
    def size(self, value):
        """ set the value for size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
