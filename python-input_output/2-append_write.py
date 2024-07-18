#!/usr/bin/python3
import os
# function that appends and returns the len(text)


def append_write(filename="", text=""):
    with open(filename, mode="a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
