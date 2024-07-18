#!/usr/bin/python3
"""create a function that reads files"""


def read_file(filename=""):
    """function that reads files"""
    with open(filename, encoding="utf-8") as a:
        print("{}".format(a.read()), end="")
