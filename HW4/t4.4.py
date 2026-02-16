import math



def f(x):
    return math.sin(x) - x / 3

left = 1.6
right = 3.0

for i in range(100):
    middle = (left + right) / 2
    if f(middle) > 0:
        left = middle
    else:
        right = middle

x = (left + right) / 2
print(f"{x:.10f}")