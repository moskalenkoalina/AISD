class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def addToTail(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def Print(self):
        cur = self.head
        while cur is not None:
            print(cur.data, end=" ")
            cur = cur.next
        print()

    def printReverseHelper(self, node):
        if node is None:
            return
        self.printReverseHelper(node.next)
        print(node.data, end=" ")

    def PrintReverse(self):
        self.printReverseHelper(self.head)
        print()


n = int(input())
arr = list(map(int, input().split()))

lst = List()

for x in arr:
    lst.addToTail(x)

lst.Print()
lst.PrintReverse()