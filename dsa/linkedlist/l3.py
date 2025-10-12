class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create initial list: 7 -> 9 -> 10
a = Node(7)
b = Node(9)
c = Node(10)
a.next = b
b.next = c
head = a

# Helper function for traversal
def traverse(head):
    curr=head
    while curr !=None:
     print(curr.data,end=" ")
     curr=curr.next

print("Initial list:")
traverse(head)

# 1️⃣ Insert at end
newNode = Node(6)
curr = head
while curr.next != None:
    curr = curr.next
curr.next = newNode

print("After inserting 6 at end:")
traverse(head)

# 2️⃣ Insert at k-th index
k = 3
newNode = Node(3)
curr = head
for i in range(k-1):
    curr = curr.next
newNode.next = curr.next
curr.next = newNode

print(f"After inserting 3 at index {k}:")
traverse(head)

# 3️⃣ Delete first node
head = head.next
print("After deleting first node:")
traverse(head)

# 4️⃣ Delete last node
curr = head
while curr.next.next != None:
    curr = curr.next
curr.next = None
print("After deleting last node:")
traverse(head)

# 5️⃣ Delete k-th index element
k = 2
curr = head
for i in range(k-1):
    curr = curr.next
curr.next = curr.next.next
print(f"After deleting node at index {k}:")
traverse(head)



# class Node:
#      def __init__(self,data):
#           self.data=data
#           self.next=None

# a=Node(7)
# b=Node(9)
# c=Node(10)
# a.next=b
# b.next=c
# head=a




# #  insertion 
# newNode=Node(6)
# curr=head
# while curr.next !=None:
    
#      curr=curr.next 
# curr.next=newNode  
 

#  # after insertion traveling
# # curr=head
# # while curr !=None:
# #      print(curr.data,end=" ")
# #      curr=curr.next

# # insertion on k th index

# k=3

# newNode=Node(3)
# curr=head

# for i in range(k-1):
#      curr=curr.next
# newNode.next=curr.next
# curr.next=newNode

# # delete first node   
# head=head.next

# # delete last node   
# curr=head
# while curr.next.next !=None:
    
#      curr=curr.next
# curr.next=None  

# # delete the k th indext element
# k=2
# curr=head
# for i in range(k-1):
#      curr=curr.next
# curr.next=curr.next.next     


#  # after insertion traveling
# curr=head
# while curr !=None:
#      print(curr.data,end=" ")
#      curr=curr.next






         