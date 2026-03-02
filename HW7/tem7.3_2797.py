SIZE = 200003
table = [None] * SIZE

def insert(number):
    index = number % SIZE

    while table[index] is not None:
        if table[index] == number:
            return False
        index = (index + 1) % SIZE

    table[index] = number
    return True


n = int(input())
numbers = list(map(int, input().split()))

count = 0

for num in numbers:
    if insert(num):
        count += 1

print(count)