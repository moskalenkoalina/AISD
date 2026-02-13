n = int(input())

b = bin(n)[2:]
k = len(b)

max_value = 0

for i in range(k):
    shifted = b[i:] + b[:i]

    value = int(shifted, 2)

    if value > max_value:
        max_value = value

print(max_value)