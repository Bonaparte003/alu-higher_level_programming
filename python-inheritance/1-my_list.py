#!/usr/bin/python3
"""Module for MyList class."""


class MyList(list):
    """Custom list class."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
