#!/bin/bash
# A bash script that makes a request to 0.0.0.0:5000 curl url till we get "You got me!"
curl -sL http://0.0.0.0:5000/catch_me -X PUT -d "user_id=98" -H "Origin: HolbertonSchool"