n, m = map(int, input().split())
edges = set()

for i in range(m):
    u, v = map(int, input().split())

    if u > v:
        u, v = v, u

    edges.add((u, v))

if len(edges) == n * (n - 1) // 2:
    print("YES")
else:
    print("NO")