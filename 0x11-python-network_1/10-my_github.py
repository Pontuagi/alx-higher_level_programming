#!/usr/bin/python3

"""
A script that takes Github credentials
Uses github api to display your id
"""

import requests
import sys
from requests.auth import HTTPBasicAuth


def get_github_user_id(username, access_token):
    """ A function to fetch github id """
    url = f"https://api.github.com/user"

    try:
        response = requests.get(
            url, auth=HTTPBasicAuth(username, access_token)
            )
        if response.status_code == 200:
            user_data = response.json()
            user_id = user_data["id"]
            print(f"{user_id}")
        else:
            print("None")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    username = sys.argv[1]
    access_token = sys.argv[2]
    get_github_user_id(username, access_token)
