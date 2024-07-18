#!/usr/bin/python3
""" Module for Student class """


class Student:
    """class Student"""
    def __init__(self, first_name, last_name, age):
        """initializes student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dictionary"""
        return self.__dict__
