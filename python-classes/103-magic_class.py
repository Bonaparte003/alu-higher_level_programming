#!/usr/bin/python3
"""Translating Bytecode to Python Code"""

import math


class MagicClass:
    """class Magic Class"""

    def __init__(self, radius=0):
        """Initialize the MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """return the area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """returns the circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)
