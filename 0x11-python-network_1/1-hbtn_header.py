#!/usr/bin/python3

"""
A pyhton script to display url value
"""

import urllib.request
import sys


def get_x_request_id(url):
    """
    Script sends a request to url
    displays the value of the X-Request-Id
    """
    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.getheader('X-Request-Id')
            if x_request_id:
                print(f"{x_request_id}")
            else:
                print("X-Request-Id not found")

    except urllib.error.URLError as e:
        print("Error:", e)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
    else:
        url = sys.argv[1]
        get_x_request_id(url)
