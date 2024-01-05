#!/usr/bin/bash
# A script tahts takes a request and makes server write a message
curl -sL -d "user_id=98" "0.0.0.0:5000/catch_me" -H "Origin:HolbertonSchool" -X PUT
