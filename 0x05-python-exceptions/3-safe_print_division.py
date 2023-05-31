#!/usr/bin/python3
def safe_print_division(a, b):
    divide = None
    try:
        divide = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(divide))
        return divide
