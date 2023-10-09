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
