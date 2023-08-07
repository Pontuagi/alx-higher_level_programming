0x0B-python-input_output

Learning Objectives:

    • Why Python programming is awesome
    • How to open a file
    • How to write text in a file
    • How to read the full content of a file
    • How to read a file line by line
    • How to move the cursor in a file
    • How to make sure a file is closed after using it
    • What is and how to use the with statement
    • What is JSON
    • What is serialization
    • What is deserialization
    • How to convert a Python data structure to a JSON string
    • How to convert a JSON string to a Python data structure

Files:

    • 0-read_file.py - a function that reads a text file (UTF8) and prints it to stdout:
    • 1-write_file.py -  a function that writes a string to a text file (UTF8) and returns the number of characters written
    • 2-append_write.py - a function that appends a string at the end of a text file (UTF8) and returns the number of characters added
    • 3-to_json_string.py - a function that returns the JSON representation of an object (string)
    • 4-from_json_string.py - a function that returns an object (Python data structure) represented by a JSON string
    • 5-save_to_json_file.py - a function that writes an Object to a text file, using a JSON representation
    • 6-load_from_json_file.py - a function that creates an Object from a “JSON file”
    • 7-add_item.py- a script that adds all arguments to a Python list, and then save them to a file
    • 8-class_to_json.py - a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object
    • 9-student.py - a class Student that defines a student by
        ◦ Public instance attributes:
            ▪ first_name
            ▪ last_name
            ▪ age
        ◦ Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
        ◦ Public method def to_json(self): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py)
    • 10-student.py - a class Student that defines a student by: (based on 9-student.py)
        ◦ Public instance attributes:
            ▪ first_name
            ▪ last_name
            ▪ age
        ◦ Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
        ◦ Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
        ◦ If attrs is a list of strings, only attribute names contained in this list must be retrieved.
        ◦ Otherwise, all attributes must be retrieved
    • 11-student.py - a class Student that defines a student by: (based on 10-student.py)
        ◦ Public instance attributes:
            ▪ first_name
            ▪ last_name
            ▪ age
        ◦ Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
        ◦ Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
            ▪ If attrs is a list of strings, only attributes name contain in this list must be retrieved.
            ▪ Otherwise, all attributes must be retrieved
        ◦ Public method def reload_from_json(self, json): that replaces all attributes of the Student instance:
            ▪ You can assume json will always be a dictionary
            ▪ A dictionary key will be the public attribute name
            ▪ A dictionary value will be the value of the public attribute
        ◦ You are not allowed to import any module
    • 12-pascal_triangle.py - a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n
        ◦ Returns an empty list if n <= 0
        ◦ You can assume n will be always an integer
        ◦ You are not allowed to import any module
    • 100-append_after.py - a function that inserts a line of text to a file, after each line containing a specific string (see example)
        ◦ Prototype: def append_after(filename="", search_string="", new_string=""):
        ◦ You must use the with statement
        ◦ You don’t need to manage file permission or file doesn't exist exceptions.
        ◦ You are not allowed to import any module
    • 101-stats.py - a script that reads stdin line by line and computes metrics
        ◦ Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
        ◦ Each 10 lines and after a keyboard interruption (CTRL + C), prints those statistics since the beginning:
            ▪ Total file size: File size: <total size>
            ▪ where is the sum of all previous (see input format above)
            ▪ Number of lines by status code:
                • possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
                • if a status code doesn’t appear, don’t print anything for this status code
                • format: <status code>: <number>
                • status codes should be printed in ascending order



