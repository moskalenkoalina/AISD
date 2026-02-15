
n = int(input("Введіть кількість предметів: "))
a = list(map(int, input("Введіть кількість одиниць води:").split()))
k = int(input("Введіть кількість води, що втрачається:"))

l = 0
r = max(a)

if k <= 1:
    print(r)
else:
    while l < r:
        m = (l + r) // 2
        dry = 0

        for water in a:
            if water > m:
                dry += (water - m + k - 2) // (k - 1)
            if dry > m:
                break

        if dry > m:
            l = m + 1
        else:
            r = m

    print("Мінімальна кількість хвилин для повного висушування всіх предметів:",l)