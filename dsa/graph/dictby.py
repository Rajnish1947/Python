n = 5
m = 6
edges = [[1, 2], [2, 4], [3, 4], [1, 3], [3, 5], [5, 4]]

# 1-based index graph
list = [[] for _ in range(n + 1)]
my_dict={}

for i in range(1,n+1):
    my_dict[i]=[]

for u, v in edges:
    my_dict[u].append(v)
    my_dict[v].append(u)


print(my_dict)