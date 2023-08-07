0x0C-python-almost_a_circle

Learning Objectives:

    • What is Unit testing and how to implement it in a large project
    • How to serialize and deserialize a Class
    • How to write and read a JSON file
    • What is *args and how to use it
    • What is **kwargs and how to use it
    • How to handle named arguments in a function

Files:

    1. models/base.py, models/__init__.py -  the first class Base:
        ◦ Create a folder named models with an empty file __init__.py inside - with this file, the folder will become a Python package
        ◦ Create a file named models/base.py:
        ◦ Class Base:
            ▪ private class attribute __nb_objects = 0
            ▪ class constructor: def __init__(self, id=None)::
                • if id is not None, assign the public instance attribute id with this argument value - you can assume id is an integer and you don’t need to test the type of it
                • otherwise, increment __nb_objects and assign the new value to the public instance attribute id
        ◦ This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)
    2. models/rectangle.py - the class Rectangle that inherits from Base
        ◦ In the file models/rectangle.py
        ◦ Class Rectangle inherits from Base
        ◦ Private instance attributes, each with its own public getter and setter:
            ▪ __width -> width
            ▪ __height -> height
            ▪ __x -> x
            ▪ __y -> y
        ◦ Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
            ▪ Call the super class with id - this super call with use the logic of the __init__ of the Base class
            ▪ Assign each argument width, height, x and y to the right attribute
    3. models/rectangle.py - pdate the class Rectangle by adding validation of all setter methods and instantiation (id excluded)
        ◦ If the input is not an integer, raise the TypeError exception with the message: <name of the attribute> must be an integer. Example: width must be an integer
        ◦ If width or height is under or equals 0, raise the ValueError exception with the message: <name of the attribute> must be > 0. Example: width must be > 0
        ◦ If x or y is under 0, raise the ValueError exception with the message: <name of the attribute> must be >= 0. Example: x must be >= 0
    4. models/rectangle.py - Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.
    5. models/rectangle.py - Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here.
    6. models/rectangle.py - Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
    7. models/rectangle.py - Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y
    8. models/rectangle.py - Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute:
        ◦ 1st argument should be the id attribute
        ◦ 2nd argument should be the width attribute
        ◦ 3rd argument should be the height attribute
        ◦ 4th argument should be the x attribute
        ◦ 5th argument should be the y attribute
    9. models/rectangle.py - Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes
    10. models/square.py - the class Square that inherits from Rectangle
    11. models/square.py - Update the class Square by adding the public getter and setter size
    12. models/square.py - Update the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes
    13. models/rectangle.py - Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle
    14. models/square.py - Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square:
    15. models/base.py - Update the class Base by adding the static method def to_json_string(list_dictionaries): that returns the JSON string representation of list_dictionaries: 
    16. models/base.py - Update the class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file:
    17. models/base.py - Update the class Base by adding the static method def from_json_string(json_string): that returns the list of the JSON string representation json_string:
    18. models/base.py - Update the class Base by adding the class method def create(cls, **dictionary): that returns an instance with all attributes already set:
    19. models/base.py - Update the class Base by adding the class method def load_from_file(cls): that returns a list of instances:
    20. models/ - Update the class Base by adding the class methods def save_to_file_csv(cls, list_objs): and def load_from_file_csv(cls): that serializes and deserializes in CSV:
    21. models/base.py - Update the class Base by adding the static method def draw(list_rectangles, list_squares): that opens a window and draws all the Rectangles and Squares:
