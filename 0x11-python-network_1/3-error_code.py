#!/usr/bin/python3
"""Import Modules Here """
from sys import argv
from urllib.error import HTTPError
from urllib.request import urlopen, Request


if __name__ == "__main__":
    try:
        with urlopen(Request(argv[1])) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except HTTPError as exception:
        print("Error code:", exception.code)
