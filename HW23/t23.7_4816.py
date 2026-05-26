from collections import deque


class Graph:
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.g[u].append(v)
        self.g[v].append(u)

    def bfs(self, start, visited):

        component = []

        queue = deque([start])
        visited.add(start)

        while queue:
            curr = queue.popleft()

            component.append(curr + 1)

            for to in self.g[curr]:
                if to not in visited:
                    visited.add(to)
                    queue.append(to)

        return component

    def connected_components(self):

        visited = set()

        components = []

        for v in range(self.n):

            if v not in visited:
                comp = self.bfs(v, visited)
                components.append(comp)

        print(len(components))

        for comp in components:
            print(len(comp))
            print(*comp)


if __name__ == "__main__":

    n, m = map(int, input().split())

    graph = Graph(n)

    for _ in range(m):
        u, v = map(int, input().split())
        graph.add_edge(u - 1, v - 1)

    graph.connected_components()