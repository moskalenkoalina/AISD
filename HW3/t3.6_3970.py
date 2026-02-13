def lower_bound(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left

def upper_bound(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= x:
            left = mid + 1
        else:
            right = mid
    return left


n = int(input())
colors = list(map(int, input().split()))

m = int(input())
queries = list(map(int, input().split()))

for q in queries:
    print(upper_bound(colors, q) - lower_bound(colors, q))