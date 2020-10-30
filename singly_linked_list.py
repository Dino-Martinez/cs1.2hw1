class Node:
    def __init__(self, data, next):
        self._data = data
        self._next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def prepend(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        if self.length == 0:
            self.tail = self.head
        self.length += 1

    def append(self, data):
        new_node = Node(data, None)
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
        self.length -= 1

    def delete_from_tail(self):
        if self.length == 0:
            return

        # define two tracker nodes
        current_node = self.head
        previous_node = current_node

        # iterate until the last tracker node is the tail
        while(current_node._next is not None):
            previous_node = current_node
            current_node = current_node._next

        # set next for node before tail to none
        previous_node._next = None
        self.length -= 1

    def print(self):
        current_node = self.head
        while(current_node is not None):
            print(current_node._data)
            current_node = current_node._next
        print('--------------')
