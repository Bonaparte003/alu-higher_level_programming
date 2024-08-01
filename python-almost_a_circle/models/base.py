#!/usr/bin/python3
"""
1. Creation of Base class with:
    a) private class attribute "__nb_objects = 0"
    b) a class constructor "def __init__(self, id=None):"
"""

import json
import csv
import turtle


class Base:
    """Creation of base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""
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
                f"create method not implemented for class {cls.__name__}"
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV string representation of list_objs to a file"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline='') as file:
            if list_objs is None:
                file.write("")
            else:
                writer = csv.writer(file)
                if cls.__name__ == "Rectangle":
                    writer.writerow(["id", "width", "height", "x", "y"])
                    for obj in list_objs:
                        writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow(["id", "size", "x", "y"])
                    for obj in list_objs:
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances from a CSV file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline='') as file:
                reader = csv.DictReader(file)
                list_dicts = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        row = {k: int(v) for k, v in row.items()}
                    elif cls.__name__ == "Square":
                        row = {k: int(v) for k, v in row.items() if k != "size"}
                        row["size"] = int(row["size"])
                    list_dicts.append(row)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []
