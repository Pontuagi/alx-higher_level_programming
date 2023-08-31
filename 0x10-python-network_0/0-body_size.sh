#/bin/bash
# Accepts a URL, sends a request to it and display size of the body of response
curl -sI "$1" | wc -c
