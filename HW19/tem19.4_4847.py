class MaxHeap:
    def __init__(self):
        self.h = []
        self.pos = {}

    def swap(self, i, j):
        self.h[i], self.h[j] = self.h[j], self.h[i]
        self.pos[self.h[i][1]] = i
        self.pos[self.h[j][1]] = j

    def up(self, i):
        while i > 0:
            p = (i - 1) // 2
            if self.h[p][0] >= self.h[i][0]:
                break
            self.swap(i, p)
            i = p

    def down(self, i):
        n = len(self.h)
        while True:
            l = 2*i + 1
            r = 2*i + 2
            m = i

            if l < n and self.h[l][0] > self.h[m][0]:
                m = l
            if r < n and self.h[r][0] > self.h[m][0]:
                m = r

            if m == i:
                break

            self.swap(i, m)
            i = m

    def add(self, id, p):
        self.h.append((p, id))
        self.pos[id] = len(self.h) - 1
        self.up(len(self.h) - 1)

    def change(self, id, p):
        i = self.pos[id]
        old = self.h[i][0]
        self.h[i] = (p, id)

        if p > old:
            self.up(i)
        else:
            self.down(i)

    def pop(self):
        p, id = self.h[0]
        print(id, p)

        last = self.h.pop()
        del self.pos[id]

        if self.h:
            self.h[0] = last
            self.pos[last[1]] = 0
            self.down(0)

if __name__ == "__main__":
    heap = MaxHeap()

    with open("input.txt") as f:
        for line in f:
            s = line.split()

            if s[0] == "ADD":
                heap.add(s[1], int(s[2]))
            elif s[0] == "CHANGE":
                heap.change(s[1], int(s[2]))
            else:
                heap.pop()