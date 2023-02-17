#!/usr/bin/python3
"""
BaseGeometry module class
"""


class BaseGeometry:
    """ class that improves geometry with integer validator"""
    def area(self):
        """raises an exception with area() is not implemented message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value """
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class that represents a rectangle"""
    def __init__(self, width, height):
        """Initializes a rectangle object with a given width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
