#!/usr/bin/python3


"""
A script that take in a URL
Sends a post request to the URL with email a parameter
Displays body of responce
"""

import sys
import urllib.request
import urllib.parse


def send_post_request(url, email):
    """
    A function that sends post request to a URL
    and displays the body of response
    """
    try:
        # Preapare data for post request
        data_post = urllib.parse.urlencode({'email': email}).encode('utf-8')

        # Create post request
        req = urllib.request.Request(url, data=data_post, method='POST')

        # Send the POST request and retrieve the response
        with urllib.request.urlopen(req) as response:
            body_bytes = response.read()
            body_str = body_bytes.decode("utf-8")

            print(body_str)

    except urllib.error.URLError as e:
        print("Error:", e)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
