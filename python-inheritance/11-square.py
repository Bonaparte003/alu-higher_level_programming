#!/usr/bin/python3
"""Module for BaseGeometry class."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that inherits from Rectangle."""
    def __init__(self, size):
        """Instantiation with size."""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns a string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
