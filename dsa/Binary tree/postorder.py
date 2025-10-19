# Left → Right → Root
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Recursive Preorder Traversal\

def postorder(root):
    if root is None:
        return
        # Step 1: Visit root
    postorder(root.left)          # Step 2: Traverse left subtree
    postorder(root.right)         # Step 3: Traverse right subtree
    print(root.data, end=" ")

# Example Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Preorder Traversal (Recursive):")
postorder(root)
