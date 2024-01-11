#!/usr/bin/python3
"""Import Modules here """
import urllib.request
from sys import argv


if __name__ == "__main__":
    if len(argv) > 2:
        data = urllib.parse.urlencode({"email": argv[2]}).encode("ascii")
        req = urllib.request.Request(argv[1], data)
        with urllib.request.urlopen(req) as response:
            body = response.read()
            print(body.decode('utf-8'))
