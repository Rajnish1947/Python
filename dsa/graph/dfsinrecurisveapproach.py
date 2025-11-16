def dfs(graph, start, visited=None):
    if visited is None:
        visited = []      # Pehle bar call me empty list banai

    if start not in visited:
        visited.append(start)   # Node ko visit mark kar diya

        # Har neighbor ke liye DFS call karo
        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)

    return visited


# Example Graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': ['B'],
    'E': ['B']
}

print("DFS Traversal (Recursive):", dfs(graph, 'A'))
