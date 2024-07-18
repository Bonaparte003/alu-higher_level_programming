#!/usr/bin/python3
import os
# Function that reads the UTF8 and prints to stdout


def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        print(f.read())
