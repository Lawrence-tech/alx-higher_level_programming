#!/usr/bin/python3
"""Square module definition.

This module defines a simple `Square` class
"""


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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = size

        if (not isinstance(position, tuple) or len(position) != 2 or not all
                (isinstance(i, int) and i >= 0 for i in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
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
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = size

    @property
    def position(self):
        """Getter method for position.
        Returns:
            TypeError: If position is not a tuple of 2 integers.
        """
        return self._position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or not all
                (isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self._position = value

    def my_print(self):
        """Prints a ``Square`` filled with ' # '"""
        if self.size:
            for i in range(self.size):
                print("  " * self.position[0], end="")
                for j in range(self.size):
                    print("#", end="")
                print()
        else:
            print()
