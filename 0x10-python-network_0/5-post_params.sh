#!/bin/bash
# Takes in a URL sends POST request and display body of the response
curl -s -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
