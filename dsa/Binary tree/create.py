class Node:
     def __init__(self,data):
          self.data=data
          self.right=None
          self.left=None
root=Node(5)
root.left=Node(3)   
root.right=Node(4)   
root.right.right=Node(2)  

print(root.right.right.data)