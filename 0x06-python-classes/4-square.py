#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """This is a getter function
            
            Raises:
            TypeError: not an integer
            ValueError: if < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        """this is a setter function
            
            Args:
                value: value to set
        """
        self.__size = value

    def area(self):
        """resturns value of size square"""
        result = self.__size * self.__size
        return result
