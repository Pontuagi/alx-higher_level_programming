#!/usr/bin/python3

"""
This module contains a single script
It fetches a url
"""

import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body_bytes = response.read()
        body_str = body_bytes.decode("utf-8")

        print("Body response:")
        print("    - type:", type(body_bytes))
        print("    - content:", repr(body_bytes))
        print("    - utf8 content:", body_str)
