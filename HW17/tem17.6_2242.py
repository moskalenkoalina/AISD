class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, val):
    if root is None:
        return Node(val)

    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    return root


def preorder(root):
    if root is None:
        return ""

    return root.val + preorder(root.left) + preorder(root.right)


lines = []
while True:
    s = input().strip()
    if s == '*':
        break
    lines.append(s)

root = None
for line in reversed(lines):
    for ch in line:
        root = insert(root, ch)

print(preorder(root))