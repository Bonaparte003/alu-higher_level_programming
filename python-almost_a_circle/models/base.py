#!/usr/bin/python3
"""
1.creation of Base class with:
    a) private class attribute "__nb_objects = 0"
    b) a class constructor "def __init__(self, id=None):"
"""

import json
import csv
import turtle


class Base:
    """creation of base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries, sort_keys=True)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of dictionaries from the JSON string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise NotImplementedError(
                    f"create method not implemented forclass {cls.__name__}"
                    )
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []
