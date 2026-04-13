class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def AddToTail(self, val: int) -> None:
        new_node = Node(val)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def RotateRight(self, k: int) -> None:
        if self.head is None or self.head.next is None:
            return

        n = 1
        cur = self.head
        while cur.next:
            cur = cur.next
            n += 1

        self.tail = cur

        k = k % n
        if k == 0:
            return

        self.tail.next = self.head

        steps = n - k
        new_tail = self.head
        for _ in range(steps - 1):
            new_tail = new_tail.next

        new_head = new_tail.next

        new_tail.next = None

        self.head = new_head
        self.tail = new_tail

    def Print(self) -> None:
        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next
        print()

n = int(input())

lst = List()

numbers = input().split()
for i in range(n):
    lst.AddToTail(int(numbers[i]))

while True:
    try:
        line = input().strip()
        if line == "":
            continue
        k = int(line)

        lst.RotateRight(k)
        lst.Print()
    except:
        break
