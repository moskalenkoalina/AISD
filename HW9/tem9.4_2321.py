def quicksort(a, l, r):
    i = l
    j = r
    pivot = a[(l + r) // 2]

    while i <= j:
        while a[i] < pivot:
            i += 1
        while a[j] > pivot:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

    if l < j:
        quicksort(a, l, j)
    if i < r:
        quicksort(a, i, r)


n = int(input())
a = list(map(int, input().split()))

quicksort(a, 0, n - 1)

print(*a)