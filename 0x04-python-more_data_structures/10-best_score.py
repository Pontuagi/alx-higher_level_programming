#!/usr/bin/python3
def best_score(a_dictionary):
    max_val = float('-inf')
    for value in a_dictionary.value():
        if value > max_val:
            max_val = value
    return max_val
