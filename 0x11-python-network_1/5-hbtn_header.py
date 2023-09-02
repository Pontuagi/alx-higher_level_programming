#!/usr/bin/python3

"""
A script that takes a URL
Sendsa request to It
Displays the value of the variable X-Request-Id in the response header
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        response = requests.get(url)
        x_request_id = response.headers.get('X-Request-Id')

        if x_request_id:
            print(x_request_id)

    except requests.exceptions.RequestException as e:
        print("Error:", e)
