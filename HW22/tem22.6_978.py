class Graph:
    def __init__(self, n):
        self.g = [[] for i in range(n)]

    def add(self, u, v):
        self.g[u].append(v)
        self.g[v].append(u)

    def dfs(self, v, used, edges):
        used[v] = True

        for to in self.g[v]:
            if not used[to]:
                edges.append((v + 1, to + 1))
                self.dfs(to, used, edges)


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = Graph(n)

    for _ in range(m):
        u, v = map(int, input().split())
        g.add(u - 1, v - 1)

    used = [False] * n
    edges = []

    g.dfs(0, used, edges)

    for u, v in edges:
        print(u, v)