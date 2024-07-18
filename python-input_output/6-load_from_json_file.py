#!/usr/bin/python3
"""imports json module"""
import json


def load_from_json_file(filename):
    """function that loads from json file"""
    with open(filename, "r", encoding="utf-8") as a:
        data = json.load(a)
        return data
