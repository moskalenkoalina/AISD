n = int(input())

first = list(map(int, input().split()))
second = list(map(int, input().split()))

moves = 0
LIMIT = 200000

while first and second and moves < LIMIT:
    a = first.pop(0)
    b = second.pop(0)

    if (a == 0 and b == n - 1):
        first.append(a)
        first.append(b)
    elif (a == n - 1 and b == 0):
        second.append(a)
        second.append(b)
    elif a > b:
        first.append(a)
        first.append(b)
    else:
        second.append(a)
        second.append(b)

    moves += 1

if moves >= LIMIT:
    print("draw")
elif not second:
    print("first", moves)
else:
    print("second", moves)