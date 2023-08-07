0x07-python-test_driven_development

Learning Objectives

    • Why Python programming is awesome
    • What’s an interactive test
    • Why tests are important
    • How to write Docstrings to create tests
    • How to write documentation for each module and function
    • What are the basic option flags to create tests
    • How to find edge cases


Files

    • 0-add_integer.py - a function that adds 2 integers.
        ◦ Prototype: def add_integer(a, b=98):
        ◦ a and b must be integers or floats, otherwise raise a TypeError exception with the message a must be an integer or b must be an integer
        ◦ a and b must be first casted to integers if they are float
        ◦ Returns an integer: the addition of a and b
        ◦ You are not allowed to import any module
          
    • 2-matrix_divided.py, tests/2-matrix_divided.txt - a function that divides all elements of a matrix.
        ◦ Prototype: def matrix_divided(matrix, div):
        ◦ matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception with the message matrix must be a matrix (list of lists) of integers/floats
        ◦ Each row of the matrix must be of the same size, otherwise raise a TypeError exception with the message Each row of the matrix must have the same size
        ◦ div must be a number (integer or float), otherwise raise a TypeError exception with the message div must be a number
        ◦ div can’t be equal to 0, otherwise raise a ZeroDivisionError exception with the message division by zero
        ◦ All elements of the matrix should be divided by div, rounded to 2 decimal places
        ◦ Returns a new matrix
        ◦ You are not allowed to import any module
          
    • 3-say_my_name.py, tests/3-say_my_name.txt - a function that prints My name is <first name> <last name>
    • 4-print_square.py, tests/4-print_square.txt - a function that prints a square with the character #.
    • 5-text_indentation.py, tests/5-text_indentation.txt - a function that prints a text with 2 new lines after each of these characters: ., ? and :
    • tests/6-max_integer_test.py - this task contains unittests for the function def max_integer(list=[]):
        ◦ Your test file should be inside a folder tests
        ◦ You have to use the unittest module
        ◦ Your test file should be python files (extension: .py)
        ◦ Your test file should be executed by using this command: python3 -m unittest tests.6-max_integer_test
        ◦ All tests you make must be passable by the function below

    • 
