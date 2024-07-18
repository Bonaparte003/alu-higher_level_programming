#!/usr/bin/python3
"""
write function that writes string of text
and returns numbers of characters written
"""


def write_file(filename="", text=""):
    """function"""
    with open(filename, "w", encoding="utf-8") as me:
        num = me.write(text)
        return num
