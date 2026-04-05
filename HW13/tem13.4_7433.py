def convert(A: str, P: int) -> str:
    stack = []

    while A != "0":
        res = []
        cur = 0

        for d in A:
            cur = cur * 10 + int(d)
            res.append(str(cur // P))
            cur %= P

        r = cur
        A = ''.join(res).lstrip('0') or '0'

        stack.append(r)

    result = ""
    while stack:
        x = stack.pop()
        if x <= 9:
            result += str(x)
        else:
            result += "[" + str(x) + "]"

    return result


A = input().strip()
P = int(input().strip())

print(convert(A, P))