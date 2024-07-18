#!/usr/bin/python3
"""function that appends and returns the len(text)"""


def append_write(filename="", text=""):
    """Appends a string to a text file (UTF8) && returns number of characters written"""
    with open(filename, mode="a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
