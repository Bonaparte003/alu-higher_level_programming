#!/usr/bin/python3
"""Node module"""


class Node:
    """Class Node that defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        self.data = data  # calls the setter
        self.next_node = next_node  # calls the setter

    @property
    def data(self):
        """Allows access to the private instance attribute __data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the private instance attribute __data."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Allows access to the private instance attribute __next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the private instance attribute __next_node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class SinglyLinkedList that defines a singly linked list."""

    def __init__(self):
        """Constructor"""
        self.__head = None

    def __str__(self):
        """Prints the entire list in stdout, one node number per line."""
        a = self.__head
        result = []
        while a is not None:
            result.append(str(a.data))
            a = a.next_node
        return '\n'.join(result)

    def sorted_insert(self, value):
        """Inserts a new Node """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            a = self.__head
            while a.next_node is not None and a.next_node.data < value:
                a = a.next_node
            new_node.next_node = a.next_node
            a.next_node = new_node
