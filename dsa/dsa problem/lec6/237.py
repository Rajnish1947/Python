# Simple Linked List example for deleting a node (LeetCode 237)

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Create linked list: 4 -> 5 -> 1 -> 9
a = Node(4)
b = Node(5)
c = Node(1)
d = Node(9)

a.next = b
b.next = c
c.next = d

# Function to print the list
def printList(head):
    curr = head
    while curr:
        print(curr.val, end=" -> " if curr.next else "\n")
        curr = curr.next

print("Original List:")
printList(a)

# Delete the given node (e.g., node b which has value 5)
# Copy next node value and bypass next
b.val = b.next.val
b.next = b.next.next

print("\nAfter deleting node 5:")
printList(a)
