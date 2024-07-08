#!/usr/bin/python3


"""Square module"""


class Square:
    """class def"""

    def __init__(self, size=0, position=(0, 0)):

        """init square"""

        self.__size = size
        self.__position = position

    @property
    def size(self):

        """get the current size '@' decoration"""
        return self.__size

    @size.setter
    def size(self, value):

        """check for errors and raise em"""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(self.__position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """squares"""

        return self.__size ** 2

    def my_print(self):
        """function that prints '#'"""

        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
