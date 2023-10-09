#!/usr/bin/python3

"""
Module containing class node and class SinglyLinkedList
"""


class Node:
    """
    Represents a node of a singly linked list.

    Attributes:
        data: An integer representing the data stored in the node.
        next_node: A reference to the next node in the linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node instance.

        Args:
            data: An integer representing the data to be stored in the node.
            next_node: A reference to the next node in the linked list.
                       Defaults to None.

        Raises:
            TypeError: If data is not integer or next_node is not Node object.
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Getter method for the data attribute."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method for the data attribute."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter method for the next_node attribute."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method for the next_node attribute."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list.

    Attributes:
        head: A reference to the first node in the linked list.
    """

    def __init__(self):
        """
        Initializes a new SinglyLinkedList instance.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts new node with the given value into linked list in sorted order.

        Args:
            value: An integer representing the value to be inserted.
        """
        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None\
                    and value >= current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.
        """
        result = ""
        current = self.__head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
