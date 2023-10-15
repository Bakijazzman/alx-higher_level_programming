#!/usr/bin/python3
"""Import modules here """
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a file """
    with open(filename, 'w', encoding="utf-8") as files:
        json.dump(my_obj, files)
