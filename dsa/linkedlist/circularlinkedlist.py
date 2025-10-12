class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create nodes
a = Node(7)
b = Node(9)
c = Node(10)

# Link them
a.next = b
b.next = c
c.next = a   # 👈 last node points to head (circular)

head = a


# 🌀 Traversing circular list (stop when we reach head again)
print("Circular Linked List:")
curr = head
while True:
    print(curr.data, end=" -> ")
    curr = curr.next
    if curr == head:
        break
print("(Back to Head)")


# 👉 Insert at end
newNode = Node(15)
curr = head
while curr.next != head:
    curr = curr.next
curr.next = newNode
newNode.next = head


# Display after insertion
print("\nAfter inserting 15 at end:")
curr = head
while True:
    print(curr.data, end=" -> ")
    curr = curr.next
    if curr == head:
        break
print("(Back to Head)")


# 👉 Delete last node
curr = head
while curr.next.next != head:
    curr = curr.next
curr.next = head


# Display after deletion
print("\nAfter deleting last node:")
curr = head
while True:
    print(curr.data, end=" -> ")
    curr = curr.next
    if curr == head:
        break
print("(Back to Head)")
