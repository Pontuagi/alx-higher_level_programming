0x04-python-more_data_structures

Learning Objectives:

    • Why Python programming is awesome
    • What are sets and how to use them
    • What are the most common methods of set and how to use them
    • When to use sets versus lists
    • How to iterate into a set
    • What are dictionaries and how to use them
    • When to use dictionaries versus lists or sets
    • What is a key in a dictionary
    • How to iterate over a dictionary
    • What is a lambda function
    • What are the map, reduce and filter functions


Files:

    • 0-square_matrix_simple.py -  a function that computes the square value of all integers of a matrix.
        ◦ Prototype: def square_matrix_simple(matrix=[]):
        ◦ matrix is a 2 dimensional array
        ◦ Returns a new matrix:
            ▪ Same size as matrix
            ▪ Each value should be the square of the value of the input
        ◦ Initial matrix should not be modified
        ◦ You are not allowed to import any module
        ◦ You are allowed to use regular loops, map, etc.
          
    • 1-search_replace.py -  a function that replaces all occurrences of an element by another in a new list.
        ◦ Prototype: def search_replace(my_list, search, replace):
        ◦ my_list is the initial list
        ◦ search is the element to replace in the list
        ◦ replace is the new element
        ◦ You are not allowed to import any module
    • 2-uniq_add.py - a function that adds all unique integers in a list (only once for each integer).
    • 3-common_elements.py - a function that returns a set of common elements in two sets.
    • 4-only_diff_elements.py - a function that returns a set of all elements present in only one set.
    • 5-number_keys.py - a function that returns the number of keys in a dictionary.
    • 6-print_sorted_dictionary.py - a function that prints a dictionary by ordered keys.
    • 7-update_dictionary.py - a function that replaces or adds key/value in a dictionary.
    • 8-simple_delete.py - a function that deletes a key in a dictionary.
    • 9-multiply_by_2.py -  a function that returns a new dictionary with all values multiplied by 2
    • 10-best_score.py - a function that returns a key with the biggest integer value.
    • 11-multiply_list_map.py - a function that returns a list with all values multiplied by a number without using any loops.
    • 12-roman_to_int.py - a function def roman_to_int(roman_string): that converts a Roman numeral to an integer.
        ◦ You can assume the number will be between 1 to 3999.
        ◦ def roman_to_int(roman_string) must return an integer
        ◦ If the roman_string is not a string or None, return 0
