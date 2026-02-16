
def f(x):
    return x**3 + 4*x**2 + x - 6

left = 0
right = 2

for i in range(100):
    middle = (left + right) / 2
    if f(middle) > 0:
        right = middle
    else:
        left = middle

x = (left + right) / 2
print(f"{x:.10f}")