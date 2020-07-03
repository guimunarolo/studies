class Stack:
    """Stack data structure representation. Last-in first-out, LIFO."""

    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self.is_empty():
            return self._items.pop()

    def peek(self):
        if not self.is_empty():
            return self._items[-1]

    def is_empty(self):
        return self._items == []
