#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        # Try to execute the function with the provided arguments
        return fct(*args)
    except Exception as e:
        # If an exception occurs, print the error message to stderr
        print("Exception:", e, file=sys.stderr)
        return None
