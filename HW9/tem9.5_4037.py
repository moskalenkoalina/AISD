def merge_sort(a):
    if len(a) <= 1:
        return a

    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


n = int(input())
robots = []

for _ in range(n):
    a, b = map(int, input().split())
    robots.append((a, b))

robots = merge_sort(robots)

for a, b in robots:
    print(a, b)