#!/usr/bin/python3
"""Imports module here """
def is_same_class(obj, a_class):
    """checks if obj class is the same 
        Args:
        obj: to objectto check
        a_class: given class
    """
    return type(obj) == a_class
