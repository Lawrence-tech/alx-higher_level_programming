#!/usr/bin/python3
"""
First rectangle that inherits from Base
"""
from . base import Base
import json


class Rectangle(Base):
    """ class Rectangle that inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class Constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieve the width of rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """ set passet private attributes of width """
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
            self.Width = value

    @property
    def height(self):
        """Retrieve the height of rectangle """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ set passet private attribute height """
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Retrieve private instance attribute x """
        return (self.__x)

    @x.setter
    def x(self, value):
        """set private instance attribute x """
        if (type(value) is not int):
            raise TypeError("x must be an integeer")
        if (value < 0):
            raise ValueError("x must be  >= 0")
            self.__x = value

    @property
    def y(self):
        """Retrieve private instance attribute y """
        return (self.__y)

    @y.setter
    def y(self, value):
        """set private instance attribute y """
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
            self.__y = value
