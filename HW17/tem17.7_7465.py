class TreeNode:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.head = None

    def _insert(self, root, item):
        if root is None:
            return TreeNode(item)

        if item < root.item:
            root.left = self._insert(root.left, item)
        else:
            root.right = self._insert(root.right, item)

        return root

    def Insert(self, item):
        self.head = self._insert(self.head, item)

    def _is_same(self, a, b):
        if a is None and b is None:
            return 1
        if a is None or b is None:
            return 0
        if a.item != b.item:
            return 0
        return self._is_same(a.left, b.left) and self._is_same(a.right, b.right)

    def IsSameTree(self, p):
        return self._is_same(self.head, p.head)
n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

t1 = Tree()
t2 = Tree()

for x in a:
    t1.Insert(x)

for x in b:
    t2.Insert(x)

print(t1.IsSameTree(t2))