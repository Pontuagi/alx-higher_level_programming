#!/bin/bash
# Accepts a URL, sends a GET request to it and idsplays the body of the responce
curl -s -o /dev/null -w "%{http-code}" "$1" || [ "$(cat)" = "200" ] && curl -s "$1"
