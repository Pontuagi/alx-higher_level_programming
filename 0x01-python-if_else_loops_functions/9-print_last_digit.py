#!/usr/bin/python3
def print_last_digit(number):
    """ print the last digit of a number"""
    number = abs(number)
    last_digit = number % 10
    print(last_digit, end="")

    return (last_digit)
