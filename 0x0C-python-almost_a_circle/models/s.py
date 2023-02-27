#!/usr/bin/python3
"""
Program that defines a Square in base from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle """
    def __init(self, size, x=0, y=0, id=None):
        """Conctructor """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Retrieves the size of Square """
        return (self.width)

    @size.setter
    def size(self, value):
        """set passet private attribute oof size """
        self.width = value
        self.height = value

    def __str__(self):
        """overriding the __str__ method that returns a custom string"""
        mssg = "[Square] ({:d}) {:d}/{:d} - {:d}"\
            .format(self.id, self.x, self.y, self.width)
        return (mssg)

    def update(self, *args, **kwargs):
        """method that assigns an argument to each attribute by Non-keyword and
        key/value """
        arlist = ["id", "size", "x", "y"]
        if (args and len(args) != 0):
            for arl in range(len(args)):
                if (arl == 0):
                    super().update(args[arl])
                elif (arl < len(arlist)):
                    setattr(self, arlist[arl], args[arl])
        else:
            for key, value in kwargs.items():
                if (key == 'id'):
                    super().update(value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
            }
