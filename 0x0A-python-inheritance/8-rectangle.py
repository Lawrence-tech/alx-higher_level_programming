#!/usr/bin/python3
"""
BaseGeometry module class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that represents a rectangle"""
    def __init__(self, width, height):
        """Initializes a rectangle object with a given width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
