class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, value):
        if self.head is None:
            return False
        if self.head.value == value:
            self.head = self.head.next
            return True
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        if current.next:
            current.next = current.next.next
            return True
        return False

    def traverse(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
# Testing the LinkedList class
linked_list = LinkedList()
linked_list.insert(10)  # Add 10 to the list
linked_list.insert(20)  # Add 20 to the list
linked_list.insert(30)  # Add 30 to the list

print("Linked list after insertions:")
linked_list.traverse()  # Print all elements

linked_list.delete(20)  # Remove 20 from the list
print("Linked list after deletion:")
linked_list.traverse()
