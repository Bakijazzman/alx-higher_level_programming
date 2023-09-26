#!/usr/bin/python3
"""Square class module"""


class Square:
    """Square Class"""

    def __init__(self, size=0):
        """class instance
            raises:
                TypeError
                ValueError
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size of int must be >= 0")
        self.__size = size
