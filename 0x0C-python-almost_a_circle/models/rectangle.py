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
