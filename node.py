class SingleNode:
    def __init__(self, data, next):
        self._data = data
        self._next = next


class DoubleNode:
    def __init__(self, data, next, prev):
        self._data = data
        self._next = next
        self._prev = prev
