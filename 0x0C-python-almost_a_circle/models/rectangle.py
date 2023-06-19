#!/usr/bin/python3


"""
This modules contain one class Rectangle
"""

from models.base import Base


class Rectangle(Base):
    """
    inherits from class Base
    Attributes:
        __width: widht of the rectangle
        __height: height of rectangle
        __x: x coordinate of rectangle
        __y: y coordinate of reactangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor for class Rectangle """
        super().__init__(id)

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height muct be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ return the private attribute width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """ set width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Retrive the value of height """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ set the height value """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ return the value of x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """ set the value of x """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        else:
            self.__x = value

    @property
    def y(self):
        """ get the value of y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """ set the value of y """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area of the rectangle """
        return (self.__width * self.__height)

    def display(self):
        """ Display the rectangle """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """ print the Rectangle"""
        new_str = f'[Rectangle] ({self.id}) {self.__x}/{self.__y}'
        new_str += f' - {self.__width}/{self.__height}'
        return (new_str)

    def update(self, *args, **kwargs):
        """ assign an argument to each attribute"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
