#!/usr/bin/python3
"""This module defines a simple Square class"""


class Square:
    """A ``Square`` class

    Attributes:
        size (`int`): The size of the ``Square``.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Constructs a ``Square`` object
    Args:
        size (`int`): The size of the ``Square``.
            The default value is 0.

    Raises:
        TypeError: If ``size`` is not an integer.
        ValueError: If ``size`` is 0
        """
        self.size = size
        self._position = position

    def area(self):
        '''Computes the area of the ``Square``.
        Returns:
            int: The area of the ``Square``.
        '''
        return self._size ** 2

    @property
    def size(self):
        """Getter method for size

        Returns:
            int: The size of the Square.
        """
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = value

    @property
    def position(self):
        """Getter method for position.
        Returns:
            tuple: the position of the Square as a tuple of 2 integers.
        Raises:
            TypeError: If position is not a tuple of 2 integers.
        """
        return self._position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or not all
        (isinstance(v, int) and v >= 0 for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def my_print(self):
        """Prints a ``Square`` filled with ' #'"""
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                for j in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print()
