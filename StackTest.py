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
# Testing the Stack class
stack = Stack()
stack.push(5)  # Push 5 onto the stack
stack.push(10)  # Push 10 onto the stack
print("Top of stack:", stack.peek())  # Peek at the top

print("Popped element:", stack.pop())  # Pop the top element
print("Popped element:", stack.pop())  # Pop the next element
print("Is stack empty?", stack.is_empty())  # Check if empty
