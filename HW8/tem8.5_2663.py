n = int(input())
a = list(map(int, input().split()))

count = 0

for i in range(n):
    for j in range(n - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            count += 1

print(count)