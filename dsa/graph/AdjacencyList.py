# Graph Representation in Python
# Adjacency List (most common, memory efficient)
# Adjacency Matrix (2D array, easy but more space)

# Using dictionary of lists
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

print(graph)
# Output:
# {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['B', 'C']}
