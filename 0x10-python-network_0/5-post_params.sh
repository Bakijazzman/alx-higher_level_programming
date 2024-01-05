#!/usr/bin/bash
# Script that takes a url, sends a POST request
# and displays the body of the response
curl -s -X POST "subject=I will always be here for PLD&email=test@gmail.com" "$1"
