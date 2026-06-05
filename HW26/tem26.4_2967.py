from math import sqrt


def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def prim(cities, n):
    used = [False] * n
    d = [float("inf")] * n

    d[0] = 0
    ans = 0

    for _ in range(n):
        v = -1

        for i in range(n):
            if not used[i] and (v == -1 or d[i] < d[v]):
                v = i

        used[v] = True
        ans += d[v]

        for i in range(n):
            if not used[i]:
                dist = distance(
                    cities[v][0], cities[v][1],
                    cities[i][0], cities[i][1]
                )

                if dist < d[i]:
                    d[i] = dist

    return ans


def main():
    n = int(input())

    cities = []

    for _ in range(n):
        x, y = map(int, input().split())
        cities.append((x, y))

    print(prim(cities, n))


main()