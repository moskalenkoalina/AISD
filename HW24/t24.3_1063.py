from collections import deque


def bfs(grid, m, n, i, j, visited):
    q = deque([(i, j)])
    visited[i][j] = True

    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    while q:
        x, y = q.popleft()

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy

            if 0 <= nx < m and 0 <= ny < n:
                if not visited[nx][ny] and grid[nx][ny] == '#':
                    visited[nx][ny] = True
                    q.append((nx, ny))


def count_components(grid, m, n):
    visited = [[False] * n for _ in range(m)]
    count = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '#' and not visited[i][j]:
                bfs(grid, m, n, i, j, visited)
                count += 1

    return count


if __name__ == "__main__":
    m, n = map(int, input().split())
    grid = [list(input().strip()) for _ in range(m)]

    print(count_components(grid, m, n))