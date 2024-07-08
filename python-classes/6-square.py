#!/usr/bin/python3
"""Square module"""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square"""
        self.size = size  # This will call the size setter
        self.position = position  # This will call the position setter

    @property
    def size(self):
        """Get the current size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with error checks"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the current position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position with error checks"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#'"""
        if self.__size == 0:
            print("")
            return

        [print("") for _ in range(self.__position[1])]
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
