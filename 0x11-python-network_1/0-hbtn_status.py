#!/usr/bin/python3

"""
This module contains a single script
It fetches a url
"""

import urllib.request


def fetch_status():
    """
    Function to fetch a url
    Uses the package urllib
    """
    url = "https://alx-intranet.hbtn.io/status"
    try:
        with urllib.request.urlopen(url) as response:
            body_bytes = response.read()
            body_str = body_bytes.decode("utf-8")

            print("Body response:")
            print("    - type:", type(body_bytes))
            print("    - content:", repr(body_bytes))
            print("    - utf8 content:", body_str)

    except urllib.error.URLError as e:
        print("Error:", e)


if __name__ == "__main__":
    fetch_status()
