n = 5
m = 6
edges = [[1, 2], [2, 4], [3, 4], [1, 3], [3, 5], [5, 4]]

# matrix
matrix = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for u, v in edges:
    matrix[u][v] = 1
    matrix[v][u] = 1


print(matrix)


