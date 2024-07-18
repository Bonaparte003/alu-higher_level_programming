#!/usr/bin/python3
import json
# function that writes an Object to text file
# in json form


def save_to_json_file(my_obj, filename):
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
