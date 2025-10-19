class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, v1, v2):
        # Assuming undirected graph
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)

    def display(self):
        for vertex, edges in self.adj_list.items():
            print(f"{vertex} --> {edges}")

# Example usage
g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')

g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')

g.display()
