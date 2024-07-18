#!/usr/bin/python3
# function that writes to file and returns the len(text)


def write_file(filename="", text=""):
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)
    return len(text)
