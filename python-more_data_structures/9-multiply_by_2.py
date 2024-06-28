#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_list = a_dictionary.copy()
    new = list(a_dictionary.keys())
    for i in new:
        new_list[i] *= 2
    return new_list
