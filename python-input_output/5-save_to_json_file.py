#!/usr/bin/python3
"""import of modules"""
import json


def save_to_json_file(my_obj, filename):
    """function hta saves to json files"""
    with open(filename, "w", encoding="utf-8") as a:
        json.dump(my_obj, a)
