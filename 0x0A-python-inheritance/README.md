0x0A-python-inheritance

Learning Objectives:

    • Why Python programming is awesome
    • What is a superclass, baseclass or parentclass
    • What is a subclass
    • How to list all attributes and methods of a class or instance
    • When can an instance have new attributes
    • How to inherit class from another
    • How to define a class with multiple base classes
    • What is the default class every class inherit from
    • How to override a method or attribute inherited from the base class
    • Which attributes or methods are available by heritage to subclasses
    • What is the purpose of inheritance
    • What are, when and how to use isinstance, issubclass, type and super built-in functions

Files:

0-lookup.py - a function that returns the list of available attributes and methods of an object:
1-my_list.py - a class MyList that inherits from list
2-is_same_class.py -  a function that returns True if the object is exactly an instance of the specified class ; otherwise False
3-is_kind_of_class.py - a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.
4-inherits_from.py - a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False
5-base_geometry.py - an empty class BaseGeometry.
6-base_geometry.py -  a class BaseGeometry (based on 5-base_geometry.py).
7-base_geometry.py - a class BaseGeometry (based on 6-base_geometry.py).
8-rectangle.py - a class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
9-rectangle.py - a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)
10-square.py - a class Square that inherits from Rectangle (9-rectangle.py):
11-square.py - a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).
100-my_int.py - a class MyInt that inherits from int:
101-add_attribute.py - a function that adds a new attribute to an object if it’s possible:
