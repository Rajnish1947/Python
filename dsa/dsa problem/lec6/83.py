# Remove duplicates from a sorted linked list (Run directly in VS Code)

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Create a linked list: 1 -> 1 -> 2 -> 3 -> 3
a = Node(1)
b = Node(1)
c = Node(2)
d = Node(3)
e = Node(3)

a.next = b
b.next = c
c.next = d
d.next = e

head = a  # starting node

# Function to remove duplicates
curr = head
while curr is not None and curr.next is not None:
    if curr.val == curr.next.val:
        curr.next = curr.next.next
    else:
        curr = curr.next

# Function to print linked list
def printList(head):
    curr = head
    while curr:
        print(curr.val, end=" -> " if curr.next else "\n")
        curr = curr.next

# Print result
print("After removing duplicates:")
printList(head)

# class Solution(object):
#     def deleteDuplicates(self, head):
#         """
#         :type head: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         if head==None or head.next==None:
#             return head
#         curr=head

#         while curr!=None and curr.next!=None:
#                 if curr.val==curr.next.val:
#                     curr.next=curr.next.next
#                 else :
#                  curr=curr.next   
#         return head            
