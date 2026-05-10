class Graph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)

    def bfs(self, start):
        dist = [-1] * self.n
        dist[start] = 0

        queue = [start]
        head = 0

        while head < len(queue):
            v = queue[head]
            head += 1

            for to in range(self.n):
                if self.matrix[v][to] == 1 and dist[to] == -1:
                    dist[to] = dist[v] + 1
                    queue.append(to)

        return dist


if __name__ == "__main__":
    n, x = map(int, input().split())
    x -= 1

    matrix = [list(map(int, input().split())) for _ in range(n)]
    g = Graph(matrix)

    dist = g.bfs(x)
    print(*dist)
