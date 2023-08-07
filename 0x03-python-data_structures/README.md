0x03-python-data_structures

Learning Objectives:

    • What are lists and how to use them
    • What are the differences and similarities between strings and lists
    • What are the most common methods of lists and how to use them
    • How to use lists as stacks and queues
    • What are list comprehensions and how to use them
    • What are tuples and how to use them
    • When to use tuples versus lists
    • What is a sequence
    • What is tuple packing
    • What is sequence unpacking
    • What is the del statement and how to use it


Files:

    1. 0-print_list_integer.py - a function that prints all integers of a list.
    2. 1-element_at.py - a function that retrieves an element from a list like in C.
    3. 2-replace_in_list.py - a function that replaces an element of a list at a specific position (like in C).
    4. 3-print_reversed_list_integer.py - a function that prints all integers of a list, in reverse order.
    5. 4-new_in_list.py - a function that replaces an element in a list at a specific position without modifying the original list (like in C).
    6. 5-no_c.py - a function that removes all characters c and C from a string.
    7. 6-print_matrix_integer.py - a function that prints a matrix of integers.
    8. 7-add_tuple.py - a function that adds 2 tuples.
    9. 8-multiple_returns.py - a function that returns a tuple with the length of a string and its first character.
    10. 9-max_integer.py -  a function that finds the biggest integer of a list.
    11. 10-divisible_by_2.py - a function that finds all multiples of 2 in a list.
    12. 11-delete_at.py - a function that deletes the item at a specific position in a list.
    13. 12-switch.py - Complete the source code in order to switch value of a and b
    14. 13-is_palindrome.c, lists.h - a function in C that checks if a singly linked list is a palindrome.
        ◦ Prototype: int is_palindrome(listint_t **head);
        ◦ Return: 0 if it is not a palindrome, 1 if it is a palindrome
        ◦ An empty list is considered a palindrome
    15. 100-print_python_list_info.c -  C function that prints some basic info about Python lists.
        ◦ Prototype: void print_python_list_info(PyObject *p);
        ◦ Format: see example
        ◦ Python version: 3.4
        ◦ Your shared library will be compiled with this command line: gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c
        ◦ OS: Ubuntu 14.04 LTS

