'''
    The LinkedList class implements a singly linked list.
'''

from typing import List, Optional, TypeVar, Generic
T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data: T = data  # value of the node
        self.next: Optional[Node[T]] = None  # pointer to the next node


class LinkedList(Generic[T]):
    def __init__(self, nodes: Optional[List[T]] = None) -> None:
        """ Creates a LinkedList, optionally initialized from a list of nodes """
        self.head = None
        if nodes:
            self.append_from_list(nodes)

    def append(self, data: T) -> None:
        """ Adds a node to the end of the list """
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
            return

    def append_from_list(self, lst: Optional[List[T]]) -> None:
        """ Appends nodes with values from a list """
        if lst is None:
            return
        for val in lst:
            self.append(val)

    def prepend(self, data: T) -> None:
        """ Adds a node to the beginning of the list """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, node_data: T, new_data: T) -> bool:
        """ Inserts a node after the first node with the given value """
        new_node = Node(new_data)
        current = self.head
        while current:
            if current.data == node_data:
                new_node.next = current.next
                current.next = new_node
                return True
            current = current.next
        return False

    def delete(self, data: T) -> bool:
        """ Deletes the first node with the given value. Returns True if deleted, False if not found. """
        current = self.head
        prev = None

        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next

        return False

    def to_list(self) -> List[T]:
        """ Returns a list with the values from the LinkedList """
        return list(iter(self))

    def clear(self) -> None:
        """ Clears the LinkedList """
        self.head = None

    def find(self, data: T) -> Optional[Node[T]]:
        """ Returns the first node found with the data """
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def __str__(self) -> str:
        """ Returns a string representation of the linked list """
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return " -> ".join(values)

    def __len__(self) -> int:
        """ Returns the number of nodes in the list """
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __iter__(self):
        """ Allows iteration like: for x in linked_list """
        current = self.head
        while current:
            yield current.data
            current = current.next
