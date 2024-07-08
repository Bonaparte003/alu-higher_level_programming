#!/usr/bin/python3
""" a module that creates an empty class"""


class Square:
    """Square Module"""
    def __init__(self, size=0):
        """Constructor method"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """function to calculate area"""
        return (self.__size ** 2)
