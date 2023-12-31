#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """This is a getter function """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """resturns value of size square"""
        result = self.__size * self.__size
        return result

    def my_print(self):
        """Print the area of a square with the char #"""
        for i in range(0, self.size):
            [print("#", end="") for j in range(self.size)]
            print("")
        if self.__size == 0:
            print("")
