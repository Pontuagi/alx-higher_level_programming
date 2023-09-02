#!/usr/bin/python3

"""
A script that takes in a URL and displays the body of response
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    response_code = response.status_code
    response_body = response.text

    print("Body response:")
    print("    - type:", type(response_body))
    print("    - content:", repr(response_body))
    print("    - utf8 content:", response_body)

    if response_code >= 400:
        print(f"Error code: {response_code}")
