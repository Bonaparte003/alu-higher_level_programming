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
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")


Obj = BaseGeometry()
Obj.integer_validator("age", 2)