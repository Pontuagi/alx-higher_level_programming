#!/usr/bin/python3

"""
A Python script that takes 2 arguments
Lists 10 commits (from the most recent to oldest) of the repository
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository_name> <owner_name>")
    else:
        repo_name = sys.argv[1]
        owner_name = sys.argv[2]

        url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

        # Send a GET request to the GitHub API
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            commits = response.json()[:10]  # Get the first 10 commits
            for commit in commits:
                sha = commit['sha']
                author_name = commit['commit']['author']['name']
                print(f"{sha}: {author_name}")
        else:
            print(f"Error: Cannot fetch commits. Code: {response.status_code}")
