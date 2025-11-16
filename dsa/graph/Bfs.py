class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return None
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


def bfs(start, adj, n):
    queue = Queue()
    visited = [False] * (n + 1)   # +1 because nodes start from 1, not 0
    ans = []  

    queue.enqueue(start)
    visited[start] = True
    ans.append(start)

    while not queue.isEmpty():
        front = queue.dequeue()

        for x in adj[front]:
            if not visited[x]:
                queue.enqueue(x)
                visited[x] = True
                ans.append(x)

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

print("BFS Traversal:", bfs(1, adj, n))





# from collections import deque

# def bfs(start, adj, n):
#     ans = []         # list to keep track of visited nodes
#     queue = deque()  # queue for BFS, start node daal diya
#     visited = [0] * (n + 1)

#     queue.append(start)   # <-- ye line missing thi
#     visited[start] = 1
#     ans.append(start)

#     while len(queue) != 0:
#         e = queue.popleft()
#         ans.append(e)

#         for node in adj[e]:
#             if visited[node] == 0:
#                 queue.append(node)
#                 visited[node] = 1

#     return ans              


# # Example use
# n = 5
# adj = {
#     1: [2, 3],
#     2: [1, 4, 5],
#     3: [1],
#     4: [2],
#     5: [2]
# }

# print("BFS Traversal:", bfs(1, adj, n))
