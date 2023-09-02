#!/usr/bin/python3

"""
A python script to display url value
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

    except urllib.error.URLError as e:
        print("Error:", e)


if __name__ == "__main__":
    url = sys.argv[1]
    get_x_request_id(url)
