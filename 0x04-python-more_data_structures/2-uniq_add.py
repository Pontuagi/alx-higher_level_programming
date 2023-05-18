#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_no = list(set(my_list))
    sum_uniq = 0
    for i in unique_no:
        sum_uniq += i
    return sum_uniq
