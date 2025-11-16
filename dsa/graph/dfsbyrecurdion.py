visited = [False] * (5 + 1)   # +1 because nodes start from 1
ans = []

def dfs(i, adjlist, visited):
    visited[i] = True
    ans.append(i)
    for x in adjlist[i]:
        if not visited[x]:
            dfs(x, adjlist, visited)

n = 5
adj = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}

dfs(1, adj, visited)  # ✅ start from node 1
print("DFS Traversal:", ans)
