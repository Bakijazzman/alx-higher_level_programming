#!/usr/bin/bash
#A script that displays only the status code of an HTTP request
curl -w "%{http_code}" "$1" -so /dev/null
