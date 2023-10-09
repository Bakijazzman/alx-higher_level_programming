#!/usr/bin/python3
"""Import modules here """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class that inherits from Rectangle"""
    def __init__(self, size):
        """initializing attributes """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """function that calculates area"""
        return self.__size * self.__size
