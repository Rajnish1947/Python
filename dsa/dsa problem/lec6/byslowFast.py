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

fast=head
slow=head
while fast !=None and fast.next!=None :
    slow=slow.next
    fast=fast.next.next
return slow    

