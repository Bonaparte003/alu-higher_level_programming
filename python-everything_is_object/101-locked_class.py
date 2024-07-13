#!/usr/bin/python3

'''creation of a class'''


class LockedClass:
    '''Prevents dealing with any kind of attributes
    except "first_name"
    '''
    __slots__ = ["first_name"]
