#!/bin/bash
# Sends request to a URL passed and argument and displays the status code of responce
curl -s -o /dev/null -w "%{http_code}" "$1"
