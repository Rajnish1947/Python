# Visit all nodes level by level, from left to right.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Create tree
root = Node(5)
root.left = Node(3)
root.right = Node(4)
root.right.right = Node(2)

# Function to print tree level by level
def print_level_order(root):
    if root is None:
        return
    
    queue = [root]  # Start with root node

    while queue:
        node = queue.pop(0)
        print(node.data, end=" ")

        # Add left and right children to the queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Call the function
print("Level order traversal:")
print_level_order(root)
