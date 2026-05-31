n, s, f = map(int, input().split())
s -= 1
f -= 1

graph = [list(map(int, input().split())) for _ in range(n)]

INF = float('inf')
dist = [INF] * n
used = [False] * n

dist[s] = 0

for _ in range(n):
    v = -1

    for i in range(n):
        if not used[i] and (v == -1 or dist[i] < dist[v]):
            v = i

    if v == -1 or dist[v] == INF:
        break

    used[v] = True

    for to in range(n):
        if graph[v][to] != -1:
            dist[to] = min(dist[to], dist[v] + graph[v][to])

print(-1 if dist[f] == INF else dist[f])
