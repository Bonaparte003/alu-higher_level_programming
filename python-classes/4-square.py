#!/usr/bin/python3
""" a module that creates an empty class"""


class Square:
    """Square Module"""
    def __init__(self, size=0):
        """Constructor method"""
        self.__size = size

    @property
    def size(self):
        """getter function"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter function"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """function to calculate area"""
        return (self.__size ** 2)
