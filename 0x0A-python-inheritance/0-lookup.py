#!/usr/bin/python3
def lookup(obj):
    """function to look up attributes and modules
        Args:
        obj: the object to lookup
        Return: list of available attributes and modules
    """
    return dir(obj)
