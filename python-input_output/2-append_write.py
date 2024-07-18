#!/usr/bin/python3
"""
write a function that appends string and
returns the number of characters added
"""


def append_write(filename="", text=""):
    """function that adds to file"""
    with open(filename, "a", encoding="utf-8") as a:
        return a.write(text)
