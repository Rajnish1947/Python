class Node:

    def __init__(self,data):
        self.data=data
        self.next=None

# let creating node
a=Node(7)
b=Node(9)

c=Node(10)
a.next=b
b.next=c
head=a

# print(head.data)
# print(head.next.data)
# print(head.next.next.data)

curr=head
while curr!=None:
    print(curr.data,end=" ")
    curr= curr.next



