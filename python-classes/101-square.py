#!/usr/bin/python3
"""Square Module"""


class Square:
    """the square class"""
    def __init__(self, size=0, position=(0, 0)):
        """constructor method"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """getter function"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter function"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            self.__size = value

    @property
    def position(self):
        """getter function"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position with error checks"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """area method"""
        return (self.__size ** 2)

    def my_print(self):
        """Print the square with the character '#'"""
        if self.__size == 0:
            print("")
            return

        [print("") for _ in range(self.__position[1])]
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """The printer"""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
