#!/usr/bin/python3
import json
"""funciton that creates an Object form JSON FILE"""


def load_from_json_file(filename):
    """Creates an Object from a JSON file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.loads(f.read())
