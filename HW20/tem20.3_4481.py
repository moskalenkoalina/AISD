import math
from math import log2, ceil


class SegmentTree:
    def __init__(self, array):
        k = len(array)
        self.size = 1 << ceil(log2(k))
        self.items = [0] * self.size + array + [0] * (self.size - k)

        for i in range(self.size - 1, 0, -1):
            self.items[i] = math.gcd(self.items[2 * i], self.items[2 * i + 1])

    def update(self, pos, new_value):
        pos += self.size
        self.items[pos] = new_value

        while pos > 1:
            pos //= 2
            self.items[pos] = math.gcd(self.items[2 * pos], self.items[2 * pos + 1])

    def query(self, left, right):
        left += self.size
        right += self.size

        result = 0

        while left <= right:
            if left % 2 == 1:
                result = math.gcd(result, self.items[left])
                left += 1
            if right % 2 == 0:
                result = math.gcd(result, self.items[right])
                right -= 1

            left //= 2
            right //= 2

        return result

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    tree = SegmentTree(arr)
    m = int(input())

    for _ in range(m):
        q, l, r = map(int, input().split())

        if q == 1:
            print(tree.query(l - 1, r - 1))
        else:
            tree.update(l - 1, r)