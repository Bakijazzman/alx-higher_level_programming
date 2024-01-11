#!/usr/bin/python3
"""Import Modues Here """
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    response = requests.post(url, data=value)
    print(response.text)
