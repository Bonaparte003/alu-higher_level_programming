#!/usr/bin/python3
"""MyInt Module"""


class MyInt(int):
    """MyInt class"""
    def __eq__(self, other):
        """Equal method"""
        return int(self) != int(other)

    def __ne__(self, other):
        """Not equal method"""
        return int(self) == int(other)
