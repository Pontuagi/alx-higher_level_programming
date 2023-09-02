#!/usr/bin/python3

"""
A script that takes in a URL
Sends a request to the URL
Displays the response (decoded in utf-8)
"""

import urllib.request
import urllib.error
import sys


def fetch_url_content(url):
    try:
        with urllib.request.urlopen(url) as response:
            body_bytes = response.read()
            body_str = body_bytes.decode("utf-8")

            print("    - type:", type(body_bytes))
            print("    - content:", repr(body_bytes))
            print("    - utf8 content:", body_str)

    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url_content(url)
