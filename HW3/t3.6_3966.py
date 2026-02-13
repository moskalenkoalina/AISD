def binary_search(arr, x):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return False


n = int(input())
collection = list(map(int, input().split()))

m = int(input())
queries = list(map(int, input().split()))

for q in queries:
    if binary_search(collection, q):
        print("YES")
    else:
        print("NO")