#!/usr/bin/python3
"""iImport modules here"""
import urllib.request as request


if __name__ == "__main__":
    request1 = request.Request("https://alx-intranet.hbtn.io/status")
    with request.urlopen(request1) as response:
        body = response.read()
        print("Body response")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")
