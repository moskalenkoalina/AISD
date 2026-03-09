n = int(input())
a = list(map(int, input().split()))

for i in range(1, n):
    key = a[i]
    j = i - 1
    changed = False

    while j >= 0 and a[j] > key:
        a[j + 1] = a[j]
        j -= 1
        changed = True

    a[j + 1] = key

    if changed:
        print(*a)