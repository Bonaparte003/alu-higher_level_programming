#!/usr/bin/python3
""""using unittest"""


def test_print_square(size):
    """"unittest"""
    if not isinstance(size, (int,)):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)