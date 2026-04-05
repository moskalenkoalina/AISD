s = input().strip()

priority = {'+':1, '-':1, '*':2, '/':2}

stack = []

for ch in reversed(s):
    if ch.isalpha():
        stack.append( (ch, 3) )
    else:
        a, pa = stack.pop()
        b, pb = stack.pop()
        p = priority[ch]

        if pa < p:
            a = f"({a})"
        if pb < p or (ch in "-/" and pb == p):
            b = f"({b})"

        stack.append( (a + ch + b, p) )

print(stack[0][0])