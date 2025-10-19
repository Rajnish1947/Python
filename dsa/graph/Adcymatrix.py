class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v):
        # Undirected graph
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1

    def display(self):
        print("Adjacency Matrix:")
        for row in self.matrix:
            print(row)

# Example usage
g = Graph(4)  # 4 vertices (0=A, 1=B, 2=C, 3=D)

g.add_edge(0, 1)  # A-B
g.add_edge(0, 2)  # A-C
g.add_edge(1, 3)  # B-D
g.add_edge(2, 3)  # C-D

g.display()
