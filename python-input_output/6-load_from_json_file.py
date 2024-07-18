#!/usr/bin/python3
import os
import json
# funciton that creates an Object form JSON FILE


def load_from_json_file(filename):
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.loads(f.read())
