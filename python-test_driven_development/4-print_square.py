#!/usr/bin/python3


def print_square(size):
    '''
    function that prints '#' in square
    '''
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print(('#' * size + '\n') * size, end="")
