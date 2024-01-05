#!/usr/bin/bash
# Script that takes a url and displays all HTTP 
# methods the server will accept
curl -sI "$1" | grep Allow | cut -d ' ' -f2-
