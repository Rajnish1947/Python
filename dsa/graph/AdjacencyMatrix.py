# Vertices: A, B, C, D
# 2D matrix (0 = no edge, 1 = edge exists)

graph = [
    [0, 1, 1, 0],  # A connected to B, C
    [1, 0, 0, 1],  # B connected to A, D
    [1, 0, 0, 1],  # C connected to A, D
    [0, 1, 1, 0]   # D connected to B, C
]

print(graph)
