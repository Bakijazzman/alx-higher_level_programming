#!/usr/bin/python3
"""Import Modules Here"""
from sys import argv
import urllib.request as request


if __name__ == "__main__":
    url = argv[1]
    with request.urlopen(url) as response:
        body = response.getheader("X-Request-Id")
        print(f"{body}")
