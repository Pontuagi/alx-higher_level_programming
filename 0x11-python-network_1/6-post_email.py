#!/usr/bin/python3

"""
A script that takes in a URL and email address
sends a POST request to the URL with email a parameter
Displays body of respose
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    response = requests.post(url, data=data)

    if response.status_code == 200:
        print(response.text)
