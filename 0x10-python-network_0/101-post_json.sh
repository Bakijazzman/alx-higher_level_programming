#!/usr/bin/bash
# A script that sends a json POST request to a url passed
# displays the body of the response
curl -s -d @"$2" -H "Content-Type: application/json" "$1" -X POST
