def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a != b:
        parent[b] = a


def solve_case(n, m, p, q):
    roads = []
    w_pq = -1

    for _ in range(m):
        u, v, w = map(int, input().split())
        roads.append((u, v, w))

        if (u == p and v == q) or (u == q and v == p):
            w_pq = w

    parent = list(range(n + 1))

    for u, v, w in roads:
        if w < w_pq:
            union(parent, u, v)

    if find(parent, p) == find(parent, q):
        return "NO"
    else:
        return "YES"


def main():
    t = int(input())

    for _ in range(t):
        n, m, p, q = map(int, input().split())
        print(solve_case(n, m, p, q))


main()