from collections import deque


class Graph:
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]
        self.indeg = [0] * n

    def add_edge(self, u, v):
        self.g[u].append(v)
        self.indeg[v] += 1

    def topological_sort(self):
        q = deque()

        for i in range(self.n):
            if self.indeg[i] == 0:
                q.append(i)

        topo = []

        while q:
            v = q.popleft()
            topo.append(v + 1)

            for to in self.g[v]:
                self.indeg[to] -= 1

                if self.indeg[to] == 0:
                    q.append(to)

        if len(topo) != self.n:
            print(-1)
        else:
            print(*topo)


n, m = map(int, input().split())

graph = Graph(n)

for _ in range(m):
    u, v = map(int, input().split())
    graph.add_edge(u - 1, v - 1)

graph.topological_sort()