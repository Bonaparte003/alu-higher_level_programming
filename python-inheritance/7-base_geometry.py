#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """A class with a method area()."""
    def area(self):
        """raises an exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value."""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
