#!/usr/bin/python3
'''Square module definition.

This module defines a simple `Square` class
'''


class Square:
    '''A simple ``simple`` class

    Attributes:
        size (`int`): The size of the ``Square``.
    '''
    def __init__(self, size=0):
        '''Constructs a ``Square`` object
    Args:
        size (`int`): The size of the ``Square``.
            The default value is 0.

    Raises:
        TypeError: If ``size`` is not an integer.
        ValueError: If ``size`` is 0
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size

    def area(self):
        '''Computes the area of the ``Square``.
        Returns:
            int: The area of the ``Square``.
        '''
        return self._Square__size ** 2

    @property
    def size(self):
        """Getter method for size

        Returns:
            int: The size of the Square.
        """
        return self._Square__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size

    @property
    def position(self):
        """
        Args:
            position: The position to print the ``Square``.
        Raises:
            TypeError: If position is not a tuple of 2 integers.
        """
        return self._Square__position

    @position.setter
    def position(self, value):
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.Square__position = position

    def my_print(self):
        """Prints a ``Square`` filled with '#'"""
        if self.size:
            for i in range(self.size):
                print(" " * self.position[0], end="")
                for j in range(self.size):
                    print("#", end="")
                print()
        else:
            print()
