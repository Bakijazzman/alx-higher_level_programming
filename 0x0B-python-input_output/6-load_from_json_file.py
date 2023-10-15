#!/usr/bin/python3
"""Import modules here """
import json


def load_from_json_file(filename):
    """creates an object from a json file"""
    with open(filename, 'r', encoding="utf-8") as files:
        return json.load(files)
