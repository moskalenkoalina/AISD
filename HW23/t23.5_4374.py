from collections import deque


class Graph:
    def __init__(self, n, edges):
        self.n = n
        self.edges = edges

    def check_connected(self, deleted):

        g = [[] for _ in range(self.n)]

        for i in range(len(self.edges)):

            if i + 1 in deleted:
                continue

            u, v = self.edges[i]

            g[u].append(v)
            g[v].append(u)

        visited = {0}
        queue = deque([0])

        while queue:
            curr = queue.popleft()

            for to in g[curr]:
                if to not in visited:
                    visited.add(to)
                    queue.append(to)

        if len(visited) == self.n:
            print("Connected")
        else:
            print("Disconnected")


if __name__ == "__main__":

    n, m = map(int, input().split())

    edges = []

    for _ in range(m):
        a, b = map(int, input().split())
        edges.append((a - 1, b - 1))

    graph = Graph(n, edges)

    k = int(input())

    for _ in range(k):

        query = list(map(int, input().split()))

        c = query[0]

        deleted = set(query[1:])

        graph.check_connected(deleted)