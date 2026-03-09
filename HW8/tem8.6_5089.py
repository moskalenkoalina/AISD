n = int(input())

words = []
for i in range(n):
    words.append(input())

for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if words[j] < words[min_index]:
            min_index = j

    words[i], words[min_index] = words[min_index], words[i]

for j in words:
    print(j)