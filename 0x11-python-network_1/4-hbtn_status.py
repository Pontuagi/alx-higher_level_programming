#!/usr/bin/python3

"""
A script that fetches https://alx-intranet.hbtn.io/status
It uses the requests packages
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    try:
        response = requests.get(url)
        response_type = type(response.text).__name__
        response_content = response.text
        print("Body response:")
        print("    - type:", type(response_type))
        print("    - content:", repr(response_content))

    except requests.exceptions.RequestException as e:
        print("Error:", e)
