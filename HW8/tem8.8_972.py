n = int(input())

times = []
for _ in range(n):
    h, m, s = map(int, input().split())
    times.append([h, m, s])

for i in range(1, n):
    key = times[i]
    j = i - 1

    while j >= 0 and (
        times[j][0] > key[0] or
        (times[j][0] == key[0] and times[j][1] > key[1]) or
        (times[j][0] == key[0] and times[j][1] == key[1] and times[j][2] > key[2])
    ):
        times[j + 1] = times[j]
        j -= 1

    times[j + 1] = key

for t in times:
    print(t[0], t[1], t[2])