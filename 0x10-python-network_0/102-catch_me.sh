#!/bin/bash
# makes a request to "0.0.0.0:5000/catch_me" causing the server to respond "You got me!"
curl -sX PUT -d "user_id=98" 0.0.0.0:5000/catch_me | grep -o "You got me!"
