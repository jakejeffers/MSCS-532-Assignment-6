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
# Testing the Array class
array = Array()
array.insert(0, 10)  # Insert 10 at index 0
array.insert(1, 20)  # Insert 20 at index 1
array.insert(2, 30)  # Insert 30 at index 2
print("Array after insertions:", array.data)

array.delete(1)  # Remove the element at index 1
print("Array after deletion:", array.data)

print("Access element at index 1:", array.access(1))  # Access index 1
