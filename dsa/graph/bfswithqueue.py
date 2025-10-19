class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)   # add at the end

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  # remove from front

    def is_empty(self):
        return len(self.items) == 0


def bfs(graph, start):
    visited = []          # visited nodes list
    q = Queue()           # create queue object
    q.enqueue(start)      # start node add karo

    while not q.is_empty():      # jab tak queue empty nahi
        vertex = q.dequeue()     # first element nikal lo

        if vertex not in visited:     # agar visit nahi hua
            visited.append(vertex)    # mark as visited

            # sab connected nodes queue me daal do
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    q.enqueue(neighbor)

    return visited


# Example Graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': ['B'],
    'E': ['B']
}

print("BFS Traversal:", bfs(graph, 'A'))
