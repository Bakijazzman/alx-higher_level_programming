#!/urs/bin/python3
"""Import Modules Here """
from sys import argv
import requests


if __name__ == "__main__":
    url = "https://api.github.com/user"
    response = request.get(url, auth=(argv[1], argv[2]))
    try:
        print(response.json().get("id"))
    except ValueError:
        print("Not a valid JSON")
