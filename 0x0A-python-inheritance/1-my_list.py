#!/usr/bin/python3
"""Import modules here """


class MyList(list):
    """class that inherits from list"""
    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
