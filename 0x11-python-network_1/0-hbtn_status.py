#!/usr/bin/python3
"""Import modules here"""
import urllib.request as request


if __name__ == "__main__":
    request1 = request.Request("https://alx-intranet.hbtn.io/status")
    with request.urlopen(request1) as response:
        body = response.read()
        print("Body response")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
