#!/bin/bash
# Takes URL a argument, sends a GET request to it and displayh body of the responce
curl -s -H "X-School-User-Id: 98" "$1"
