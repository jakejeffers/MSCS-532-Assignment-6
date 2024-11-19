class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.data.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.data[0]

    def is_empty(self):
        return len(self.data) == 0
# Testing the Queue class
queue = Queue()
queue.enqueue(1)  # Add 1 to the queue
queue.enqueue(2)  # Add 2 to the queue
queue.enqueue(3)  # Add 3 to the queue

print("Front of queue:", queue.peek())  # Peek at the front

print("Dequeued element:", queue.dequeue())  # Remove front
print("Dequeued element:", queue.dequeue())  # Remove next
print("Is queue empty?", queue.is_empty())  # Check if empty
