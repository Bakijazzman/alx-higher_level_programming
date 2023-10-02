#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """An empty class with no methods or attributes"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializing the class
        Args:
            width: represents the width of the rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError: if input is not an integer
            ValueError: if input is less than 0
        """
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    @property
    def width(self):
        """returns attributes to the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retturn the height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """sets height attributes"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of a triangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of a triangle"""
        if not self.width or not self.height:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """prints a string of the class """
        rect = ""

        if self.width == 0 or self.height == 0:
            return rect

        for mem in range(self.height):
            rect += ("#" * self.width) + "\n"

        return rect[:-1]

    def __repr__(self):
        """return formal representaton of the class """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """prints a message on delete """
        print("Bye rectangle...")
        self.__class__.number_of_instances -= 1
