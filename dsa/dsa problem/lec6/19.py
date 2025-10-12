# Simple version of Remove Nth Node From End
# Run directly in VS Code
#         p1 = head
#         p2 = head

        
#         for i in range(n):
#             p2 = p2.next

        
#         if p2 is None:
#             head = head.next
#             return head  

       
#         while p2.next is not None:
#             p2 = p2.next
#             p1 = p1.next

        
#         p1.next = p1.next.next

#         return head






class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# 🔹 Create linked list: 1 -> 2 -> 3 -> 4 -> 5
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
a.next = b
b.next = c
c.next = d
d.next = e

head = a

# 🔹 Print original list
curr = head
print("Original list:")
while curr:
    print(curr.val, end=" -> " if curr.next else "\n")
    curr = curr.next

# 🔹 Choose n
n = int(input("\nEnter n (which node from end to remove): "))

# Step 1: Create dummy node before head (helps with edge cases)
dummy = Node(0)
dummy.next = head

# Step 2: Set two pointers
p1 = dummy
p2 = dummy

# Step 3: Move p2 n+1 steps ahead
for i in range(n + 1):
    if p2:
        p2 = p2.next

# Step 4: Move both until p2 reaches end
while p2:
    p1 = p1.next
    p2 = p2.next

# Step 5: Remove target node
p1.next = p1.next.next

# Step 6: Print final list
print("\nAfter removing", n, "node(s) from end:")
curr = dummy.next
while curr:
    print(curr.val, end=" -> " if curr.next else "\n")
    curr = curr.next
