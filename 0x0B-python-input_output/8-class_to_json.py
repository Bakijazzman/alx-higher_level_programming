#!/usr/bin/python3
"""import modules here """


def class_to_json(obj):
    """returns the dictionary descrption of a simple data """
    return obj.__dict__
