#!/usr/bin/python3
"""Import Modules Here """
from sys import argv
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    a = ""
    if len(argv) > 1:
        a = {"q": argv[1][0]}
        response = requests.post(url, data=a)
        try:
            result = response.json()
            if result:
                print("[{}] {}".format(result.get("id"), result.get("name")))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
