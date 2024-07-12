#!/usr/bin/python3
"""Module for inherits_from method."""


def inherits_from(obj, a_class):
    """checks if an object is an instance of a class."""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
