from node import DoubleNode
from singly_linked_list import SinglyLinkedList


class DoublyLinkedList(SinglyLinkedList):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def prepend(self, data):
        new_node = DoubleNode(data, self.head, None)
        if self.length != 0:
            self.head._prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self.length += 1

    def append(self, data):
        new_node = DoubleNode(data, None, self.tail)
        if self.length != 0:
            self.tail._next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.length += 1

    def delete_from_head(self):
        if self.length == 0:
            return
        self.head = self.head._next
        self.head._prev = None
        self.length -= 1

    def delete_from_tail(self):
        if self.length == 0:
            return

        # define two tracker nodes
        current_node = self.head
        previous_node = current_node

        # iterate until the last tracker node is the tail
        while current_node._next is not None:
            previous_node = current_node
            current_node = current_node._next

        # set next for node before tail to none
        previous_node._next = None
        self.tail = previous_node
        self.length -= 1

    def find(self, data):
        current_node = self.tail
        while current_node is not None:
            if current_node._data == data:
                return True
            current_node = current_node._prev

        return False

    def delete(self, data):
        if self.length == 0:
            return
        # define two tracker nodes
        current_node = self.head
        previous_node = current_node

        # iterate until the current node is equal to the requested deletion
        while current_node is not None:
            if current_node._data == data:
                self.length -= 1
                previous_node._next = current_node._next
                current_node._next._prev = previous_node
                return
            previous_node = current_node
            current_node = current_node._next

    def reverse(self):
        reversed_list = DoublyLinkedList()
        current_node = self.tail
        while current_node is not None:
            reversed_list.append(current_node._data)
            current_node = current_node._prev

        return reversed_list

    def print(self):
        current_node = self.head
        while current_node is not None:
            print(current_node._data)
            current_node = current_node._next
        print('--------------')
