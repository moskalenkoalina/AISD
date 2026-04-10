class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def push_front(self, x):
        node = Node(int(x))

        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        self._size += 1
        return "ok"

    def push_back(self, x):
        node = Node(int(x))

        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self._size += 1
        return "ok"

    def pop_front(self):
        if self.head is None:
            return "error"

        value = self.head.value
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None

        self._size -= 1
        return value

    def pop_back(self):
        if self.tail is None:
            return "error"

        value = self.tail.value
        self.tail = self.tail.prev

        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None

        self._size -= 1
        return value

    def front(self):
        if self.head is None:
            return "error"
        return self.head.value

    def back(self):
        if self.tail is None:
            return "error"
        return self.tail.value

    def size(self):
        return self._size

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)


if __name__ == "__main__":
    d = Deque()

    while True:
        command = input()
        result = d.execute(command)
        print(result)

        if command == "exit":
            break