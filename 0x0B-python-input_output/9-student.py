#!/usr/bin/python3
"""Import Modules Here """


class Student:
    """no private attributes recorded"""

    def __init__(self, first_name, last_name, age):
        """initializing attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves dictionary representation of instance """
        return self.__dict__
