#!/usr/bin/python3
"""Import Modules here """
from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    if len(argv) > 2:
        data = parse.urlencode({"email": argv[2]}).encode("ascii")
        req = request.Request(argv[1], data)
        with request.urlopen(req) as response:
            body = reponse.read()
            print(body.decode('utf-8'))
