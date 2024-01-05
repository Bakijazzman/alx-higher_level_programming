#!/usr/bin/bash
# A script that sends a delete request to the URL passed in
# and the first arguement displays the body of the response
curl -sX DELETE "$1"
