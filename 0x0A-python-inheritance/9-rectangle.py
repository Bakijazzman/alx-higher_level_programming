#!/usr/bin/python3
"""Import module here """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class that nherits from base geometry"""
    def __init__(self, width, height):
        """validates width and height values"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns area of a rectangle """
        return self.__width * self.__height

    def __str__(self):
        """func to return the rec description"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
