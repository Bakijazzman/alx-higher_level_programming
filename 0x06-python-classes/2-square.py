#!/usr/bin/python3
"""Defining a Square"""


class Square:
    """Square Class"""

    def __init__(self, size=0):
        """class instance

            Args:
                size: the size of the square

            Raises:
                TypeError: size must be an integer
                ValueError: size must be >= 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size of int must be >= 0")
        self.__size = size
