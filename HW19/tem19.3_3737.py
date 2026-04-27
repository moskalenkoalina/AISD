n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    if 2*i+1 < n and a[i] > a[2*i+1]:
        print("NO")
        exit()
    if 2*i+2 < n and a[i] > a[2*i+2]:
        print("NO")
        exit()

print("YES")