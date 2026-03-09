n = int(input())
a = list(map(int, input().split()))

first_value = a[0]
count = 0

for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if a[j] < a[min_index]:
            min_index = j
    if min_index != i:
        # перевірка,чи бере участь перший елемент
        if a[i] == first_value or a[min_index] == first_value:
            count += 1
        # міняємо місцями
        a[i], a[min_index] = a[min_index], a[i]

print(count)