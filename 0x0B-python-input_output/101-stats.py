#!/usr/bin/python3

"""this script contains two functions
the module reads input from stdin, computes metrics
and pints the statistics
"""

import sys
from collections import defaultdict


def comput_metrics():
    """
    this function takes input from stdin line by line
    It then computes the metrics
    """
    total_file_size = 0
    status_code_count = defaultdict(int)

    try:
        line_count = 0
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            ip_address, _, _, status_code, file_size = line.split(" ")[0],\
            line.split(" ")[-4], line.split(" ")[-3], line.split(" ")[-2],\
            line.split(" ")[-1]

            total_file_size += int(file_size)
            status_code_count[status_code] += 1

            line_count += 1
            if line_count % 10 == 0:
                print_stat(total_file_size, status_code_count)
    except KeyboardInterrupt:
        print_stat(total_file_size, status_code_count)


def print_stat(total_file_size, status_code_count):
    """
    this funtion prints the statistics since the beginning
    Args:
        total_file_size (int): the size of the file
        status_code_count (defaultdict): dictionary containing the status code count
    """
    print("File size:", total_file_size)
    for status_code in sorted(status_code_count.keys()):
        count = status_code_count[status_code]
        print(status_code + ":", count)


comput_metrics()
