#!/usr/bin/python3
"""imprts module here """


class MyInt(int):
    """class that inherits from int """
    def __eq__(self, other):
        """Equal is reversed to !="""
        return int(self) != int(other)

    def __ne__(self, other):
        """Not equal is reversed to =="""
        return int(self) == int(other)
