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
        """Initializing a SinglyLinkedList"""

        self.__head = head

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.
            The node is inserted into the list at the correct
            ordered numerical position.
        Args:
            value (Node): The new Node to insert.
        """

        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while temp.next_node is not None and temp.next_node.data < value:
                temp = temp.next.node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))
