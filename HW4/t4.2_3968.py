import math

C = float(input())

left = 0.0
right = C

for i in range(100):
    middle = (left + right) / 2
    if middle * middle + math.sqrt(middle) > C:
        right = middle
    else:
        left = middle

print(f"{(left + right) / 2:.10f}")