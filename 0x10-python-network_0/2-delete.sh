#!/bin/bash
# Sends a DELETE request to the URL passed and first argument and display body of responce
curl -s -X DELETE "$1"
