#/bin/bash
# Accepts a URL, sends a request to it and display size of the body of response
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
