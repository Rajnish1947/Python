# Define a Node class
# Root → Left → Right
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Recursive Preorder Traversal\

def preorder(root):
    if root is None:
        return
    print(root.data, end=" ")    # Step 1: Visit root
    preorder(root.left)          # Step 2: Traverse left subtree
    preorder(root.right)         # Step 3: Traverse right subtree

# Example Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Preorder Traversal (Recursive):")
preorder(root)
