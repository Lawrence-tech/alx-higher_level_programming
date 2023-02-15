#!/usr/bin/python3
""" Class Rectangle that defines the Rectangle"""


class Rectangle:
    """ class defines a Rectangle with attributes """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Retrieve the width of rectnagle"""
        return self.__width

    @width.setter
    def width(self, width):
        """Width setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Height property function"""
        return self.__height

    @height.setter
    def height(self, height):
        """Height setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """Returns area of rectangle"""
        return self.height * self.width

    def perimeter(self):
        """Returns perimeter of rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return self.height * 2 + self.width * 2

    def __str__(self):
        """Returns rectangle with the character # """
        if self.width == 0 or self.height == 0:
            return ""
        string = ""
        for y in range(self.height - 1):
            string += '#' * self.width + '\n'
        string += '#' * self.width
        return string

    def __repr__(self):
        """Returns repr of the rectangle"""
        string = "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
        return string

    def __del__(self):
        """Delete a rectangle"""
        print("Bye rectangle...")
        if Rectangle.number_of_instances != 0:
            Rectangle.number_of_instances -= 1
