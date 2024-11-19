class Array:
    def __init__(self):
        self.data = []

    def insert(self, index, value):
        if index > len(self.data) or index < 0:
            raise IndexError("Index out of range")
        self.data.insert(index, value)

    def delete(self, index):
        if index >= len(self.data) or index < 0:
            raise IndexError("Index out of range")
        return self.data.pop(index)

    def access(self, index):
        if index >= len(self.data) or index < 0:
            raise IndexError("Index out of range")
        return self.data[index]
