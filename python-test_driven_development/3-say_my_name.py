#!/usr/bin/python3

"""function say_my_name that prints out the names with 'My name is'"""


def say_my_name(first_name, last_name=""):
    '''
    function that prints names
    '''
    if type(first_name) is not str:
        raise TypeError("Names must be strings")
    if type(last_name) is not str:
        raise TypeError("Names must be strings")
    print("My name is", first_name, last_name)
