#!/usr/bin/bash
# A script that takes a url and sends a request to the url
# Also diisplays tthe size of tthe body of the response
curl -w "%{size_download}\n" "$1" -so /dev/null
