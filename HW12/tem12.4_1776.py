while True:
    n = int(input())
    if n == 0:
        break

    while True:
        line = input().strip()
        if line == "0":
            print()
            break

        t = list(map(int, line.split()))
        stack = []
        curr = 1
        ok = True

        for x in t:
            while curr <= n and (not stack or stack[-1] != x):
                stack.append(curr)
                curr += 1

            if stack and stack[-1] == x:
                stack.pop()
            else:
                ok = False
                break

        if ok:
            print("Yes")
        else:
            print("No")