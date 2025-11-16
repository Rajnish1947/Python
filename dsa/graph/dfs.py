class Stack:
    def __init__(self):
        self.stack = []

    # Push element into stack
    def push(self, x):
        self.stack.append(x)

    # Pop element from stack
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    # Get the top (last) element
    def last(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    # Get size of stack
    def size(self):
        return len(self.stack)

    # Display stack nicely when printed
    def __str__(self):
        return f"Stack: {self.stack}"


def dfs(start, adj, n):
    stack = Stack()
    visited = [False] * (n + 1)   # +1 because nodes start from 1, not 0
    ans = []

    stack.push(start)
    visited[start] = True

    while stack.size() > 0:
        top = stack.pop()
        ans.append(top)

        # Process neighbors (push unvisited)
        for x in adj[top]:  # reverse to match recursive DFS order
            if not visited[x]:
                stack.push(x)
                visited[x] = True

    return ans


# Example use
n = 5
adj = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}

print("DFS Traversal:", dfs(1, adj, n))




# def dfs(node, result, visited, graph):
#     visited[node] = 1
#     result.append(node)
    
#     for n in graph[node]:
#         if visited[n] == 0:
#             dfs(n, result, visited, graph)

# # Example Graph (Adjacency List)
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A'],
#     'D': ['B'],
#     'E': ['B']
# }

# # Initialize visited as a dictionary
# visited = {node: 0 for node in graph}
# result = []

# # Call DFS starting from node 'A'
# dfs('A', result, visited, graph)

# print("DFS Traversal:", result)
