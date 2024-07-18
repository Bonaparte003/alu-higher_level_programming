#!/usr/bin/python3
import json
"""function that returns datastructures in json"""


def from_json_string(my_str):
    """Returns the JSON representation of a string"""
    return (json.loads(my_str))
