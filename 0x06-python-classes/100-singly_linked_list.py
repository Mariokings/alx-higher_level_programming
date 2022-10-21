#!/usr/bin/python3

"""Defines a class Node"""


class Node:
    """Represents a Node"""

    def __init__(self, data, next_node=None):
        """Initializing a new Node
        Args:
            data (int): value stored in a singly linked list
            next_node (): new node in a singly linked list
        """
        self.data = data
        self.next_node = next_node

        @property
        def data(self):
            """Get/set a new data"""
            return self.__data

        @data.setter
        def data(self, value):
            try:
                assert type(value) == int
            except AssertionError:
                raise TypeError(data must be an integer)
            self.__data = value

            @property
            def next_node(self):
                """Get/set a new node"""
                return self.__next_node

            @next_node.setter
            def next_node(self, value):
                if not isinstance(value, Node) and value not None:
                    raise TypeError("next_node must be a Node object")
                self.__next_node = next_node



"""Define a class SinglyLinkedList"""

class SinglyLinkedList:
    """Represents a SinglyLinkedList"""

    def __init__(self, head):
        """Initializing a SinglyLinkedList

        Args:
            head:
        """
        self.__head = head

    def __str__(self):
        return f"{self.__head}"
