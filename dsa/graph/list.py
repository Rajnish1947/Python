n = 5
m = 6
edges = [[1, 2], [2, 4], [3, 4], [1, 3], [3, 5], [5, 4]]

# 1-based index graph
list = [[] for _ in range(n + 1)]

for u, v in edges:
    list[u].append(v)
    list[v].append(u)


print(list)
