n, k = map(int, input().split())

used = [False] * (n + 1)
perm = []


def generate():
    if len(perm) == k:
        print(*perm)
        return

    for i in range(1, n + 1):
        if not used[i]:
            used[i] = True
            perm.append(i)

            generate()

            perm.pop()
            used[i] = False


generate()