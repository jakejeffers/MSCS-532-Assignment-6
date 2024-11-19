class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.data.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0
