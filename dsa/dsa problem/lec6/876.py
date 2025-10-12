# Problem:
# You are given the head of a singly linked list.
# Return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.
# Example:
# Input:
# head = [1, 2, 3, 4, 5]
# Output:
# [3, 4, 5]
# The middle node is 3.

# Input:
# head = [1, 2, 3, 4, 5, 6]
# Output:
# [4, 5, 6]
# There are two middles (3, 4), return 4.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create linked list: 7 -> 9 -> 10
a = Node(7)
b = Node(9)
c = Node(10)
d= Node(20)
e= Node(15)
f= Node(15)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
head = a

# Step 1: Find length of list
length = 0
curr = head
while curr != None:
    
    curr = curr.next
    length += 1

# Step 2: Move to middle node
curr = head
for i in range(length // 2):
    curr = curr.next
    

# Step 3: Print the middle node
print("Middle node is:", curr.data)
 
