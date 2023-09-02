#!/usr/bin/python3

"""
A script that sends a POST request to http://0.0.0.0:5000/search_user
with the given letter as a parameter and processes the response.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': letter}

    try:
        response = requests.post(url, data=data)
        response_json = response.json()

        if response_json:
            if "id" in response_json and "name" in response_json:
                print(
                      "[{}] {}".format(
                          response_json["id"], response_json["name"])
                      )
            else:
                print("Not a valid JSON")
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
    except Exception as e:
        print("Error:", e)
