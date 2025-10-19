from collections import deque

def bfs(graph, start):
    visited = []         # list to keep track of visited nodes
    queue = deque([start])  # queue for BFS, start node daal diya

    while queue:               # jab tak queue empty nahi hoti
        vertex = queue.popleft()  # queue se ek node nikalo

        if vertex not in visited:   # agar visit nahi hua hai to
            visited.append(vertex)  # mark as visited
            # uske sab neighbors queue me daal do
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return visited

# Example use
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': ['B'],
    'E': ['B']
}

print("BFS Traversal:", bfs(graph, 'A'))
