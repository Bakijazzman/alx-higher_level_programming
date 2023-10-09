#!/usr/bin/python3
"""Imprts Module here """


def inherits_from(obj, a_class):
    """checks if object is an instancce of class that was inherited
    Args:
    obj: object given
    a_class: class given
    """
    obj_class = type(obj)

    if issubclass(obj_class, a_class) and obj_class != a_class:
        return True
    else:
        return False
