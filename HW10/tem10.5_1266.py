def search(i, current_sum):
    global best_sum

    if current_sum > N:
        return

    if i == s:
        if current_sum > best_sum:
            best_sum = current_sum
        return
    search(i + 1, current_sum + tracks[i])

    search(i + 1, current_sum)

while True:
    try:
        data = list(map(int, input().split()))
    except:
        break

    N = data[0]
    s = data[1]
    tracks = data[2:]

    best_sum = 0

    search(0, 0)

    print("sum:" + str(best_sum))