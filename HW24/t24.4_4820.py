from collections import deque


def bfs(grid, n, m, start, end):
    q = deque([start])

    dist = [[-1] * m for _ in range(n)]
    dist[start[0]][start[1]] = 0

    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    while q:
        x, y = q.popleft()

        if (x, y) == end:
            return dist[x][y]

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == '0' and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

    return -1


if __name__ == "__main__":

    n, m = map(int, input().split())

    grid = [input().split() for _ in range(n)]

    y1, x1 = map(int, input().split())
    y2, x2 = map(int, input().split())

    start = (x1 - 1, y1 - 1)
    end = (x2 - 1, y2 - 1)

    print(bfs(grid, n, m, start, end))