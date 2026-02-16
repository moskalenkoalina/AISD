
def f(x):
    return x**3+x+1

left = 0
right = 10

for i in range(100):
    middle = (left + right) / 2
    if f(middle) > 5:
        right = middle
    else:
        left = middle

x = (left +right) / 2
print(f"{x:.10f}")