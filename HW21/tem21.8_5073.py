n, m = map(int, input().split())

edges = set()

for i in range(m):
    u, v = map(int, input().split())

    if (u, v) in edges:
        print("YES")
        exit()
    edges.add((u, v))

print("NO")