n = int(input())

g = [[] for _ in range(n + 1)]
cost = [0] * (n + 1)

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    cost[i] = data[0]
    k = data[1]
    children = data[2:]
    g[i] = children

def dfs(v):
    if len(g[v]) == 0:
        return cost[v]

    mn = float('inf')
    for j in g[v]:
        mn = min(mn, dfs(j))

    return cost[v] + mn

print(dfs(1))