visited = [False] * 5   # +1 because nodes start from 1
ans = []

def dfs(i, parent, adjlist, visited):
    visited[i] = True

    for x in adjlist[i]:
        if x == parent:
            continue
        if visited[x]:
            return True

        if dfs(x, i, adjlist, visited):
            return True

    return False


n = 5
adj = {
    0: [2, 3],
    1: [1, 4, 5],
    2: [1],
    3: [2],
    4: [2]
}

adjs = {
    0: [1, 3],
    1: [0,2],
    2: [1],
    3: [0],
    4: [0]
}
# call from node 1 instead of 0
print(dfs(1, -1, adj, visited))
print(dfs(1, -1, adjs, visited))
