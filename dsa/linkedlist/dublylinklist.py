class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# Create nodes
a = DoublyNode(7)
b = DoublyNode(9)
c = DoublyNode(10)

# Connect nodes (Doubly Linked List)
a.next = b
b.prev = a
b.next = c
c.prev = b

# Head of the list
head = a